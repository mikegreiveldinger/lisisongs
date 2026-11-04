"""Holt die Emoji-Bilder (Fluent Emoji 3D, MIT-Lizenz), die woerter.json braucht, nach bilder/.
Gemalte Bilder werden direkt aus ../lisis-woerterwelt/bilder-gemalt genommen und hier nicht kopiert.
Aufruf: python3 hole-bilder.py <ordner-mit-fluent-assets>   (siehe lisis-woerterwelt/hole-bilder.py)"""
import json, pathlib, sys
from PIL import Image
hier = pathlib.Path(__file__).parent
assets = pathlib.Path(sys.argv[1])
daten = json.loads((hier / "woerter.json").read_text(encoding="utf-8"))
bilder = {e["bild"] for teil in ("silben", "woerter", "saetze", "ueberraschungen") for e in daten[teil]}
emojis = [b for b in bilder if not b.isascii()]
name = lambda e: "-".join(f"{ord(c):04x}" for c in e if ord(c) != 0xFE0F)
fehlt = []
for e in emojis:
    quelle = next((p for p in [assets / f"{'-'.join(f'{ord(c):04x}' for c in e)}.webp", assets / f"{name(e)}.webp"] if p.exists()), None)
    if not quelle: fehlt.append(e); continue
    im = Image.open(quelle).convert("RGBA"); im.thumbnail((256, 256), Image.LANCZOS)
    im.save(hier / "bilder" / f"{name(e)}.webp", "WEBP", quality=88, method=6)
print(f"{len(emojis) - len(fehlt)} Emoji-Bilder geholt", "· fehlen: " + " ".join(fehlt) if fehlt else "")
