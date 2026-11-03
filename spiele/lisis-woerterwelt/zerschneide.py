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

def bereiche(alpha, schritt=4, wachsen=2, schwelle=.5):
    """Zusammenhängende Motive finden (auf verkleinerter Maske, ohne Zusatzbibliotheken).
    Nahe Teile (Regentropfen, Schneeflocken) werden durch leichtes Wachsen verbunden."""
    h, w = alpha.shape
    klein = alpha[:h - h % schritt, :w - w % schritt].reshape(h // schritt, schritt, w // schritt, schritt).max(axis=(1, 3)) > schwelle
    gross = klein.copy()
    for _ in range(wachsen):
        g = gross.copy()
        g[1:] |= gross[:-1]; g[:-1] |= gross[1:]; g[:, 1:] |= gross[:, :-1]; g[:, :-1] |= gross[:, 1:]
        gross = g
    marke = np.zeros(gross.shape, int); n = 0
    for y0, x0 in zip(*np.nonzero(gross)):
        if marke[y0, x0]: continue
        n += 1; stapel = [(y0, x0)]; marke[y0, x0] = n
        while stapel:
            y, x = stapel.pop()
            for yy, xx in ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)):
                if 0 <= yy < gross.shape[0] and 0 <= xx < gross.shape[1] and gross[yy, xx] and not marke[yy, xx]:
                    marke[yy, xx] = n; stapel.append((yy, xx))
    teile = []
    for k in range(1, n + 1):
        ys, xs = np.nonzero((marke == k) & klein)
        if len(xs): teile.append((k, xs.mean() * schritt, ys.mean() * schritt, len(xs)))
    return marke, teile

def main():
    bogen_datei = pathlib.Path(sys.argv[1])
    name = sys.argv[2] if len(sys.argv) > 2 else bogen_datei.stem
    daten = json.loads((hier / "woerter-bilder.json").read_text(encoding="utf-8"))
    bogen = next((b for b in wb.bogen_liste(daten) if b["name"] == name), None)
    if not bogen: sys.exit(f"Unbekannter Bogen: {name}")
    ziel = hier / "bilder-gemalt"; ziel.mkdir(exist_ok=True)
    im = Image.open(bogen_datei).convert("RGB"); W, H = im.size
    frei, alpha = freistellen(im)
    marke, teile = bereiche(alpha)
    schritt = 4
    voll = np.kron(marke, np.ones((schritt, schritt), int))
    voll = np.pad(voll, ((0, H - voll.shape[0]), (0, W - voll.shape[1])))
    kontrolle = Image.new("RGB", (3 * 200, 3 * 230), "white"); d = ImageDraw.Draw(kontrolle)
    for i, wort in enumerate(bogen["woerter"]):
        r, c = divmod(i, 3)
        # alle Teile, deren Mittelpunkt in dieser Zelle liegt (winzige Krümel unter 3 Kästchen werden ignoriert)
        zelle = np.zeros((H, W), bool); zelle[r * H // 3:(r + 1) * H // 3, c * W // 3:(c + 1) * W // 3] = True
        maske = np.zeros((H, W), bool)
        for k, cx, cy, n in teile:
            if n < 3: continue
            teil = voll == k
            anteil = (teil & zelle).sum() / teil.sum()
            if int(cx * 3 // W) == c and int(cy * 3 // H) == r and anteil > .75:
                maske |= teil                      # Motiv gehört fast ganz in diese Zelle: ganz nehmen, auch was über den Rand ragt
            elif anteil > .25:
                maske |= teil & zelle              # zwei Motive hängen zusammen: an der Zellgrenze trennen
        if not maske.any(): print(f"⚠️  {wort['id']}: Zelle {i + 1} ist leer"); continue
        maske &= alpha > 0
        ys, xs = np.nonzero(alpha * maske > .25)
        x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
        if x0 < 3 or y0 < 3 or x1 > W - 4 or y1 > H - 4:
            print(f"⚠️  {wort['id']}: Motiv berührt den Bildrand – evtl. abgeschnitten, bitte prüfen")
        stueck = np.asarray(frei).copy(); stueck[..., 3] = (stueck[..., 3] * maske).astype("uint8")
        stueck = Image.fromarray(stueck).crop((x0, y0, x1 + 1, y1 + 1))
        seite = int(max(x1 - x0, y1 - y0) * 1.08) + 4
        quadrat = Image.new("RGBA", (seite, seite), (0, 0, 0, 0))
        quadrat.paste(stueck, ((seite - stueck.width) // 2, (seite - stueck.height) // 2))
        quadrat = quadrat.resize((GROESSE, GROESSE), Image.LANCZOS)
        quadrat.save(ziel / f"{wort['id']}.webp", "WEBP", quality=82, method=6)
        kachel = Image.new("RGB", (GROESSE, GROESSE), "white"); kachel.paste(quadrat, (0, 0), quadrat)
        kontrolle.paste(kachel.resize((190, 190)), (c * 200 + 5, r * 230 + 5))
        d.text((c * 200 + 8, r * 230 + 200), wort["wort"], fill="black")
    kontrolle.save(ziel / f"kontrolle-{name}.jpg", quality=85)
    print(f"OK: {len(bogen['woerter'])} Bilder aus {name}")

if __name__ == "__main__":
    main()
