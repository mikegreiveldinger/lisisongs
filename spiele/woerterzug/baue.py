"""Baut woerterzug.html aus quelle.html und woerter.json.

Alles wird eingebettet (Wortliste, Bilder, Figuren, Schriften), damit das Spiel als einzelne Datei offline läuft.
Gemalte Wortbilder kommen aus ../lisis-woerterwelt/bilder-gemalt, Emoji-Bilder aus bilder/ (siehe hole-bilder.py).
Aufruf: python3 baue.py
"""
import base64, json, mimetypes, pathlib, re

hier = pathlib.Path(__file__).parent
quelle = (hier / "quelle.html").read_text(encoding="utf-8")
daten = json.loads((hier / "woerter.json").read_text(encoding="utf-8"))
typen = {".woff2": "font/woff2", ".png": "image/png", ".jpg": "image/jpeg", ".webp": "image/webp"}

def uri(datei):
    return f"data:{typen.get(datei.suffix) or mimetypes.guess_type(datei.name)[0]};base64," + base64.b64encode(datei.read_bytes()).decode()

# Bilder, die die Wortliste braucht (+ das fallende Herbstblatt in der Landschaft)
schluessel = {e["bild"] for teil in ("silben", "woerter", "saetze", "ueberraschungen") for e in daten[teil]} | {"pflanzen-blatt"}
bilder, fehlt = {}, []
for b in sorted(schluessel):
    if b.isascii():
        datei = hier.parent / "lisis-woerterwelt" / "bilder-gemalt" / f"{b}.webp"
    else:
        datei = hier / "bilder" / ("-".join(f"{ord(c):04x}" for c in b if ord(c) != 0xFE0F) + ".webp")
    if datei.exists(): bilder[b] = uri(datei)
    else: fehlt.append(b)
if fehlt:
    print("⚠️  Bilder fehlen (dort erscheint das Emoji):", " ".join(fehlt))

daten_ohne_hinweis = {k: v for k, v in daten.items() if k != "hinweis"}
html = quelle.replace("/*{{DATEN}}*/{}", json.dumps(daten_ohne_hinweis, ensure_ascii=False))
html = html.replace("/*{{BILDER}}*/{}", json.dumps(bilder))
html = re.sub(r"\{\{([\w./-]+)\}\}", lambda m: uri((hier / m.group(1)).resolve()), html)
ziel = hier / "woerterzug.html"
ziel.write_text("<!doctype html>\n<html lang=\"de\">\n" + html + "\n</html>\n", encoding="utf-8")
print(f"OK: {ziel.name} ({ziel.stat().st_size / 1024:.0f} KB, {len(bilder)} Bilder, "
      f"{len(daten['silben'])} Silbenwörter, {len(daten['woerter'])} Wörter, {len(daten['saetze'])} Sätze)")
