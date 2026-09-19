#!/usr/bin/env python3
"""Render a circular avatar with a gradient ring from veera.jpg.

GitHub's markdown sanitiser strips `style`, so `border-radius` is unavailable —
a round avatar has to be baked into the raster. This also keys the photo's white
cut-out background onto a dark backdrop so the avatar sits on GitHub's dark
theme instead of reading as a white sticker.

Output: assets/avatar.png (440x440, RGBA)

Usage:
    python3 scripts/generate_avatar.py
"""

from __future__ import annotations

import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFilter
except ImportError:  # pragma: no cover
    sys.exit("Pillow is required: pip install Pillow")

SRC = "veera.jpg"
OUT = "assets/avatar.png"
SIZE = 440
SS = 4  # supersample factor for smooth edges

# Square crop over head and shoulders of the 390x435 source.
CROP = (6, 16, 346, 356)

BACKDROP_INNER = (30, 27, 75)
BACKDROP_OUTER = (8, 13, 30)
RING_FROM = (34, 211, 238)
RING_TO = (167, 139, 250)

WHITE_CUTOFF = 232  # luminance above which the cut-out background starts
SPREAD = 20         # soft ramp so edges feather instead of stair-stepping


def subject_over_backdrop(photo: Image.Image, size: int) -> Image.Image:
    """Replace the near-white cut-out background with a dark radial gradient."""
    photo = photo.convert("RGB").resize((size, size), Image.LANCZOS)

    # Alpha from luminance: dark pixels (the subject) opaque, white bg clear.
    grey = photo.convert("L")
    alpha = grey.point(
        lambda v: 255 if v < WHITE_CUTOFF
        else (0 if v > WHITE_CUTOFF + SPREAD
              else int(255 * (WHITE_CUTOFF + SPREAD - v) / SPREAD))
    )
    alpha = alpha.filter(ImageFilter.GaussianBlur(size / 320))

    backdrop = Image.new("RGB", (size, size))
    px = backdrop.load()
    cx = cy = (size - 1) / 2
    maxd = (size / 2) ** 2
    for y in range(size):
        for x in range(size):
            d = ((x - cx) ** 2 + (y - cy) ** 2) / maxd
            t = min(d, 1.0)
            px[x, y] = tuple(
                int(round(BACKDROP_INNER[c] + (BACKDROP_OUTER[c] - BACKDROP_INNER[c]) * t))
                for c in range(3)
            )

    subject = photo.copy()
    subject.putalpha(alpha)
    out = backdrop.convert("RGBA")
    out.alpha_composite(subject)
    return out


def ring(size: int, width: int) -> Image.Image:
    """Annulus filled with a diagonal cyan-to-violet ramp."""
    ramp = Image.new("RGB", (size, size))
    px = ramp.load()
    for y in range(size):
        for x in range(size):
            t = (x + y) / (2 * (size - 1))
            px[x, y] = tuple(
                int(round(RING_FROM[c] + (RING_TO[c] - RING_FROM[c]) * t)) for c in range(3)
            )
    mask = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse([0, 0, size - 1, size - 1], fill=255)
    d.ellipse([width, width, size - 1 - width, size - 1 - width], fill=0)
    band = ramp.convert("RGBA")
    band.putalpha(mask)
    return band


def main() -> int:
    if not os.path.exists(SRC):
        sys.exit(f"{SRC} not found — run from the repository root")

    big = SIZE * SS
    photo = Image.open(SRC).crop(CROP)

    face = subject_over_backdrop(photo, big // 2).resize((big, big), Image.LANCZOS)

    # Clip the portrait to a circle, leaving room for the ring.
    inset = int(big * 0.035)
    mask = Image.new("L", (big, big), 0)
    ImageDraw.Draw(mask).ellipse([inset, inset, big - 1 - inset, big - 1 - inset], fill=255)

    canvas = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    canvas.paste(face, (0, 0), mask)
    canvas.alpha_composite(ring(big, int(big * 0.030)))

    out = canvas.resize((SIZE, SIZE), Image.LANCZOS)
    os.makedirs("assets", exist_ok=True)
    out.save(OUT, "PNG", optimize=True)
    print(f"wrote {OUT} ({os.path.getsize(OUT):,} bytes, {SIZE}x{SIZE})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
