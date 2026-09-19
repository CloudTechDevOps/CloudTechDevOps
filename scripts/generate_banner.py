#!/usr/bin/env python3
"""Render the profile banner as a real PNG.

The previous banner was an SVG. That renders fine on github.com, but SVG is not
displayed by most link-preview and social scrapers (LinkedIn, Slack, X), so the
banner vanished wherever the profile was shared. A raster PNG renders anywhere.

Generating it also lets the side panel carry live figures from the GitHub API
instead of an unverifiable hardcoded claim.

Output: assets/banner.png at 2x scale (2400x720) for crisp display at 1200px.

Usage:
    GITHUB_TOKEN=... ACCOUNT=CloudTechDevOps python3 scripts/generate_banner.py

Statistics may also be supplied via REPOS / FORKS / STARS / FOLLOWERS
environment variables, which the workflow does to avoid a second API round trip.

Implementation note: every translucent element is drawn onto its own RGBA layer
and alpha-composited. Drawing a low-alpha colour directly onto the canvas with
ImageDraw overwrites the alpha channel rather than blending, which turns a
subtle 5%-opacity line into solid white once the image is flattened to RGB.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.request
from typing import Callable

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
except ImportError:  # pragma: no cover
    sys.exit("Pillow is required: pip install Pillow")

SCALE = 2
W, H = 1200 * SCALE, 360 * SCALE

BG_STOPS = [
    (0.00, (2, 6, 23)),
    (0.38, (30, 27, 75)),
    (0.72, (49, 46, 129)),
    (1.00, (13, 90, 115)),
]
CYAN = (34, 211, 238)
ICE_CYAN = (103, 232, 249)
VIOLET = (167, 139, 250)
GREEN = (52, 211, 153)
PINK = (244, 114, 182)
AMBER = (251, 191, 36)
ICE = (165, 243, 252)
MIST = (224, 242, 254)
SLATE = (148, 163, 184)
WHITE = (255, 255, 255)

FONT_CANDIDATES = {
    "regular": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ],
    "bold": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    ],
    "mono": [
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
        "/System/Library/Fonts/Supplemental/Courier New.ttf",
    ],
}


def resolve_fonts() -> dict[str, str]:
    chosen: dict[str, str] = {}
    for kind, paths in FONT_CANDIDATES.items():
        for path in paths:
            if os.path.exists(path):
                chosen[kind] = path
                break
        else:
            sys.exit(f"No {kind} font found. Tried: {paths}")
    return chosen


FONTS = resolve_fonts()
_cache: dict[tuple[str, int], ImageFont.FreeTypeFont] = {}


def font(kind: str, size: int) -> ImageFont.FreeTypeFont:
    key = (kind, size)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(FONTS[kind], size * SCALE)
    return _cache[key]


def measure(body: str, kind: str, size: int) -> int:
    box = font(kind, size).getbbox(body)
    return int(box[2] - box[0]) // SCALE


def on_layer(canvas: Image.Image, paint: Callable[[ImageDraw.ImageDraw], None]) -> None:
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    paint(ImageDraw.Draw(layer))
    canvas.alpha_composite(layer)


def lerp(a: int, b: int, t: float) -> int:
    return int(round(a + (b - a) * t))


def sample(t: float) -> tuple[int, int, int]:
    t = min(max(t, 0.0), 1.0)
    lo, hi = BG_STOPS[0], BG_STOPS[-1]
    for i in range(len(BG_STOPS) - 1):
        if BG_STOPS[i][0] <= t <= BG_STOPS[i + 1][0]:
            lo, hi = BG_STOPS[i], BG_STOPS[i + 1]
            break
    span = (hi[0] - lo[0]) or 1
    k = (t - lo[0]) / span
    return tuple(lerp(lo[1][c], hi[1][c], k) for c in range(3))


def background() -> Image.Image:
    """True diagonal gradient, built small and upscaled so it stays smooth."""
    n = 96
    small = Image.new("RGB", (n, n))
    px = small.load()
    for y in range(n):
        for x in range(n):
            px[x, y] = sample((x / (n - 1) + y / (n - 1)) / 2)
    return small.resize((W, H), Image.BICUBIC).convert("RGBA")


def blob(canvas: Image.Image, cx: int, cy: int, radius: int, color, peak: float) -> None:
    cx, cy, radius = cx * SCALE, cy * SCALE, radius * SCALE

    def paint(draw: ImageDraw.ImageDraw) -> None:
        steps = 30
        for i in range(steps, 0, -1):
            frac = i / steps
            r = int(radius * frac)
            alpha = int(255 * peak * (1 - frac) ** 1.6)
            if alpha > 0:
                draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (alpha,))

    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    paint(ImageDraw.Draw(layer))
    canvas.alpha_composite(layer.filter(ImageFilter.GaussianBlur(26 * SCALE)))


def glass(
    canvas: Image.Image,
    box: tuple[int, int, int, int],
    radius: int,
    fill_alpha: int = 28,
    stroke_alpha: int = 78,
) -> None:
    x0, y0, x1, y1 = (v * SCALE for v in box)
    on_layer(
        canvas,
        lambda d: d.rounded_rectangle(
            [x0, y0, x1, y1],
            radius=radius * SCALE,
            fill=WHITE + (fill_alpha,),
            outline=WHITE + (stroke_alpha,),
            width=max(1, int(1.4 * SCALE)),
        ),
    )


def label(
    canvas: Image.Image,
    xy: tuple[int, int],
    body: str,
    kind: str,
    size: int,
    color,
    alpha: int = 255,
    anchor: str = "ls",
) -> None:
    on_layer(
        canvas,
        lambda d: d.text(
            (xy[0] * SCALE, xy[1] * SCALE),
            body,
            font=font(kind, size),
            fill=color + (alpha,),
            anchor=anchor,
        ),
    )


def pills(canvas: Image.Image, labels: list[str], x: int, y: int, size: int = 12) -> None:
    """Auto-width chips. The old SVG hardcoded each pill width, so substituting
    a wider fallback font risked the label spilling past its rounded rect."""
    pad, gap, height = 14, 8, 26
    cursor = x
    for text_body in labels:
        width = measure(text_body, "bold", size) + pad * 2
        glass(canvas, (cursor, y, cursor + width, y + height), height // 2, 40, 66)
        label(canvas, (cursor + width // 2, y + 18), text_body, "bold", size, MIST, anchor="ms")
        cursor += width + gap


def fetch_stats(account: str) -> dict[str, str]:
    supplied = {k: os.environ.get(k) for k in ("REPOS", "FORKS", "STARS", "FOLLOWERS")}
    if all(supplied.values()):
        return {k: v for k, v in supplied.items() if v}

    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        sys.exit("Provide REPOS/FORKS/STARS/FOLLOWERS or GITHUB_TOKEN")

    def api(path: str):
        req = urllib.request.Request(
            f"https://api.github.com/{path}",
            headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
                "User-Agent": "banner-generator",
            },
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)

    user = api(f"users/{account}")
    repos = api(f"users/{account}/repos?per_page=100&type=owner")
    return {
        "REPOS": str(user["public_repos"]),
        "FOLLOWERS": str(user["followers"]),
        "FORKS": str(sum(r["forks_count"] for r in repos)),
        "STARS": str(sum(r["stargazers_count"] for r in repos)),
    }


def build(stats: dict[str, str]) -> Image.Image:
    canvas = background()

    blob(canvas, 150, 80, 150, CYAN, 0.60)
    blob(canvas, 470, 320, 175, VIOLET, 0.42)
    blob(canvas, 1000, 60, 150, GREEN, 0.38)
    blob(canvas, 920, 320, 120, PINK, 0.30)
    blob(canvas, 380, 40, 95, CYAN, 0.28)

    # Faint structural rules, composited so they stay at true low opacity.
    on_layer(
        canvas,
        lambda d: [
            d.line([(0, y * SCALE), (W, y * SCALE)], fill=WHITE + (10,), width=SCALE)
            for y in (120, 200, 280)
        ]
        and None,
    )

    # Terminal-style top bar
    glass(canvas, (60, 26, 1140, 78), 26, 24, 68)
    for i, dot in enumerate((PINK, AMBER, GREEN)):
        cx, cy, r = 86 + i * 18, 52, 5
        on_layer(
            canvas,
            lambda d, cx=cx, dot=dot, r=r, cy=cy: d.ellipse(
                [(cx - r) * SCALE, (cy - r) * SCALE, (cx + r) * SCALE, (cy + r) * SCALE],
                fill=dot + (255,),
            ),
        )
    label(canvas, (150, 57), "~/veerababu-narni  \u203a  senior-devops-architect --status active", "mono", 12, ICE)
    tagline = "\u25cf 24,400+ engineers trained"
    label(canvas, (1114 - measure(tagline, "mono", 12), 57), tagline, "mono", 12, ICE_CYAN)

    # Identity panel
    glass(canvas, (60, 102, 776, 306), 26, 30, 86)
    label(canvas, (96, 170), "Veerababu Narni", "bold", 37, WHITE)
    label(canvas, (96, 201), "Senior DevOps & Multi-Cloud Architect", "regular", 16, MIST, 238)
    label(canvas, (96, 236), "15+ yrs \u00b7 AWS \u00b7 Azure \u00b7 GCP \u00b7 Kubernetes \u00b7 Terraform", "mono", 12, ICE_CYAN)
    pills(canvas, ["AWS \u00b7 Azure", "GCP", "Kubernetes \u00b7 CKA", "Terraform", "Gen AI \u00b7 Agentic AI"], 96, 260)

    # Live status panel, vertically aligned with the identity panel
    glass(canvas, (800, 102, 1140, 306), 26, 30, 86)
    label(canvas, (828, 130), "SYSTEM.STATUS", "mono", 11, SLATE)

    y = 162
    for value, caption in (
        ("15+", "years experience"),
        ("24,400+", "engineers trained"),
        (stats["FOLLOWERS"], "github followers"),
    ):
        label(canvas, (828, y), value, "bold", 24, WHITE)
        label(canvas, (828, y + 17), caption, "regular", 11, SLATE)
        y += 48

    live = f"{stats['REPOS']} repos \u00b7 {stats['FORKS']} forks \u00b7 {stats['STARS']} stars"
    label(canvas, (828, 296), live, "mono", 11, ICE_CYAN)

    return canvas.convert("RGB")


def main() -> int:
    account = os.environ.get("ACCOUNT", "CloudTechDevOps")
    stats = fetch_stats(account)
    print("banner stats:", stats)
    print("fonts:", {k: os.path.basename(v) for k, v in FONTS.items()})

    os.makedirs("assets", exist_ok=True)
    out = "assets/banner.png"
    build(stats).save(out, "PNG", optimize=True)
    print(f"wrote {out} ({os.path.getsize(out):,} bytes, {W}x{H})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
