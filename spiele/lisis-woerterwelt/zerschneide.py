"""Schneidet gemalte Wortbögen (3 × 3) in Einzelbilder für das Spiel.

Aufruf: python3 zerschneide.py <bogen.png|jpg> [<bogen-name>]
Der Bogen-Name (z. B. tiere-1) bestimmt anhand von woerter-bilder.json, welches Wort in welcher Zelle steht.
Ohne Namen wird der Dateiname genommen. Ergebnis: bilder-gemalt/<wort-id>.webp (256 px, Hintergrund durchsichtig)
und eine Kontrollübersicht bilder-gemalt/kontrolle-<bogen-name>.jpg.
"""
import importlib.util, json, pathlib, sys
from PIL import Image, ImageDraw, ImageFilter
import numpy as np

hier = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("wb", hier / "woerter-bilder.py")
wb = importlib.util.module_from_spec(spec); spec.loader.exec_module(wb)
GROESSE = 256

def freistellen(rgb):
    """Papierfarbe -> durchsichtig, mit weichem Übergang, damit Schatten und Pinselkanten sanft auslaufen."""
    a = np.asarray(rgb).astype(float)
    rand = np.concatenate([a[:6].reshape(-1, 3), a[-6:].reshape(-1, 3), a[:, :6].reshape(-1, 3), a[:, -6:].reshape(-1, 3)])
    papier = np.median(rand, axis=0)
    abstand = np.sqrt(((a - papier) ** 2).sum(axis=2))
    alpha = np.clip((abstand - 10) / 28, 0, 1)
    maske = Image.fromarray((alpha * 255).astype("uint8")).filter(ImageFilter.GaussianBlur(.6))
    out = rgb.convert("RGBA"); out.putalpha(maske)
    return out, alpha

def main():
    bogen_datei = pathlib.Path(sys.argv[1])
    name = sys.argv[2] if len(sys.argv) > 2 else bogen_datei.stem
    daten = json.loads((hier / "woerter-bilder.json").read_text(encoding="utf-8"))
    bogen = next((b for b in wb.bogen_liste(daten) if b["name"] == name), None)
    if not bogen: sys.exit(f"Unbekannter Bogen: {name}")
    ziel = hier / "bilder-gemalt"; ziel.mkdir(exist_ok=True)
    im = Image.open(bogen_datei).convert("RGB"); W, H = im.size
    kontrolle = Image.new("RGB", (3 * 200, 3 * 230), "white"); d = ImageDraw.Draw(kontrolle)
    for i, wort in enumerate(bogen["woerter"]):
        r, c = divmod(i, 3)
        zelle = im.crop((c * W // 3, r * H // 3, (c + 1) * W // 3, (r + 1) * H // 3))
        frei, alpha = freistellen(zelle)
        ys, xs = np.where(alpha > .25)
        if not len(xs): print(f"⚠️  {wort['id']}: Zelle {i + 1} ist leer"); continue
        x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
        rand_ber = [x0 < 3, y0 < 3, x1 > zelle.width - 4, y1 > zelle.height - 4]
        if any(rand_ber): print(f"⚠️  {wort['id']}: Motiv berührt den Zellenrand – evtl. abgeschnitten, bitte prüfen")
        seite = int(max(x1 - x0, y1 - y0) * 1.08) + 4
        cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
        quadrat = Image.new("RGBA", (seite, seite), (0, 0, 0, 0))
        quadrat.paste(frei.crop((x0, y0, x1 + 1, y1 + 1)), (seite // 2 - (cx - x0), seite // 2 - (cy - y0)))
        quadrat = quadrat.resize((GROESSE, GROESSE), Image.LANCZOS)
        quadrat.save(ziel / f"{wort['id']}.webp", "WEBP", quality=82, method=6)
        kachel = Image.new("RGB", (GROESSE, GROESSE), "white"); kachel.paste(quadrat, (0, 0), quadrat)
        kontrolle.paste(kachel.resize((190, 190)), (c * 200 + 5, r * 230 + 5))
        d.text((c * 200 + 8, r * 230 + 200), wort["wort"], fill="black")
    kontrolle.save(ziel / f"kontrolle-{name}.jpg", quality=85)
    print(f"OK: {len(bogen['woerter'])} Bilder aus {name}")

if __name__ == "__main__":
    main()
