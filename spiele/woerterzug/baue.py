"""Baut den Wörterzug in drei Sprachen aus quelle.html:
  woerterzug.html          (Deutsch,  Wörter aus woerter.json)
  lisi-word-train.html     (UK English, woerter-en.json)
  le-train-des-mots.html   (Français, woerter-fr.json)

Alles wird eingebettet, damit jedes Spiel als einzelne Datei offline läuft:
- Wortbilder: gemalt (bilder-gemalt/<id>.webp oder ../lisis-woerterwelt/bilder-gemalt/<id>.webp), sonst Ersatzbild (bilder/<emoji>.webp)
- Landschaften: landschaften/land-<nr>.jpg (fürs iPad verkleinert), die Schiene darin wird automatisch gefunden
- Zug: zug/lok.webp und zug/waggon.webp (falls vorhanden, sonst gezeichneter Zug)
Aufruf: python3 baue.py   (nach Änderungen an den englischen/französischen Wörtern vorher: python3 sprachen.py)
"""
import base64, io, json, mimetypes, pathlib, re

from PIL import Image
import numpy as np

hier = pathlib.Path(__file__).parent
ww = hier.parent / "lisis-woerterwelt" / "bilder-gemalt"
quelle = (hier / "quelle.html").read_text(encoding="utf-8")

# Geräusche aus spiele/klaenge/*.mp3 einbetten (siehe klaenge/aufbereiten.py)
_klaenge = {k.stem: "data:audio/mpeg;base64," + base64.b64encode(k.read_bytes()).decode()
            for k in sorted((pathlib.Path(__file__).parent.parent / "klaenge").glob("*.mp3"))}
quelle = quelle.replace("/*{{KLAENGE}}*/{}", json.dumps(_klaenge))
print("Geräusche:", ", ".join(_klaenge) or "keine (Ersatz-Piepsen)")
typen = {".woff2": "font/woff2", ".png": "image/png", ".jpg": "image/jpeg", ".webp": "image/webp"}
uri = lambda d: f"data:{typen.get(d.suffix) or mimetypes.guess_type(d.name)[0]};base64," + base64.b64encode(d.read_bytes()).decode()
emojiname = lambda e: "-".join(f"{ord(c):04x}" for c in e if ord(c) != 0xFE0F)


def schiene(datei):
    """Findet die vordere Schiene in einer gemalten Landschaft (graue, waagrechte Linie im unteren Drittel).
    Gibt den Abstand vom unteren Bildrand im Verhältnis zur Bildbreite zurück, damit der Zug genau darauf steht."""
    im = Image.open(datei).convert("RGB"); w, h = im.size
    a = np.asarray(im).astype(int); zeilen = []
    for y in range(int(h * .6), h):
        r = a[y]; mx = r.max(1); mn = r.min(1)
        if (((mx - mn) < 40) & (mx > 70) & (mx < 215)).mean() > .6: zeilen.append(y)
    y = max(zeilen) if zeilen else int(h * .86)
    while y - 1 in zeilen: y -= 1   # obere Kante der vorderen Schiene
    return round((h - y) / w, 4)


# Landschaften einmal vorbereiten (verkleinert, als WebP) – gelten für alle Sprachen
LAND, SCHIENE = {}, {}
for nr in range(1, 13):
    d = next((hier / "landschaften" / f"land-{nr}.{e}" for e in ("jpg", "webp") if (hier / "landschaften" / f"land-{nr}.{e}").exists()), None)
    if not d: continue
    im = Image.open(d).convert("RGB"); im.thumbnail((1200, 800), Image.LANCZOS)
    puffer = io.BytesIO(); im.save(puffer, "WEBP", quality=74, method=6)
    LAND[nr] = "data:image/webp;base64," + base64.b64encode(puffer.getvalue()).decode()
    SCHIENE[nr] = schiene(d)


def baue(sprache, datenfile, ziel_name, titel):
    daten = json.loads((hier / datenfile).read_text(encoding="utf-8"))
    bilder, fehlt, gemalt = {}, [], 0

    def nimm(schluessel, *kandidaten):
        for d in kandidaten:
            if d.exists(): bilder[schluessel] = uri(d); return True
        return False

    def emoji(e):
        if e and e not in bilder and not nimm(e, hier / "bilder" / f"{emojiname(e)}.webp"): fehlt.append(e)

    def bild(b):
        if not b: return
        if b.isascii():
            if b not in bilder and not nimm(b, hier / "bilder-gemalt" / f"{b}.webp", ww / f"{b}.webp"): fehlt.append(b)
        else: emoji(b)

    for l in daten["level"]:
        for e in l["eintraege"]:
            if "id" in e and (e["id"] in bilder or nimm(e["id"], hier / "bilder-gemalt" / f"{e['id']}.webp", ww / f"{e['id']}.webp")): gemalt += 1
            elif "id" in e: emoji(e.get("emoji")) if e.get("emoji") else fehlt.append(e["id"])
            bild(e.get("bild"))
        if l["nr"] in LAND:
            bilder[f"land-{l['nr']}"] = LAND[l["nr"]]; l["schiene"] = SCHIENE[l["nr"]]
    for u in daten["ueberraschungen"]: bild(u["bild"])
    bild("pflanzen-blatt")
    for teil in ("lok", "waggon"): nimm(teil, hier / "zug" / f"{teil}.webp", hier / "zug" / f"{teil}.png")
    if fehlt: print(f"⚠️  [{sprache}] ohne Bild:", " ".join(sorted(set(fehlt))))

    html = quelle.replace("/*SPRACHE*/'de'", f"'{sprache}'")
    html = html.replace("<title>Lisi und der Wörterzug</title>", f"<title>{titel}</title>")
    html = html.replace("/*{{DATEN}}*/{}", json.dumps({k: v for k, v in daten.items() if k != "hinweis"}, ensure_ascii=False))
    html = html.replace("/*{{BILDER}}*/{}", json.dumps(bilder))
    html = re.sub(r"\{\{([\w./-]+)\}\}", lambda m: uri((hier / m.group(1)).resolve()), html)
    ziel = hier / ziel_name
    ziel.write_text(f"<!doctype html>\n<html lang=\"{sprache}\">\n" + html + "\n</html>\n", encoding="utf-8")
    print(f"OK: {ziel.name} ({ziel.stat().st_size / 1024:.0f} KB) · {gemalt} gemalte Wortbilder · {len(LAND)} Landschaften · "
          f"Zug gemalt: {'ja' if 'lok' in bilder else 'nein'}")


baue("de", "woerter.json", "woerterzug.html", "Lisi und der Wörterzug")
baue("en", "woerter-en.json", "lisi-word-train.html", "Lisi and the Word Train")
baue("fr", "woerter-fr.json", "le-train-des-mots.html", "Lisi et le train des mots")
