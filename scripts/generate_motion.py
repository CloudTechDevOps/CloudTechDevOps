#!/usr/bin/env python3
"""Generate the animated SVGs used by the profile README.

GitHub renders README images through <img>, so no JavaScript runs. Motion is
done with CSS keyframes and SMIL (<animate>, <animateMotion>, <set>), both of
which survive GitHub's image proxy untouched. Fonts are system stacks because
an SVG loaded as an image cannot fetch web fonts.

Outputs (all under assets/motion/):
    hero.svg          name, title, typed role lines, avatar with orbit ring
    metrics.svg       count-up headline numbers
    genai-rag.svg     RAG pipeline with data packets flowing between stages
    agentic-loop.svg  agent -> MCP tools -> human approval -> execute loop
    fde-journey.svg   five-phase forward deployed engineering timeline
    divider.svg       light sweep divider
    footer.svg        animated wave footer

Usage:
    python3 scripts/generate_motion.py
"""

from __future__ import annotations

import base64
import io
import os
from html import escape

try:
    from PIL import Image
except ImportError:  # the avatar is optional; everything else is pure text
    Image = None

OUT_DIR = "assets/motion"
AVATAR = "assets/avatar.png"

SANS = "Segoe UI, Helvetica Neue, Helvetica, Arial, sans-serif"
MONO = "Consolas, Menlo, Courier New, monospace"

INK = "#020617"
NAVY = "#0f172a"
INDIGO = "#1e1b4b"
CYAN = "#22d3ee"
ICE = "#67e8f9"
VIOLET = "#a78bfa"
PINK = "#f472b6"
GREEN = "#34d399"
AMBER = "#fbbf24"
WHITE = "#f8fafc"
MIST = "#cbd5e1"
SLATE = "#94a3b8"

# Pauses CSS motion for viewers who ask for less of it. SMIL has no media
# query hook, so SMIL is kept to small travelling dots and one-shot reveals.
REDUCED = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"

GLOW = """<filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
  <feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>"""

BRAND = f"""<linearGradient id="brand" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="{CYAN}"/><stop offset="50%" stop-color="{VIOLET}"/><stop offset="100%" stop-color="{PINK}"/>
</linearGradient>"""

PANEL = f"""<linearGradient id="panel" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#ffffff" stop-opacity="0.10"/><stop offset="100%" stop-color="#ffffff" stop-opacity="0.03"/>
</linearGradient>"""


def background(w: int, h: int, rx: int = 22) -> str:
    """Rounded dark card with a faint grid, shared by every diagram."""
    return f"""<linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="{INK}"/><stop offset="55%" stop-color="{NAVY}"/><stop offset="100%" stop-color="{INDIGO}"/>
</linearGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
  <path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity="0.045"/>
</pattern>
<clipPath id="card"><rect width="{w}" height="{h}" rx="{rx}"/></clipPath>
</defs>
<g clip-path="url(#card)">
<rect width="{w}" height="{h}" fill="url(#bg)"/>
<rect width="{w}" height="{h}" fill="url(#grid)"/>"""


def svg(w: int, h: int, label: str, defs: str, style: str, body: str) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100%" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}">
<title>{escape(label)}</title>
<style>{style}{REDUCED}</style>
<defs>
{GLOW}
{BRAND}
{PANEL}
{defs}
{body}
</g>
<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="22" fill="none" stroke="#ffffff" stroke-opacity="0.12"/>
</svg>
"""


def text(x, y, body, size, fill=WHITE, weight=400, family=SANS, anchor="start", extra=""):
    return (
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
        f'fill="{fill}" text-anchor="{anchor}" {extra}>{escape(body)}</text>'
    )


def node(x, y, w, h, title, sub, accent, cls=""):
    """Glass node with an accent bar, a title and a one-line caption."""
    return f"""<g class="{cls}">
  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="url(#panel)" stroke="{accent}" stroke-opacity="0.55"/>
  <rect x="{x + 14}" y="{y + 12}" width="26" height="3" rx="1.5" fill="{accent}"/>
  {text(x + 14, y + 36, title, 15, WHITE, 600)}
  {text(x + 14, y + 55, sub, 11.5, SLATE)}
</g>"""


def flow(pid, d, color, dur, dots=2, delay=0.0):
    """A dashed path with light packets travelling along it."""
    out = [
        f'<path id="{pid}" d="{d}" fill="none" stroke="{color}" stroke-opacity="0.25" stroke-width="2"/>',
        f'<path d="{d}" fill="none" stroke="{color}" stroke-opacity="0.8" stroke-width="2" '
        f'stroke-dasharray="6 10" class="dash"/>',
    ]
    for i in range(dots):
        begin = delay + i * dur / dots
        out.append(
            f'<circle r="4" fill="{color}" filter="url(#glow)">'
            f'<animateMotion dur="{dur}s" begin="{begin:.2f}s" repeatCount="indefinite" rotate="auto">'
            f'<mpath xlink:href="#{pid}"/></animateMotion></circle>'
        )
    return "\n".join(out)


DASH = ".dash{animation:dash 1.2s linear infinite}@keyframes dash{to{stroke-dashoffset:-32}}"


def avatar_data_uri(size: int = 240) -> str | None:
    if Image is None or not os.path.exists(AVATAR):
        return None
    img = Image.open(AVATAR).convert("RGB").resize((size, size), Image.LANCZOS)
    buf = io.BytesIO()
    img.save(buf, "JPEG", quality=86, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


# --------------------------------------------------------------------------- hero

ROLES = [
    "Turning AI use cases into production systems",
    "Shipping Generative AI & RAG to production",
    "Building Agentic AI that operates infrastructure",
    "AWS · Azure · GCP · Kubernetes · Terraform",
]


def hero() -> str:
    w, h = 1200, 460
    size, char = 19, 0.6 * 19  # textLength pins every glyph to this width
    slot = 4.0
    total = slot * len(ROLES)
    x0, ty = 70, 262

    typed = []
    cursor_vals, cursor_keys = [x0], [0.0]
    for i, role in enumerate(ROLES):
        line = "› " + role
        width = round(char * len(line), 1)
        t0, t1, t2, t3 = i * slot, i * slot + 1.5, i * slot + 3.3, i * slot + 3.8
        keys = [0, t0, t1, t2, t3, total]
        vals = [0, 0, width, width, 0, 0]
        if i == 0:
            keys, vals = keys[1:], vals[1:]
        uniq_k, uniq_v = [], []
        for k, v in zip(keys, vals):
            if uniq_k and abs(k - uniq_k[-1]) < 1e-9:
                uniq_v[-1] = v
                continue
            uniq_k.append(k)
            uniq_v.append(v)
        kt = ";".join(f"{k / total:.4f}" for k in uniq_k)
        vs = ";".join(str(v) for v in uniq_v)
        typed.append(
            f"""<clipPath id="type{i}"><rect x="{x0}" y="{ty - 24}" width="0" height="34">
  <animate attributeName="width" values="{vs}" keyTimes="{kt}" dur="{total}s" repeatCount="indefinite"/></rect></clipPath>
<text x="{x0}" y="{ty}" font-family="{MONO}" font-size="{size}" fill="{ICE}" textLength="{width}" lengthAdjust="spacingAndGlyphs" clip-path="url(#type{i})">{escape(line)}</text>"""
        )
        for k, v in zip([t0, t1, t2, t3], [0, width, width, 0]):
            if k == 0:
                continue
            cursor_keys.append(k)
            cursor_vals.append(x0 + v + 3)
    cursor_keys.append(total)
    cursor_vals.append(x0)
    ckt = ";".join(f"{k / total:.4f}" for k in cursor_keys)
    cvs = ";".join(f"{v:.1f}" for v in cursor_vals)

    chips = ["AWS · Azure · GCP", "Kubernetes", "Terraform", "Gen AI", "Agentic AI", "FDE"]
    chip_svg, cx = [], x0
    for i, chip in enumerate(chips):
        cw = int(len(chip) * 7.6 + 30)
        ai = chip in ("Gen AI", "Agentic AI", "FDE")
        stroke = VIOLET if ai else ICE
        chip_svg.append(
            f"""<g class="rise" style="animation-delay:{0.9 + i * 0.12:.2f}s">
  <rect x="{cx}" y="318" width="{cw}" height="32" rx="16" fill="url(#panel)" stroke="{stroke}" stroke-opacity="0.6"/>
  {text(cx + cw / 2, 339, chip, 13, WHITE, 600, anchor="middle")}
</g>"""
        )
        cx += cw + 10

    avatar = avatar_data_uri()
    acx, acy, ar = 1000, 240, 112
    photo = (
        f'<image href="{avatar}" x="{acx - ar}" y="{acy - ar}" width="{ar * 2}" height="{ar * 2}" clip-path="url(#face)" preserveAspectRatio="xMidYMid slice"/>'
        if avatar
        else f'<circle cx="{acx}" cy="{acy}" r="{ar}" fill="{INDIGO}"/>'
    )
    orbiters = "\n".join(
        f"""<g><animateTransform attributeName="transform" type="rotate" from="{a} {acx} {acy}" to="{a + sign * 360} {acx} {acy}" dur="{d}s" repeatCount="indefinite"/>
  <circle cx="{acx}" cy="{acy - r}" r="{dot}" fill="{c}" filter="url(#glow)"/></g>"""
        for a, sign, d, r, dot, c in [
            (0, 1, 9, 136, 5, ICE),
            (140, 1, 9, 136, 3.5, VIOLET),
            (60, -1, 14, 156, 4, PINK),
            (250, -1, 14, 156, 3, GREEN),
        ]
    )

    style = f"""
.blob{{animation:drift 16s ease-in-out infinite alternate}}
.b2{{animation-duration:20s;animation-delay:-6s}}.b3{{animation-duration:24s;animation-delay:-12s}}
@keyframes drift{{0%{{transform:translate(0,0)}}50%{{transform:translate(70px,-40px)}}100%{{transform:translate(-50px,30px)}}}}
.scan{{animation:scan 7s linear infinite}}@keyframes scan{{from{{transform:translateY(-20px)}}to{{transform:translateY(480px)}}}}
.rise{{animation:rise .8s cubic-bezier(.2,.7,.2,1) both}}
@keyframes rise{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:none}}}}
.blink{{animation:blink 1s steps(1) infinite}}@keyframes blink{{50%{{opacity:0}}}}
.pulse{{animation:pulse 2s ease-in-out infinite}}@keyframes pulse{{50%{{opacity:.25}}}}
.spin{{transform-origin:{acx}px {acy}px;animation:spin 18s linear infinite}}.spin.r{{animation-duration:26s;animation-direction:reverse}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
"""
    defs = f"""<linearGradient id="name" x1="70" y1="0" x2="620" y2="0" gradientUnits="userSpaceOnUse">
  <stop offset="0%" stop-color="{WHITE}"/><stop offset="35%" stop-color="{ICE}"/><stop offset="65%" stop-color="{VIOLET}"/><stop offset="100%" stop-color="{WHITE}"/>
  <animateTransform attributeName="gradientTransform" type="translate" values="-600 0;600 0;-600 0" dur="10s" repeatCount="indefinite"/>
</linearGradient>
<linearGradient id="ring" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="{CYAN}"/><stop offset="50%" stop-color="{VIOLET}"/><stop offset="100%" stop-color="{PINK}"/>
</linearGradient>
<linearGradient id="scanG" x1="0%" y1="0%" x2="0%" y2="100%">
  <stop offset="0%" stop-color="{CYAN}" stop-opacity="0"/><stop offset="100%" stop-color="{CYAN}" stop-opacity="0.10"/>
</linearGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="60"/></filter>
<clipPath id="face"><circle cx="{acx}" cy="{acy}" r="{ar}"/></clipPath>
{"".join(t.split("</clipPath>")[0] + "</clipPath>" for t in typed)}
{background(w, h)}"""

    body = f"""
<g filter="url(#blur)" opacity="0.55">
  <circle class="blob" cx="260" cy="120" r="170" fill="{CYAN}" opacity="0.45"/>
  <circle class="blob b2" cx="760" cy="380" r="190" fill="{VIOLET}" opacity="0.5"/>
  <circle class="blob b3" cx="1050" cy="90" r="150" fill="{PINK}" opacity="0.35"/>
</g>
<rect class="scan" x="0" y="0" width="{w}" height="70" fill="url(#scanG)"/>

<g class="rise">
  <rect x="40" y="26" width="{w - 80}" height="46" rx="23" fill="url(#panel)" stroke="#ffffff" stroke-opacity="0.18"/>
  <circle cx="66" cy="49" r="5" fill="{PINK}"/><circle cx="84" cy="49" r="5" fill="{AMBER}"/><circle cx="102" cy="49" r="5" fill="{GREEN}"/>
  {text(126, 54, "~/veerababu-narni  ›  cloud-devops-ai-fde --status active", 13, ICE, family=MONO)}
  <circle class="pulse" cx="1036" cy="49" r="5" fill="{GREEN}"/>
  {text(1048, 54, "AVAILABLE · FDE", 12, GREEN, 600, MONO)}
</g>

<g class="rise" style="animation-delay:.15s">
  {text(x0, 128, "HELLO, I'M", 14, ICE, 600, MONO, extra='letter-spacing="4"')}
  <text x="{x0}" y="186" font-family="{SANS}" font-size="56" font-weight="800" fill="url(#name)">Veerababu Narni</text>
</g>
<g class="rise" style="animation-delay:.35s">
  {text(x0, 222, "Cloud DevOps & AI Forward Deployed Engineer", 23, MIST, 500)}
</g>

{"".join(t.split("</clipPath>")[1] for t in typed)}
<rect class="blink" x="{x0}" y="{ty - 18}" width="10" height="22" fill="{ICE}">
  <animate attributeName="x" values="{cvs}" keyTimes="{ckt}" dur="{total}s" repeatCount="indefinite"/>
</rect>

{"".join(chip_svg)}

{text(x0, 400, "15+ yrs   ·   30K+ students trained   ·   30+ real projects   ·   3 clouds + AI & FDE", 13.5, SLATE, 500, MONO)}

<g class="rise" style="animation-delay:.5s">
  <circle cx="{acx}" cy="{acy}" r="{ar + 30}" fill="{VIOLET}" opacity="0.10" filter="url(#glow)"/>
  <circle class="spin" cx="{acx}" cy="{acy}" r="{ar + 10}" fill="none" stroke="url(#ring)" stroke-width="3" stroke-dasharray="120 40 30 40"/>
  <circle class="spin r" cx="{acx}" cy="{acy}" r="{ar + 22}" fill="none" stroke="{ICE}" stroke-opacity="0.35" stroke-dasharray="2 9"/>
  {photo}
  <circle cx="{acx}" cy="{acy}" r="{ar}" fill="none" stroke="#ffffff" stroke-opacity="0.25" stroke-width="2"/>
  {orbiters}
  <rect x="{acx - 74}" y="{acy + ar + 34}" width="148" height="30" rx="15" fill="{NAVY}" stroke="{GREEN}" stroke-opacity="0.7"/>
  <circle class="pulse" cx="{acx - 54}" cy="{acy + ar + 49}" r="4.5" fill="{GREEN}"/>
  {text(acx + 8, acy + ar + 54, "Building with AI", 12.5, WHITE, 600, anchor="middle")}
</g>
"""
    return svg(w, h, "Veerababu Narni — Cloud DevOps & AI Forward Deployed Engineer", defs, style, body)


# ------------------------------------------------------------------------ metrics

METRICS = [
    (15, "+", "", "Years Experience", "AWS · Azure · GCP · OCI", CYAN),
    (30, "K+", "K", "Students Trained", "zero to placement-ready", VIOLET),
    (30, "+", "", "Real Projects", "built, deployed, operated", PINK),
    (3, "", "", "Clouds + AI & FDE", "multi-cloud · Gen AI · FDE", GREEN),
]


def metrics() -> str:
    w, h = 1200, 210
    cw, gap, top = 270, 20, 22
    x = (w - (4 * cw + 3 * gap)) // 2
    cards, steps, frame = [], 10, 0.12
    for i, (value, suffix, mid, label, sub, color) in enumerate(METRICS):
        start = 0.3 + i * 0.15
        cx = x + cw / 2
        frames = []
        for s in range(steps + 1):
            n = round(value * s / steps)
            body = f"{n}{suffix}" if s == steps else f"{n}{mid}"
            appear = start + s * frame
            hide = (
                f'<set attributeName="visibility" to="hidden" begin="{appear + frame:.2f}s" fill="freeze"/>'
                if s < steps
                else ""
            )
            frames.append(
                f'<text x="{cx}" y="{top + 92}" font-family="{SANS}" font-size="50" font-weight="800" '
                f'fill="url(#m{i})" text-anchor="middle" visibility="hidden">{body}'
                f'<set attributeName="visibility" to="visible" begin="{appear:.2f}s" fill="freeze"/>{hide}</text>'
            )
        perim = 2 * (cw + 160)
        cards.append(
            f"""<linearGradient id="m{i}" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="{WHITE}"/><stop offset="100%" stop-color="{color}"/>
</linearGradient>
<g class="rise" style="animation-delay:{i * 0.15:.2f}s">
  <rect x="{x}" y="{top}" width="{cw}" height="160" rx="18" fill="url(#panel)" stroke="#ffffff" stroke-opacity="0.12"/>
  <rect x="{x}" y="{top}" width="{cw}" height="160" rx="18" fill="none" stroke="{color}" stroke-width="2"
        stroke-dasharray="90 {perim - 90}" class="orbit" style="animation-delay:{-i * 1.5}s" filter="url(#glow)"/>
  <circle cx="{x + 24}" cy="{top + 24}" r="4" fill="{color}" class="pulse"/>
  {"".join(frames)}
  {text(cx, top + 122, label, 16, WHITE, 600, anchor="middle")}
  {text(cx, top + 143, sub, 12, SLATE, anchor="middle")}
</g>"""
        )
        x += cw + gap
    style = f"""
.rise{{animation:rise .7s cubic-bezier(.2,.7,.2,1) both}}
@keyframes rise{{from{{opacity:0;transform:translateY(16px)}}to{{opacity:1;transform:none}}}}
.orbit{{animation:orbit 6s linear infinite}}@keyframes orbit{{to{{stroke-dashoffset:-{2 * (cw + 160)}}}}}
.pulse{{animation:pulse 2s ease-in-out infinite}}@keyframes pulse{{50%{{opacity:.2}}}}
"""
    defs = "\n".join(c.split("</linearGradient>")[0] + "</linearGradient>" for c in cards)
    body = "\n".join(c.split("</linearGradient>", 1)[1] for c in cards)
    return svg(w, h, "By the numbers: 15+ years experience, 30K+ students trained, 30+ real projects, 3 clouds plus AI and FDE", defs + background(w, h), style, body)


# ---------------------------------------------------------------------- Gen AI

def genai() -> str:
    w, h = 1200, 430
    nw, nh = 196, 70
    top_y, bot_y = 126, 292
    xs = [40, 268, 496, 724]
    ingest = [
        ("Enterprise Data", "docs · wikis · code · tickets", CYAN),
        ("Chunk & Clean", "parse · split · metadata", CYAN),
        ("Embeddings", "Bedrock · OpenAI · HF", VIOLET),
        ("Vector Store", "pgvector · Pinecone · OpenSearch", VIOLET),
    ]
    xs2 = [40, 268, 496, 724, 952]
    query = [
        ("User / App", "question or task", ICE),
        ("Retrieve + Rerank", "hybrid search · top-k", VIOLET),
        ("LLM", "Claude · GPT · Gemini", PINK),
        ("Guardrails + Evals", "PII · grounding · scoring", AMBER),
        ("Answer", "cited · traced · costed", GREEN),
    ]
    nodes = [node(x, top_y, nw, nh, t, s, c) for x, (t, s, c) in zip(xs, ingest)]
    nodes += [node(x, bot_y, nw if i < 4 else 208, nh, t, s, c) for i, (x, (t, s, c)) in enumerate(zip(xs2, query))]
    flows = []
    for i in range(3):
        y = top_y + nh / 2
        flows.append(flow(f"i{i}", f"M{xs[i] + nw} {y} L{xs[i + 1]} {y}", CYAN, 1.6, 2, i * 0.3))
    for i in range(4):
        y = bot_y + nh / 2
        flows.append(flow(f"q{i}", f"M{xs2[i] + nw} {y} L{xs2[i + 1]} {y}", PINK if i else ICE, 1.6, 2, i * 0.3))
    vx = xs[3] + nw / 2
    rx = xs2[1] + nw / 2
    flows.append(
        flow("ctx", f"M{vx} {top_y + nh} C{vx} {top_y + nh + 60} {rx} {bot_y - 60} {rx} {bot_y}", VIOLET, 2.4, 3)
    )
    style = f"""{DASH}
.rise{{animation:rise .7s ease both}}@keyframes rise{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:none}}}}
.idx{{animation:idx 3s ease-in-out infinite}}@keyframes idx{{50%{{opacity:.35}}}}
"""
    body = f"""
{text(40, 48, "GENERATIVE AI", 13, ICE, 700, MONO, extra='letter-spacing="4"')}
{text(40, 74, "Production RAG pipeline — grounded answers from enterprise data", 19, WHITE, 600)}
{text(952 + 208, 48, "LLMOps on Kubernetes", 12, SLATE, 500, MONO, anchor="end")}
{text(952 + 208, 66, "tracing · cost · latency SLOs", 12, SLATE, 500, MONO, anchor="end")}
<rect x="952" y="{top_y}" width="208" height="{nh}" rx="14" fill="none" stroke="{GREEN}" stroke-opacity="0.45" stroke-dasharray="4 6" class="dash"/>
{text(1056, top_y + 32, "Prompt & Context", 14, WHITE, 600, anchor="middle")}
{text(1056, top_y + 52, "versioned · schema outputs", 11.5, SLATE, anchor="middle")}
{text(xs[0], top_y - 12, "INGEST", 11, CYAN, 700, MONO, extra='letter-spacing="3" class="idx"')}
{text(xs2[0], bot_y - 12, "QUERY", 11, PINK, 700, MONO, extra='letter-spacing="3" class="idx"')}
{text((vx + rx) / 2 + 70, (top_y + nh + bot_y) / 2 - 14, "context", 12, VIOLET, 600, MONO, anchor="middle")}
{"".join(flows)}
<g class="rise">{"".join(nodes)}</g>
{text(40, 404, "Fine-tuning (LoRA / PEFT) · self-hosted vLLM & Ollama · golden datasets · LLM-as-judge evals", 12.5, SLATE, 500, MONO)}
"""
    return svg(w, h, "Generative AI: production RAG pipeline from enterprise data through embeddings, vector store, retrieval, LLM, guardrails and evals to a cited answer", background(w, h), style, body)


# --------------------------------------------------------------------- Agentic

def agentic() -> str:
    w, h = 1200, 540
    nw, nh = 196, 70
    style = f"""{DASH}
.think{{transform-box:fill-box;transform-origin:center;animation:think 2.4s ease-in-out infinite}}
@keyframes think{{50%{{transform:scale(1.18);opacity:.25}}}}
.lit{{animation:lit 6s ease-in-out infinite}}@keyframes lit{{0%,100%{{stroke-opacity:.35}}50%{{stroke-opacity:1}}}}
.rise{{animation:rise .7s ease both}}@keyframes rise{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:none}}}}
"""
    mid = 308
    a = (40, mid - nh / 2)
    p = (276, mid - nh / 2)
    m = (512, mid - nh / 2)
    tools = [
        ("Cloud APIs", "AWS · Azure · GCP", CYAN),
        ("Kubernetes", "kubectl · Helm · ArgoCD", CYAN),
        ("Terraform · CI/CD", "plan · pipelines · PRs", VIOLET),
        ("RAG Knowledge", "runbooks · docs · history", PINK),
    ]
    ty = [170, 262, 354, 446]
    tx = 760
    hx, hy = 1004, 214
    ex, ey = 1004, 370
    tw = 176
    parts = [
        node(*a, nw, nh, "Alert / Request", "PagerDuty · Slack · ticket", AMBER),
        node(*p, nw, nh, "Planner Agent", "reason · plan · reflect", VIOLET),
        node(*m, nw - 20, nh, "MCP Tool Router", "scoped, least-privilege", ICE),
        node(hx, hy, tw, nh, "Human Approval", "review the diff & risk", AMBER),
        node(ex, ey, tw, nh, "Execute + Audit", "apply · verify · log", GREEN),
    ]
    for (t, s, c), y in zip(tools, ty):
        parts.append(node(tx, y - nh / 2, 196, nh, t, s, c))
    flows = [
        flow("f0", f"M{a[0] + nw} {mid} L{p[0]} {mid}", AMBER, 1.4, 2),
        flow("f1", f"M{p[0] + nw} {mid} L{m[0]} {mid}", VIOLET, 1.4, 2, 0.4),
    ]
    mr = m[0] + nw - 20
    for i, y in enumerate(ty):
        flows.append(flow(f"t{i}", f"M{mr} {mid} C{mr + 40} {mid} {tx - 40} {y} {tx} {y}", CYAN, 1.8, 1, 0.8 + i * 0.25))
        flows.append(flow(f"h{i}", f"M{tx + 196} {y} C{tx + 220} {y} {hx - 30} {hy + nh / 2} {hx} {hy + nh / 2}", VIOLET, 2.2, 1, 1.6 + i * 0.3))
    flows.append(flow("ok", f"M{hx + tw / 2} {hy + nh} L{ex + tw / 2} {ey}", GREEN, 1.2, 2))
    loop = f"M{hx + tw / 2} {hy} C{hx + tw / 2} 64 {p[0] + nw / 2} 64 {p[0] + nw / 2} {p[1]}"
    flows.append(flow("back", loop, PINK, 4, 2))
    body = f"""
{text(40, 46, "AGENTIC AI", 13, VIOLET, 700, MONO, extra='letter-spacing="4"')}
{text(40, 72, "Autonomous ops loop — agents that plan, call tools, and ask before they act", 19, WHITE, 600)}
<circle class="think" cx="{p[0] + nw - 22}" cy="{p[1] + 22}" r="9" fill="{VIOLET}"/>
{"".join(flows)}
<g class="rise">{"".join(parts)}</g>
<rect class="lit" x="{hx}" y="{hy}" width="{tw}" height="{nh}" rx="14" fill="none" stroke="{AMBER}" stroke-width="2"/>
{text((hx + tw / 2 + p[0] + nw / 2) / 2, 100, "rejected → re-plan with feedback", 12, PINK, 600, MONO, anchor="middle")}
{text(hx + tw / 2 + 8, (hy + nh + ey) / 2 + 4, "approved", 12, GREEN, 600, MONO)}
{text(40, 516, "LangGraph · CrewAI · AutoGen patterns · MCP servers · memory · step-level traces · task-success evals", 12.5, SLATE, 500, MONO)}
"""
    return svg(w, h, "Agentic AI: an alert goes to a planner agent, which calls cloud, Kubernetes, Terraform and RAG tools through an MCP router, then waits for human approval before executing with an audit log; rejected plans loop back to the planner", background(w, h), style, body)


# ------------------------------------------------------------------------- FDE

PHASES = [
    ("Discover", "sit with the team,", "map workflow & KPIs", CYAN),
    ("Prototype", "working demo on", "real data in days", ICE),
    ("Productionise", "IaC · CI/CD · evals", "security review", VIOLET),
    ("Deploy & Operate", "their cloud account,", "observability + cost", PINK),
    ("Enable & Hand Over", "runbooks, training,", "team owns it", GREEN),
]


def fde() -> str:
    w, h = 1200, 300
    y = 140
    xs = [130 + i * 235 for i in range(5)]
    dur = 10
    style = f"""
.prog{{animation:prog {dur}s cubic-bezier(.4,0,.2,1) infinite}}
@keyframes prog{{0%{{transform:scaleX(0)}}85%,100%{{transform:scaleX(1)}}}}
.head{{animation:head {dur}s cubic-bezier(.4,0,.2,1) infinite}}
@keyframes head{{0%{{transform:translateX(0)}}85%,100%{{transform:translateX({xs[-1] - xs[0]}px)}}}}
.rise{{animation:rise .7s ease both}}@keyframes rise{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:none}}}}
"""
    stops = []
    for i, (title, l1, l2, color) in enumerate(PHASES):
        at = round(85 * i / 4)
        style += (
            f".n{i}{{transform-box:fill-box;transform-origin:center;animation:n{i} {dur}s ease infinite}}"
            f"@keyframes n{i}{{0%,{max(at - 1, 0)}%{{fill:{NAVY};transform:scale(1)}}"
            f"{at + 2}%{{fill:{color};transform:scale(1.25)}}{min(at + 8, 99)}%,100%{{fill:{color};transform:scale(1)}}}}\n"
        )
        x = xs[i]
        stops.append(
            f"""<g class="rise" style="animation-delay:{i * 0.12:.2f}s">
  <circle cx="{x}" cy="{y}" r="26" fill="none" stroke="{color}" stroke-opacity="0.35"/>
  <circle class="n{i}" cx="{x}" cy="{y}" r="17" fill="{NAVY}" stroke="{color}" stroke-width="2"/>
  {text(x, y + 5, str(i + 1), 14, WHITE, 700, anchor="middle")}
  {text(x, y + 62, title, 16, WHITE, 600, anchor="middle")}
  {text(x, y + 84, l1, 12.5, SLATE, anchor="middle")}
  {text(x, y + 101, l2, 12.5, SLATE, anchor="middle")}
</g>"""
        )
    body = f"""
{text(40, 46, "FORWARD DEPLOYED ENGINEERING", 13, PINK, 700, MONO, extra='letter-spacing="4"')}
{text(40, 72, "Embedded with your team — from an AI use case to a system running in your cloud", 19, WHITE, 600)}
<rect x="{xs[0]}" y="{y - 2}" width="{xs[-1] - xs[0]}" height="4" rx="2" fill="#ffffff" fill-opacity="0.08"/>
<rect class="prog" x="{xs[0]}" y="{y - 2}" width="{xs[-1] - xs[0]}" height="4" rx="2" fill="url(#brand)" style="transform-origin:{xs[0]}px {y}px"/>
<g class="head"><circle cx="{xs[0]}" cy="{y}" r="7" fill="{WHITE}" filter="url(#glow)"/></g>
{"".join(stops)}
"""
    return svg(w, h, "Forward deployed engineering journey: discover, prototype, productionise, deploy and operate, enable and hand over", background(w, h), style, body)


# ------------------------------------------------------------- divider, footer

def divider() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 1200 40" role="img" aria-label="">
<style>.sweep{{animation:sweep 4s ease-in-out infinite}}@keyframes sweep{{from{{transform:translateX(-300px)}}to{{transform:translateX(1200px)}}}}
.pulse{{transform-box:fill-box;transform-origin:center;animation:pulse 2s ease-in-out infinite}}@keyframes pulse{{50%{{transform:scale(1.6);opacity:.5}}}}{REDUCED}</style>
<defs>
<linearGradient id="line" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="{CYAN}" stop-opacity="0"/><stop offset="20%" stop-color="{CYAN}" stop-opacity="0.45"/>
  <stop offset="50%" stop-color="{VIOLET}" stop-opacity="0.65"/><stop offset="80%" stop-color="{PINK}" stop-opacity="0.45"/>
  <stop offset="100%" stop-color="{PINK}" stop-opacity="0"/>
</linearGradient>
<linearGradient id="spark" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%" stop-color="#ffffff" stop-opacity="0"/><stop offset="50%" stop-color="#ffffff" stop-opacity="0.95"/><stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
</linearGradient>
{GLOW}
</defs>
<rect x="0" y="19" width="1200" height="2" fill="url(#line)"/>
<rect class="sweep" x="0" y="18" width="300" height="4" rx="2" fill="url(#spark)" filter="url(#glow)"/>
<circle class="pulse" cx="600" cy="20" r="4" fill="#e0f2fe" filter="url(#glow)"/>
</svg>
"""


def footer() -> str:
    w, h = 1200, 200

    def wave(amp, y, length):
        d = f"M0 {y}"
        x = 0
        while x < w * 2 + length:
            d += f" q{length / 4} {-amp} {length / 2} 0 t{length / 2} 0"
            x += length
        return d + f" V{h} H0 Z"

    style = f"""
.w1{{animation:wave 14s linear infinite}}.w2{{animation:wave 9s linear infinite reverse}}.w3{{animation:wave 20s linear infinite}}
@keyframes wave{{to{{transform:translateX(-400px)}}}}
.rise{{animation:rise 1s ease both}}@keyframes rise{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:none}}}}
"""
    body = f"""
<g class="rise">
{text(w / 2, 70, "“The best way to learn multi-cloud DevOps and AI is to build real systems — not memorise commands.”", 17, WHITE, 500, anchor="middle", extra='font-style="italic"')}
{text(w / 2, 100, "VEERABABU NARNI  ·  CLOUD DEVOPS & AI FORWARD DEPLOYED ENGINEER", 12, ICE, 600, MONO, anchor="middle", extra='letter-spacing="2"')}
</g>
<path class="w3" d="{wave(10, 150, 400)}" fill="{PINK}" fill-opacity="0.10"/>
<path class="w1" d="{wave(14, 160, 400)}" fill="{VIOLET}" fill-opacity="0.16"/>
<path class="w2" d="{wave(10, 172, 400)}" fill="{CYAN}" fill-opacity="0.18"/>
"""
    return svg(w, h, "Footer: the best way to learn multi-cloud DevOps and AI is to build real systems", background(w, h), style, body)


def main() -> int:
    os.makedirs(OUT_DIR, exist_ok=True)
    outputs = {
        "hero.svg": hero(),
        "metrics.svg": metrics(),
        "genai-rag.svg": genai(),
        "agentic-loop.svg": agentic(),
        "fde-journey.svg": fde(),
        "divider.svg": divider(),
        "footer.svg": footer(),
    }
    for name, content in outputs.items():
        path = os.path.join(OUT_DIR, name)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(content)
        print(f"wrote {path} ({len(content.encode()):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
