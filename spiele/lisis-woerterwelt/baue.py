"""Baut lisis-woerterwelt.html (Deutsch) lisis-word-world.html (Englisch) und le-monde-des-mots.html (Französisch) aus quelle.html.

Alle {{pfad}}-Platzhalter (Bilder aus marke/, Schriften aus schriften/) werden als data:-URI eingebettet,
damit das Spiel als einzelne Datei überall läuft: offline, auf dem Tablet, in der Nextcloud.
Aufruf: python3 baue.py
"""
import base64, json, mimetypes, pathlib, re

hier = pathlib.Path(__file__).parent
quelle = (hier / "quelle.html").read_text(encoding="utf-8")
typen = {".woff2": "font/woff2", ".png": "image/png", ".jpg": "image/jpeg"}

def einbetten(m):
    datei = hier / m.group(1)
    typ = typen.get(datei.suffix) or mimetypes.guess_type(datei.name)[0]
    return f"data:{typ};base64," + base64.b64encode(datei.read_bytes()).decode()

# Wortbilder (bilder/<codepunkte>.webp) als Tabelle Emoji -> data:-URI
def codepunkte(e): return "-".join(f"{ord(c):04x}" for c in e if ord(c) != 0xFE0F)
emojis = {e for e in re.findall(r"'([^\x00-\x7F]{1,12})'", quelle) if not re.search(r"[A-Za-zÄÖÜäöüß●]", e)}
bilder = {}
for e in sorted(emojis):
    datei = hier / "bilder" / f"{codepunkte(e)}.webp"
    if datei.exists(): bilder[e] = "data:image/webp;base64," + base64.b64encode(datei.read_bytes()).decode()
quelle = quelle.replace("/*{{BILDER}}*/{}", json.dumps(bilder, ensure_ascii=False))
# Gemalte Wortbilder (bilder-gemalt/<wort-id>.webp) gehen vor
gemalt = {p.stem: "data:image/webp;base64," + base64.b64encode(p.read_bytes()).decode()
          for p in sorted((hier / "bilder-gemalt").glob("*.webp"))}
quelle = quelle.replace("/*{{GEMALT}}*/{}", json.dumps(gemalt))
html = re.sub(r"\{\{([\w./-]+)\}\}", einbetten, quelle)
# Zwei Sprachen aus derselben Quelle: Deutsch (lisis-woerterwelt.html) und Englisch (lisis-word-world.html)
for sprache, datei, titel in [("de", "lisis-woerterwelt.html", "Lisis Wörterwelt"), ("en", "lisis-word-world.html", "Lisi’s Word World"),
                             ("fr", "le-monde-des-mots.html", "Le monde des mots de Lisi")]:
    text = html.replace("/*SPRACHE*/'de'", f"'{sprache}'").replace("<title>Lisis Wörterwelt</title>", f"<title>{titel}</title>")
    ziel = hier / datei
    ziel.write_text(f"<!doctype html>\n<html lang=\"{sprache}\">\n" + text + "\n</html>\n", encoding="utf-8")
    print(f"OK: {ziel.name} ({ziel.stat().st_size / 1024:.0f} KB, {len(bilder)} 3D-Bilder, {len(gemalt)} gemalte Bilder)")
