#!/usr/bin/env python3
"""Holt und veröffentlicht die Spieleseite https://spiller.lisi.lu (Cloudflare Pages), nach dem Vorbild von veroeffentlichen.py.

Aufruf (im Ordner dieses Skripts, auf dem Mac):
  python3 spiller-webseite.py holen            1. Schritt: aktuelle Seite herunterladen und Cloudflare-Projekt finden
  python3 spiller-webseite.py veroeffentlichen 2. Schritt: den Ordner Webseite/ hochladen (nach Prüfung)

"holen" lädt alle Dateien, die von spiller.lisi.lu aus verlinkt sind (Seiten, Bilder, Spiele), nach Webseite/,
schreibt eine Liste aller gefundenen Adressen nach Webseite/.bestand.txt und sucht mit wrangler das Pages-Projekt,
zu dem spiller.lisi.lu gehört (Webseite/.projekt.txt). Danach kann Claude die Seite in Webseite/ umbauen.

"veroeffentlichen" prüft zuerst, dass jede Datei aus .bestand.txt noch in Webseite/ liegt (sonst wären Links kaputt),
und lädt dann den ganzen Ordner mit wrangler hoch. Achtung: Cloudflare Pages ersetzt dabei die ganze Seite.
Die Anmeldung bei Cloudflare macht wrangler selbst ("wrangler login"); hier steht kein Zugangsschlüssel.
"""
import html.parser
import os
import pathlib
import re
import subprocess
import sys
import urllib.parse
import urllib.request

BASIS = pathlib.Path(__file__).resolve().parent
ORDNER = BASIS / "Webseite"
ADRESSE = os.environ.get("SPILLER_ADRESSE", "https://spiller.lisi.lu")
NODE = pathlib.Path.home() / ".local" / "lisi-node" / "aktuell" / "bin"
WRANGLER = os.environ.get("WRANGLER", str(NODE / "wrangler"))


class Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []
    def handle_starttag(self, tag, attrs):
        for name, wert in attrs:
            if name in ("href", "src", "poster", "data-src") and wert:
                self.links.append(wert)
            if name == "srcset" and wert:
                self.links += [teil.strip().split(" ")[0] for teil in wert.split(",") if teil.strip()]
            if name == "style" and wert:
                self.links += re.findall(r"url\(['\"]?([^'\")]+)", wert)


def lokaler_pfad(url):
    pfad = urllib.parse.urlsplit(url).path or "/"
    if pfad.endswith("/"):
        pfad += "index.html"
    return pathlib.PurePosixPath(urllib.parse.unquote(pfad.lstrip("/")))


def holen():
    host = urllib.parse.urlsplit(ADRESSE).netloc
    if (ORDNER / ".bestand.txt").exists() and "--neu" not in sys.argv:
        sys.exit("Abbruch: Webseite/ gibt es schon (evtl. mit Änderungen von Claude). Neu holen nur mit: holen --neu")
    offen, gesehen, bestand = [ADRESSE + "/"], set(), []
    ORDNER.mkdir(exist_ok=True)
    while offen:
        url = urllib.parse.urldefrag(offen.pop())[0]
        if url in gesehen:
            continue
        gesehen.add(url)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "lisi-spiller-skript"}), timeout=60) as antwort:
                daten, typ, ende = antwort.read(), antwort.headers.get_content_type(), antwort.geturl()
        except Exception as fehler:
            print(f"⚠️  nicht geladen: {url} ({fehler})")
            continue
        if urllib.parse.urlsplit(ende).netloc != host:
            continue
        pfad = lokaler_pfad(ende)
        if typ == "text/html" and pfad.suffix not in (".html", ".htm"):
            pfad = pfad / "index.html"
        ziel = ORDNER / pfad
        ziel.parent.mkdir(parents=True, exist_ok=True)
        ziel.write_bytes(daten)
        bestand.append(str(pfad))
        print(f"✓ {pfad}")
        if typ in ("text/html", "text/css"):
            text = daten.decode("utf-8", "replace")
            if typ == "text/html":
                p = Links(); p.feed(text); funde = p.links
            else:
                funde = re.findall(r"url\(['\"]?([^'\")]+)", text)
            for link in funde:
                if link.startswith(("data:", "mailto:", "tel:", "javascript:", "#")):
                    continue
                voll = urllib.parse.urljoin(ende, link)
                if urllib.parse.urlsplit(voll).netloc == host:
                    offen.append(voll)
    (ORDNER / ".bestand.txt").write_text("\n".join(sorted(set(bestand))) + "\n", encoding="utf-8")
    print(f"\n{len(set(bestand))} Dateien in {ORDNER.name}/ gespeichert.")
    projekt = finde_projekt(host)
    if projekt:
        (ORDNER / ".projekt.txt").write_text(projekt + "\n", encoding="utf-8")
        print(f"Cloudflare-Projekt für {host}: {projekt}")
    print("Fertig. Sag Claude Bescheid, dann wird die Seite umgebaut.")


def finde_projekt(host):
    if not pathlib.Path(WRANGLER).exists():
        print(f"⚠️  wrangler nicht gefunden ({WRANGLER}) – Projektname bitte von Hand in Webseite/.projekt.txt eintragen.")
        return None
    umgebung = dict(os.environ, PATH=f"{NODE}:{os.environ.get('PATH', '')}", WRANGLER_SEND_METRICS="false")
    lauf = subprocess.run([WRANGLER, "pages", "project", "list"], env=umgebung, stdin=subprocess.DEVNULL,
                          capture_output=True, text=True, timeout=300)
    zeilen = [z for z in lauf.stdout.splitlines() if host in z]
    if not zeilen:
        print(f"⚠️  Kein Cloudflare-Pages-Projekt mit der Adresse {host} gefunden.")
        print("   Vielleicht liegt die Seite nicht bei Cloudflare Pages (z. B. Canva) oder die Anmeldung ist abgelaufen")
        print(f"   ('{WRANGLER} login'). Ausgabe von wrangler:\n" + "\n".join((lauf.stdout + lauf.stderr).strip().splitlines()[-15:]))
        return None
    namen = re.findall(r"[│|]\s*([a-z0-9][a-z0-9-]*)\s*[│|]", zeilen[0])
    return namen[0] if namen else None


def veroeffentlichen():
    bestand_datei, projekt_datei = ORDNER / ".bestand.txt", ORDNER / ".projekt.txt"
    if not bestand_datei.exists() or not projekt_datei.exists():
        sys.exit("Abbruch: Zuerst 'python3 spiller-webseite.py holen' ausführen (und ggf. Projektname eintragen).")
    fehlt = [p for p in bestand_datei.read_text(encoding="utf-8").split() if not (ORDNER / p).exists()]
    if fehlt:
        sys.exit("Abbruch: Diese Dateien der bisherigen Seite fehlen in Webseite/ – Links wären danach kaputt:\n  " + "\n  ".join(fehlt))
    projekt = projekt_datei.read_text(encoding="utf-8").strip()
    if not pathlib.Path(WRANGLER).exists():
        sys.exit(f"Abbruch: wrangler fehlt ({WRANGLER}).")
    anzahl = sum(1 for p in ORDNER.rglob("*") if p.is_file() and not p.name.startswith("."))
    print(f"{anzahl} Dateien werden zu '{projekt}' hochgeladen …", flush=True)
    umgebung = dict(os.environ, PATH=f"{NODE}:{os.environ.get('PATH', '')}", WRANGLER_SEND_METRICS="false")
    lauf = subprocess.run([WRANGLER, "pages", "deploy", str(ORDNER), "--project-name", projekt, "--branch", "main",
                           "--commit-dirty=true"], env=umgebung, stdin=subprocess.DEVNULL, capture_output=True, text=True, timeout=900)
    if lauf.returncode != 0:
        print("\n".join((lauf.stdout + lauf.stderr).strip().splitlines()[-12:]))
        sys.exit(f"Upload fehlgeschlagen. Ist die Cloudflare-Anmeldung abgelaufen? Dann '{WRANGLER} login' ausführen.")
    print(f"Veröffentlicht: {ADRESSE}")


if __name__ == "__main__":
    befehl = sys.argv[1] if len(sys.argv) > 1 else ""
    if befehl == "holen":
        holen()
    elif befehl == "veroeffentlichen":
        veroeffentlichen()
    else:
        sys.exit(__doc__)
