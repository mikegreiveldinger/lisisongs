"""Holt die Ersatzbilder (Fluent Emoji 3D, MIT-Lizenz), die woerter.json braucht, nach bilder/.
Sie werden nur gezeigt, solange es für ein Wort noch kein gemaltes Bild in bilder-gemalt/ gibt.
Aufruf: python3 hole-bilder.py <ordner-mit-fluent-assets>   (siehe lisis-woerterwelt/hole-bilder.py)"""
import json, pathlib, sys
from PIL import Image
hier = pathlib.Path(__file__).parent
assets = pathlib.Path(sys.argv[1])
daten = json.loads((hier / "woerter.json").read_text(encoding="utf-8"))
emojis = set()
for l in daten["level"]:
    for e in l["eintraege"]:
        for b in (e.get("emoji"), e.get("bild")):
            if b and not b.isascii(): emojis.add(b)
for u in daten["ueberraschungen"]:
    if not u["bild"].isascii(): emojis.add(u["bild"])
name = lambda e: "-".join(f"{ord(c):04x}" for c in e if ord(c) != 0xFE0F)
fehlt = []
for e in sorted(emojis):
    quelle = next((p for p in [assets / f"{'-'.join(f'{ord(c):04x}' for c in e)}.webp", assets / f"{name(e)}.webp"] if p.exists()), None)
    if not quelle: fehlt.append(e); continue
    im = Image.open(quelle).convert("RGBA"); im.thumbnail((256, 256), Image.LANCZOS)
    im.save(hier / "bilder" / f"{name(e)}.webp", "WEBP", quality=88, method=6)
print(f"{len(emojis) - len(fehlt)} Ersatzbilder geholt", "· fehlen: " + " ".join(fehlt) if fehlt else "")
