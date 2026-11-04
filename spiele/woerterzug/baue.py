"""Baut woerterzug.html aus quelle.html und woerter.json.

Alles wird eingebettet, damit das Spiel als einzelne Datei offline läuft:
- Wortbilder: zuerst gemalt (bilder-gemalt/<id>.webp, aus den Bögen), sonst Ersatzbild (bilder/<emoji>.webp)
- Satzbilder: gemalte Bilder aus ../lisis-woerterwelt/bilder-gemalt oder Ersatzbilder
- Landschaften: landschaften/land-<nr>.jpg (falls vorhanden, sonst zeichnet das Spiel eine Landschaft)
- Zug: zug/lok.webp und zug/waggon.webp (falls vorhanden, sonst gezeichneter Zug); Streckenkarte: zug/karte.jpg
Aufruf: python3 baue.py
"""
import base64, json, mimetypes, pathlib, re

hier = pathlib.Path(__file__).parent
quelle = (hier / "quelle.html").read_text(encoding="utf-8")
daten = json.loads((hier / "woerter.json").read_text(encoding="utf-8"))
typen = {".woff2": "font/woff2", ".png": "image/png", ".jpg": "image/jpeg", ".webp": "image/webp"}
uri = lambda d: f"data:{typen.get(d.suffix) or mimetypes.guess_type(d.name)[0]};base64," + base64.b64encode(d.read_bytes()).decode()
emojiname = lambda e: "-".join(f"{ord(c):04x}" for c in e if ord(c) != 0xFE0F)

bilder, gemalt, fehlt = {}, 0, []
def nimm(schluessel, *kandidaten):
    for d in kandidaten:
        if d.exists(): bilder[schluessel] = uri(d); return True
    return False
def emoji(e):
    if e and e not in bilder and not nimm(e, hier / "bilder" / f"{emojiname(e)}.webp"): fehlt.append(e)
def bild(b):
    if not b: return
    if b.isascii():
        if b not in bilder and not nimm(b, hier / "bilder-gemalt" / f"{b}.webp", hier.parent / "lisis-woerterwelt" / "bilder-gemalt" / f"{b}.webp"): fehlt.append(b)
    else: emoji(b)

for l in daten["level"]:
    for e in l["eintraege"]:
        if "id" in e and nimm(e["id"], hier / "bilder-gemalt" / f"{e['id']}.webp"): gemalt += 1
        emoji(e.get("emoji")); bild(e.get("bild"))
    nimm(f"land-{l['nr']}", hier / "landschaften" / f"land-{l['nr']}.jpg", hier / "landschaften" / f"land-{l['nr']}.webp")
for u in daten["ueberraschungen"]: bild(u["bild"])
bild("pflanzen-blatt")
for teil in ("lok", "waggon"): nimm(teil, hier / "zug" / f"{teil}.webp", hier / "zug" / f"{teil}.png")
nimm("karte", hier / "zug" / "karte.jpg", hier / "zug" / "karte.webp")
if fehlt: print("⚠️  ohne Bild:", " ".join(sorted(set(fehlt))))

html = quelle.replace("/*{{DATEN}}*/{}", json.dumps({k: v for k, v in daten.items() if k != "hinweis"}, ensure_ascii=False))
html = html.replace("/*{{BILDER}}*/{}", json.dumps(bilder))
html = re.sub(r"\{\{([\w./-]+)\}\}", lambda m: uri((hier / m.group(1)).resolve()), html)
ziel = hier / "woerterzug.html"
ziel.write_text("<!doctype html>\n<html lang=\"de\">\n" + html + "\n</html>\n", encoding="utf-8")
landschaften = sum(1 for k in bilder if k.startswith("land-"))
print(f"OK: {ziel.name} ({ziel.stat().st_size / 1024:.0f} KB) · {gemalt} gemalte Wortbilder · {landschaften} Landschaften · "
      f"Zug gemalt: {'ja' if 'lok' in bilder else 'nein'}")
