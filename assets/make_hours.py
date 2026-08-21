#!/usr/bin/env python3
"""Generate the build-log panel SVGs used in the profile README.

Writes assets/hours-dark.svg and assets/hours-light.svg so the README can
pick one with <picture>. Self-hosted on purpose: no third-party card
service to rate-limit us.

Run:  python assets/make_hours.py
"""

from pathlib import Path

W = 1000
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"

# The real tally, seven months of nights.
CELLS = [
    ("198",     "hours, counted",        "#A371F7"),
    ("60",      "days across 7 months",  "#A371F7"),
    ("48",      "of them past midnight", "#F778BA"),
    ("122",     "libraries learned",     "#2DB7F5"),
    ("277k",    "files &#183; 29k folders",   "#2DB7F5"),
    ("8.4 GB",  "written and shipped",   "#3FB950"),
]

THEMES = {
    "dark":  dict(bg="#0D1117", line="#21262D", text="#E6EDF3",
                  dim="#7D8590", cell="#010409", op="0.14"),
    "light": dict(bg="#FFFFFF", line="#D1D9E0", text="#1F2328",
                  dim="#59636E", cell="#F6F8FA", op="0.10"),
}

COLS, ROWS = 3, 2
PAD, GAP, TOP = 34, 16, 88
CELL_H = 118


def build(theme):
    t = THEMES[theme]
    cw = (W - PAD * 2 - GAP * (COLS - 1)) / COLS
    height = TOP + ROWS * CELL_H + (ROWS - 1) * GAP + 66

    o = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{height:.0f}" '
        f'viewBox="0 0 {W} {height:.0f}" role="img" '
        f'aria-label="Build log: 198 hours over 60 days across seven months, 48 of them past midnight, '
        f'122 libraries learned, 277 thousand files, 8.4 gigabytes shipped">',
        f'<rect width="{W}" height="{height:.0f}" rx="10" fill="{t["bg"]}" stroke="{t["line"]}"/>',
        f'<text x="{PAD}" y="46" font-family="{MONO}" font-size="15" font-weight="700" '
        f'fill="{t["text"]}" letter-spacing="1.5">BUILD LOG</text>',
        f'<text x="{W-PAD}" y="46" font-family="{MONO}" font-size="12" fill="{t["dim"]}" '
        f'text-anchor="end" letter-spacing="1.2">SEVEN MONTHS &#183; NO TEAM &#183; NO GOOD MACHINE</text>',
        f'<line x1="{PAD}" y1="62" x2="{W-PAD}" y2="62" stroke="{t["line"]}"/>',
    ]

    for i, (num, label, acc) in enumerate(CELLS):
        cx = PAD + (i % COLS) * (cw + GAP)
        cy = TOP + (i // COLS) * (CELL_H + GAP)
        o.append(f'<rect x="{cx:.0f}" y="{cy}" width="{cw:.0f}" height="{CELL_H}" rx="8" '
                 f'fill="{t["cell"]}" stroke="{acc}" stroke-opacity="0.35"/>')
        o.append(f'<rect x="{cx:.0f}" y="{cy}" width="{cw:.0f}" height="{CELL_H}" rx="8" '
                 f'fill="{acc}" fill-opacity="{t["op"]}"/>')
        o.append(f'<text x="{cx+cw/2:.0f}" y="{cy+64}" font-family="{MONO}" font-size="42" '
                 f'font-weight="700" fill="{acc}" text-anchor="middle">{num}</text>')
        o.append(f'<text x="{cx+cw/2:.0f}" y="{cy+92}" font-family="{MONO}" font-size="12.5" '
                 f'fill="{t["dim"]}" text-anchor="middle">{label}</text>')

    fy = height - 26
    o.append(f'<line x1="{PAD}" y1="{fy-24:.0f}" x2="{W-PAD}" y2="{fy-24:.0f}" stroke="{t["line"]}"/>')
    o.append(f'<text x="{PAD}" y="{fy:.0f}" font-family="{MONO}" font-size="11.5" fill="{t["dim"]}">'
             f'a browser that edits video &#183; a viewer that reads scans &#183; a screener for brain recordings '
             f'&#183; a channel that runs itself</text>')
    o.append(f'<text x="{W-PAD}" y="{fy:.0f}" font-family="{MONO}" font-size="11.5" '
             f'fill="{t["dim"]}" text-anchor="end">made with stubbornness</text>')
    o.append('</svg>')
    return "\n".join(o)


if __name__ == "__main__":
    out = Path(__file__).parent
    for theme in THEMES:
        p = out / f"hours-{theme}.svg"
        p.write_text(build(theme), encoding="utf-8")
        print(f"wrote {p.name} ({p.stat().st_size} bytes)")
