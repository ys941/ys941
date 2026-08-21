#!/usr/bin/env python3
"""Generate the portfolio map SVGs used at the top of the profile README.

Two themes are written so the README can pick one with <picture>:
    assets/map-dark.svg   assets/map-light.svg

Run:  python assets/make_map.py
"""

from pathlib import Path

W = 1000
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"

LANES = [
    ("CLINICAL AI", "clinical", [
        ("Aura", "universal DICOM workstation"),
        ("EEG Analyzer", "epilepsy screening workbench"),
    ]),
    ("AUTONOMOUS SYSTEMS", "auto", [
        ("InstaPilot", "Instagram + YouTube"),
        ("YouTubePilot", "Shorts channel, unattended"),
        ("CardioFlow", "multi-brand engine"),
        ("WhatsApp AutoPilot", "replies in your voice"),
    ]),
    ("CREATIVE & TOOLS", "creative", [
        ("ReelStudio", "4K editor in the browser"),
        ("Aria", "AI-to-AI robot podcast"),
        ("Grabbit", "paste a link, get the file"),
        ("masstree.in", "microbiology toolkit"),
    ]),
]

STACK = ("Next.js  ·  TypeScript  ·  Python  ·  FastAPI  ·  Postgres  ·  "
         "Prisma  ·  FFmpeg  ·  three.js  ·  Cornerstone.js  ·  MNE")

THEMES = {
    "dark": dict(bg="#0D1117", panel="#010409", line="#21262D",
                 text="#E6EDF3", dim="#7D8590", chip_op="0.16", stroke_op="0.55"),
    "light": dict(bg="#FFFFFF", panel="#F6F8FA", line="#D1D9E0",
                  text="#1F2328", dim="#59636E", chip_op="0.12", stroke_op="0.45"),
}

ACCENT = {"clinical": "#2DB7F5", "auto": "#A371F7", "creative": "#F778BA"}

# monospace advance width at a given font size
ADV = 0.60


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def build(theme):
    t = THEMES[theme]
    o = []
    a = o.append

    lane_h, pad_top = 104, 96
    height = pad_top + lane_h * len(LANES) + 74

    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height}" '
      f'viewBox="0 0 {W} {height}" role="img" '
      f'aria-label="Portfolio map: ten projects across clinical AI, autonomous systems and creative tools">')
    a(f'<rect width="{W}" height="{height}" rx="10" fill="{t["bg"]}" stroke="{t["line"]}"/>')

    # ---- header ----
    a(f'<text x="34" y="46" font-family="{MONO}" font-size="15" font-weight="700" '
      f'fill="{t["text"]}" letter-spacing="1.5">YS941 / PORTFOLIO</text>')
    a(f'<text x="{W-34}" y="46" font-family="{MONO}" font-size="12" fill="{t["dim"]}" '
      f'text-anchor="end" letter-spacing="1.2">10 PROJECTS &#183; 3 DOMAINS &#183; SHIPPED SOLO</text>')
    a(f'<line x1="34" y1="66" x2="{W-34}" y2="66" stroke="{t["line"]}"/>')

    # ---- lanes ----
    y = pad_top
    for label, key, items in LANES:
        acc = ACCENT[key]
        a(f'<rect x="34" y="{y-16}" width="3" height="54" rx="1.5" fill="{acc}"/>')
        a(f'<text x="50" y="{y}" font-family="{MONO}" font-size="12.5" font-weight="700" '
          f'fill="{acc}" letter-spacing="1.3">{esc(label)}</text>')
        a(f'<text x="50" y="{y+22}" font-family="{MONO}" font-size="11" fill="{t["dim"]}">'
          f'{len(items)} shipped</text>')

        x = 250
        row_y = y - 22
        for name, desc in items:
            fs_n, fs_d = 13.5, 10.5
            w = max(len(name) * fs_n * ADV, len(desc) * fs_d * ADV) + 30
            if x + w > W - 34:                      # wrap to a second row
                x, row_y = 250, row_y + 46
            a(f'<rect x="{x}" y="{row_y}" width="{w:.0f}" height="40" rx="7" '
              f'fill="{acc}" fill-opacity="{t["chip_op"]}" '
              f'stroke="{acc}" stroke-opacity="{t["stroke_op"]}"/>')
            a(f'<text x="{x+15}" y="{row_y+17}" font-family="{MONO}" font-size="{fs_n}" '
              f'font-weight="600" fill="{t["text"]}">{esc(name)}</text>')
            a(f'<text x="{x+15}" y="{row_y+31}" font-family="{MONO}" font-size="{fs_d}" '
              f'fill="{t["dim"]}">{esc(desc)}</text>')
            x += w + 12
        y += lane_h

    # ---- footer ----
    fy = height - 42
    a(f'<line x1="34" y1="{fy-22}" x2="{W-34}" y2="{fy-22}" stroke="{t["line"]}"/>')
    a(f'<text x="34" y="{fy}" font-family="{MONO}" font-size="11" fill="{t["dim"]}" '
      f'letter-spacing="0.4">{esc(STACK)}</text>')
    a(f'<text x="{W-34}" y="{fy}" font-family="{MONO}" font-size="11" fill="{t["dim"]}" '
      f'text-anchor="end">built at the bench &#9749;</text>')

    a('</svg>')
    return "\n".join(o)


if __name__ == "__main__":
    out = Path(__file__).parent
    for theme in THEMES:
        p = out / f"map-{theme}.svg"
        p.write_text(build(theme), encoding="utf-8")
        print(f"wrote {p.name} ({p.stat().st_size} bytes)")
