#!/usr/bin/env python3
"""Malt die Wortbilder für Lisis Wörterwelt über Codex (ChatGPT-Abo), nach dem Vorbild von bilder.py.

Aufruf (im Ordner dieses Skripts, auf dem Mac mit der ChatGPT-App):
  python3 woerter-bilder.py                 alle fehlenden Bögen malen
  python3 woerter-bilder.py --max 5         höchstens 5 Bögen malen und dann aufhören (Nutzungslimit schonen)
  python3 woerter-bilder.py --thema tiere   nur ein Thema
  python3 woerter-bilder.py --liste         nur anzeigen, was schon da ist und was noch fehlt
  python3 woerter-bilder.py --einzeln tiere-hund    ein einzelnes Wort allein neu malen (falls es auf dem Bogen missraten ist)

Um Aufrufe zu sparen, malt Codex pro Aufruf einen Bogen mit bis zu 9 Wörtern (3 × 3) eines Themas.
Die Bögen landen in bilder-gemalt/boegen/, Einzelbilder in bilder-gemalt/einzeln/.
Der erste fertige Bogen dient allen weiteren als Stilvorlage, damit alle Bilder gleich aussehen.
Schon vorhandene Bilder werden übersprungen: Bricht das Skript ab (z. B. Nutzungslimit erreicht),
einfach später erneut starten. Zerschnitten und ins Spiel eingebaut werden die Bögen danach von Claude.
Was gemalt wird, steht in woerter-bilder.json (englische Motivbeschreibung pro Wort).
"""
import argparse
import json
import os
import pathlib
import subprocess
import sys

BASIS = pathlib.Path(__file__).resolve().parent
CODEX = os.environ.get("CODEX", "/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex")
ZIEL = BASIS / "bilder-gemalt"
BOEGEN = ZIEL / "boegen"
EINZELN = ZIEL / "einzeln"
PRO_BOGEN = 9

STIL = ("Realistic hand-painted illustration for a German children's picture dictionary (age 5 to 8). "
        "True-to-life shapes, proportions and colors, painted in soft watercolor and gouache with fine pencil outlines "
        "and a gentle paper texture, like a high-quality classic picture book. Warm soft daylight from the upper left. "
        "Plain light cream background (#fff8ec) with no scenery unless the subject itself is a place. "
        "Friendly and inviting, nothing scary. Objects, food and vehicles have no faces. "
        "Each subject is shown alone, complete, not cut off, and clearly recognizable from its most typical side. "
        "No text, no letters, no numbers, no labels, no frames, no borders, no grid lines.")


def bogen_liste(daten):
    """Teilt jedes Thema in Bögen zu höchstens 9 Wörtern, möglichst gleich groß."""
    boegen = []
    for thema in daten["themen"]:
        w = thema["woerter"]
        anzahl = -(-len(w) // PRO_BOGEN)
        groesse = -(-len(w) // anzahl)
        for i in range(anzahl):
            boegen.append({"name": f"{thema['id']}-{i + 1}", "thema": thema["id"], "woerter": w[i * groesse:(i + 1) * groesse]})
    return boegen


def codex(ordner, dateiname, auftrag, vorlage=None):
    """Ruft Codex für genau ein Bild auf und wandelt es in JPG um. Gibt True zurück, wenn das JPG danach existiert."""
    png = ordner / f"{dateiname}.png"
    jpg = ordner / f"{dateiname}.jpg"
    text = (f"Generate exactly ONE image with your image generation tool, then copy the resulting PNG "
            f"into the current working directory as '{png.name}' and reply only with its file path. "
            f"Do not do anything else.\n\n" + auftrag)
    befehl = [CODEX, "exec", "--skip-git-repo-check", "-s", "workspace-write", "-C", str(ordner), "--color", "never"]
    if vorlage:
        befehl += ["-i", str(vorlage)]
    befehl.append("-")  # Auftrag über stdin, sonst hält "-i" ihn für eine weitere Bilddatei
    try:
        lauf = subprocess.run(befehl, cwd=ordner, input=text, text=True, capture_output=True, timeout=900)
        if not png.exists():
            print("   " + "\n   ".join((lauf.stdout + lauf.stderr).strip().splitlines()[-6:]))
    except subprocess.TimeoutExpired:
        print(f"   ⚠️  {dateiname}: Zeitüberschreitung")
    if not png.exists():
        return False
    subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "90", str(png), "--out", str(jpg)],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if jpg.exists():
        png.unlink()
    return jpg.exists()


def vorlage_text(vorlage):
    if not vorlage:
        return ""
    return ("The attached image is the approved first sheet of this picture dictionary. Paint in exactly the same style: "
            "same painting technique, palette, lighting, cream background color, line quality and scale of the subjects. "
            "Do not copy its subjects.\n\n")


def male_bogen(bogen, vorlage):
    zellen = [f"{i + 1}. {w['motiv']}" for i, w in enumerate(bogen["woerter"])]
    zellen += [f"{i + 1}. (empty: leave this cell plain cream background)" for i in range(len(zellen), PRO_BOGEN)]
    auftrag = (f"Image (square, 1024x1024): {STIL}\n\n" + vorlage_text(vorlage) +
               "Layout: a picture-dictionary sheet with exactly nine cells in an even 3x3 grid (three rows, three columns), "
               "each cell exactly one third of the width and one third of the height. Each subject sits centered in its own cell, "
               "fully inside it, filling about 70 percent of the cell, with plain cream background around it so the subjects "
               "never touch or overlap. No lines between the cells.\n\n"
               "Cells, row by row from top left to bottom right:\n" + "\n".join(zellen))
    return codex(BOEGEN, bogen["name"], auftrag, vorlage)


def male_einzeln(wort, vorlage):
    auftrag = (f"Image (square, 1024x1024): {STIL}\n\n" + vorlage_text(vorlage) +
               f"One single subject, centered, filling about 70 percent of the image: {wort['motiv']}")
    return codex(EINZELN, wort["id"], auftrag, vorlage)


def main():
    p = argparse.ArgumentParser(description="Malt die Wortbilder für Lisis Wörterwelt über Codex.")
    p.add_argument("--max", type=int, help="höchstens so viele Bilder in diesem Lauf malen")
    p.add_argument("--thema", help="nur dieses Thema (z. B. tiere)")
    p.add_argument("--einzeln", nargs="+", metavar="WORT-ID", help="diese Wörter einzeln neu malen (z. B. tiere-hund)")
    p.add_argument("--liste", action="store_true", help="nur anzeigen, was fertig ist und was fehlt")
    a = p.parse_args()

    if not pathlib.Path(CODEX).exists() and not a.liste:
        sys.exit(f"Codex nicht gefunden: {CODEX}\nIst die ChatGPT-App installiert?")
    daten = json.loads((BASIS / "woerter-bilder.json").read_text(encoding="utf-8"))
    BOEGEN.mkdir(parents=True, exist_ok=True)
    EINZELN.mkdir(parents=True, exist_ok=True)
    boegen = bogen_liste(daten)
    fertig = lambda b: (BOEGEN / f"{b['name']}.jpg").exists()
    erster = next((BOEGEN / f"{b['name']}.jpg" for b in boegen if fertig(b)), None)

    if a.liste:
        for b in boegen:
            print(f"{'✅' if fertig(b) else '⬜'} {b['name']:<14} " + ", ".join(w["wort"] for w in b["woerter"]))
        print(f"\n{sum(map(fertig, boegen))} von {len(boegen)} Bögen fertig.")
        return

    if a.einzeln:
        alle = {w["id"]: w for t in daten["themen"] for w in t["woerter"]}
        for wid in a.einzeln:
            if wid not in alle:
                print(f"⚠️  Unbekannte Wort-ID: {wid}")
                continue
            print(f"{wid}: wird einzeln gemalt …", flush=True)
            print(f"{wid}: fertig" if male_einzeln(alle[wid], erster) else f"   ⚠️  {wid}: kein Bild erhalten")
        return

    offen = [b for b in boegen if not fertig(b) and (not a.thema or b["thema"] == a.thema)]
    if a.thema and not any(b["thema"] == a.thema for b in boegen):
        sys.exit(f"Unbekanntes Thema: {a.thema}. Mögliche: " + ", ".join(t["id"] for t in daten["themen"]))
    if a.max is not None:
        offen = offen[:a.max]
    print(f"{len(offen)} Bögen werden gemalt (je ca. 1–2 Minuten).")
    fehler = 0
    for b in offen:
        print(f"{b['name']}: wird gemalt … (" + ", ".join(w["wort"] for w in b["woerter"]) + ")", flush=True)
        if male_bogen(b, erster):
            print(f"{b['name']}: fertig")
            erster = erster or BOEGEN / f"{b['name']}.jpg"
            fehler = 0
        else:
            fehler += 1
            print(f"   ⚠️  {b['name']}: kein Bild erhalten. Vielleicht ist das Nutzungslimit erreicht: später erneut starten.")
            if fehler >= 2:
                print("Zweimal hintereinander kein Bild – ich höre auf. Später einfach erneut starten.")
                break
    gesamt = sum(map(fertig, boegen))
    print(f"\n{gesamt} von {len(boegen)} Bögen fertig.")
    sys.exit(0 if gesamt == len(boegen) else 1)


if __name__ == "__main__":
    main()
