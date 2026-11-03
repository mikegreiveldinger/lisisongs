"""Baut lisis-woerterwelt.html aus quelle.html.

Alle {{pfad}}-Platzhalter (Bilder aus marke/, Schriften aus schriften/) werden als data:-URI eingebettet,
damit das Spiel als einzelne Datei überall läuft: offline, auf dem Tablet, in der Nextcloud.
Aufruf: python3 baue.py
"""
import base64, mimetypes, pathlib, re

hier = pathlib.Path(__file__).parent
quelle = (hier / "quelle.html").read_text(encoding="utf-8")
typen = {".woff2": "font/woff2", ".png": "image/png", ".jpg": "image/jpeg"}

def einbetten(m):
    datei = hier / m.group(1)
    typ = typen.get(datei.suffix) or mimetypes.guess_type(datei.name)[0]
    return f"data:{typ};base64," + base64.b64encode(datei.read_bytes()).decode()

html = re.sub(r"\{\{([\w./-]+)\}\}", einbetten, quelle)
ziel = hier / "lisis-woerterwelt.html"
ziel.write_text("<!doctype html>\n<html lang=\"de\">\n" + html + "\n</html>\n", encoding="utf-8")
print(f"OK: {ziel.name} ({ziel.stat().st_size / 1024:.0f} KB)")
