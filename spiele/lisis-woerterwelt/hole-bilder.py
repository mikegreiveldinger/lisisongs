"""Holt die Wortbilder für quelle.html aus dem Fluent-Emoji-3D-Paket (Microsoft, MIT-Lizenz) nach bilder/.

Aufruf: python3 hole-bilder.py <ordner-mit-fluent-assets>
Den Ordner bekommt man mit:  npm pack @lobehub/fluent-emoji-3d  und  tar xzf lobehub-fluent-emoji-3d-*.tgz  (-> package/assets)
Jedes Bild wird auf 160 px verkleinert. Für die Schottland-Flagge (fehlt im Paket) wird die Luxemburg-Flagge
als Form und Schattierung genommen und neu eingefärbt.
"""
import pathlib, re, sys
from PIL import Image

hier = pathlib.Path(__file__).parent
quelle = (hier / "quelle.html").read_text(encoding="utf-8")
assets = pathlib.Path(sys.argv[1])
ziel = hier / "bilder"; ziel.mkdir(exist_ok=True)

def name(e):
    return "-".join(f"{ord(c):04x}" for c in e if ord(c) != 0xFE0F)

def finde(e):
    for n in ["-".join(f"{ord(c):04x}" for c in e), name(e)]:
        p = assets / f"{n}.webp"
        if p.exists(): return p

def speichere(im, e):
    im = im.convert("RGBA"); im.thumbnail((160, 160), Image.LANCZOS)
    im.save(ziel / f"{name(e)}.webp", "WEBP", quality=88, method=6)

SCHOTTLAND = "🏴\U000e0067\U000e0062\U000e0073\U000e0063\U000e0074\U000e007f"
def schottland():
    lu = Image.open(finde("🇱🇺")).convert("RGBA"); w, h = lu.size; px = lu.load()
    out = Image.new("RGBA", (w, h)); po = out.load()
    spalten = {}
    for x in range(w):
        ys = [y for y in range(h) if px[x, y][3] > 128]
        if ys: spalten[x] = (ys[0], ys[-1])
    x0, x1 = min(spalten), max(spalten)
    stripe = [(237, 41, 57), (255, 255, 255), (0, 161, 222)]  # Grundfarben der Luxemburg-Flagge
    for x, (top, bot) in spalten.items():
        for y in range(h):
            r, g, b, a = px[x, y]
            if a == 0: continue
            u = (x - x0) / max(1, x1 - x0); v = min(1, max(0, (y - top) / max(1, bot - top)))
            base = stripe[min(2, int(v * 3))]
            licht = (r + g + b) / max(1, sum(base))  # Schattierung der Welle
            weiss = abs(v - u) < .11 or abs(v - (1 - u)) < .11
            c = (245, 247, 250) if weiss else (0, 94, 184)
            po[x, y] = tuple(min(255, int(k * licht)) for k in c) + (a,)
    return out

emojis = sorted({e for e in re.findall(r"'([^\x00-\x7F]{1,12})'", quelle) if not re.search(r"[A-Za-zÄÖÜäöüß●]", e)})
fehlt = []
for e in emojis:
    if e == SCHOTTLAND: speichere(schottland(), e); continue
    p = finde(e)
    if p: speichere(Image.open(p), e)
    else: fehlt.append(e)
print(f"{len(emojis) - len(fehlt)} Bilder in bilder/", "· fehlen:" if fehlt else "", " ".join(fehlt))
