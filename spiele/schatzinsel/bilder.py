#!/usr/bin/env python3
"""Malt die Bilder für die Schatzinsel der Zahlen über Codex (ChatGPT-Abo), nach dem Vorbild von woerter-bilder.py.

Aufruf (im Ordner dieses Skripts, auf dem Mac mit der ChatGPT-App):
  python3 bilder.py              alle fehlenden Bilder malen (12 Stück, je ca. 1–2 Minuten)
  python3 bilder.py --max 3      höchstens 3 Bilder malen (Nutzungslimit schonen)
  python3 bilder.py --nur film4  nur dieses Bild (neu) malen; vorhandenes vorher löschen
  python3 bilder.py --liste      anzeigen, was fertig ist

Die Bilder landen in bilder/ (JPG, 1600 px breit; das Schiff als PNG mit weißem Hintergrund,
das Freistellen macht Claude). Das erste fertige Bild (muschelbucht) ist die Stilvorlage für alle weiteren.
Wo Lisi vorkommt, bekommt Codex zusätzlich vorlagen/lisi.jpg mit.
Bricht das Skript ab (z. B. Nutzungslimit), einfach später erneut starten: Fertiges wird übersprungen.
"""
import argparse
import os
import pathlib
import subprocess
import sys

BASIS = pathlib.Path(__file__).resolve().parent
CODEX = os.environ.get("CODEX", "/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex")
ZIEL = BASIS / "bilder"
LISI = BASIS / "vorlagen" / "lisi.jpg"

STIL = ("Hand-painted watercolor and gouache illustration for a German children's picture book (age 5 to 8), "
        "warm, friendly and cheerful, soft light, gentle paper texture, like a high-quality classic picture book. "
        "Nothing scary. No text, no letters, no numbers, no labels, no frame, no border.")
FIGUREN = ("Characters (only if the scene asks for them): Lisi, a girl of about seven with light brown hair in a ponytail, "
           "green eyes, freckles, a yellow knitted beanie with a big pompom and a long yellow knitted scarf "
           "(exactly like the girl in the attached portrait), here dressed as a little ship's captain in a yellow raincoat; "
           "Kiki, a small red parrot with green wings and a yellow beak; "
           "Otto, a big friendly orange octopus with large kind eyes, rosy cheeks and a small dark blue captain's hat.")
BREIT = "Wide landscape image, 1536x1024 (3:2)."
RUHIG = "The middle of the picture must stay calm and simple (open water, sand or sky), because a big card is placed there."

BILDER = [
    ("muschelbucht", BREIT, False, "A sunny turquoise bay with a white sandy beach full of colorful seashells, a few friendly red crabs at the left and right edges, gentle waves, a small sailing ship far away on the horizon. No people. " + RUHIG),
    ("palmenstrand", BREIT, False, "A golden beach with tall coconut palms at the left and right edges, coconuts in the palms, two small cheerful monkeys sitting high in one palm, a turquoise lagoon. No people. " + RUHIG),
    ("vulkaninsel", BREIT, False, "A friendly, not scary, green tropical volcano island in warm late-afternoon light, a small white puff of smoke from the volcano, warm dark lava stones with a soft orange glow at the edges, ferns and red flowers. No people. " + RUHIG),
    ("nebelriff", BREIT, False, "A misty blue-grey reef in soft morning fog, a red and white lighthouse on a rock at the right edge with a warm glowing light, a friendly whale spouting water far away on the left. Calm and gentle, not scary. No people. " + RUHIG),
    ("schatzinsel", BREIT, False, "The treasure island in golden afternoon light: a big rock with a compass rose carved into it at the left edge, palms, an old anchor in the sand, glittering water and a few golden sparkles. No people. " + RUHIG),
    ("film1", BREIT, False, "A complete old treasure map on aged parchment that fills the whole picture edge to edge, seen from straight above, flat, no table, no hands. Five small painted islands connected by a dotted red route: an island with pink seashells in the upper left, an island with palms in the upper right, a small green volcano in the lower left, a lighthouse on a rock in the middle, and a palm island in the lower right with a big red X on it. The red X is at about 80 percent from the left and 70 percent from the top. A compass rose in the upper right corner, little painted waves between the islands."),
    ("film2", BREIT, False, "Open sunny sea with gentle waves, a few seagulls and white clouds, a small palm island far away on the horizon on the right. The horizon is a bit above the middle. The lower half is open water with no objects, because a ship will sail there. No ship, no people."),
    ("schiff", "Square image, 1024x1024.", True, "A small friendly wooden sailing ship seen exactly from the side, sailing to the right, white sails, a little red flag, golden details and round portholes. Lisi stands on deck and waves; Kiki the parrot sits on the bow. The whole ship is fully visible and centered, nothing cut off. Plain pure white background, no water, no waves, no shadow."),
    ("film3", BREIT, True, "A sunny tropical beach: Otto the octopus rises out of the turquoise water on the right, holding a big wooden treasure chest with golden bands in his tentacles, water splashing and sparkling. On the sand on the left, Lisi and Kiki look at him in happy surprise."),
    ("film4", BREIT, True, "Close-up on the beach: the open treasure chest in the middle is full of shining gold coins and the most beautiful colorful seashells, warm golden light streams out of it. Lisi jumps for joy on the left, Otto the octopus smiles on the right, Kiki the parrot flies above the chest."),
    ("film5", BREIT, True, "A cheerful beach party at sunset: colorful paper lanterns on a string between the palms, Lisi, Kiki and Otto celebrate next to the open treasure chest. All the friends from the journey join in: red crabs, two little monkeys, a sea turtle, and a whale spouting water in the sea. Pink and orange sky with the first stars. Keep the upper quarter of the sky calm and empty."),
]


def datei(name):
    return ZIEL / (f"{name}.png" if name == "schiff" else f"{name}.jpg")


def codex(name, format_, mit_lisi, motiv, stilvorlage):
    png = ZIEL / f"{name}-roh.png"
    auftrag = (f"Generate exactly ONE image with your image generation tool, then copy the resulting PNG "
               f"into the current working directory as '{png.name}' and reply only with its file path. "
               f"Do not do anything else.\n\nImage: {format_} {STIL}\n\n")
    bilder = []
    if stilvorlage:
        bilder.append(stilvorlage)
        auftrag += ("One attached image is an approved picture from the same game. Paint in exactly the same style: "
                    "same painting technique, palette, lighting and line quality. Do not copy its content.\n\n")
    if mit_lisi:
        bilder.append(LISI)
        auftrag += FIGUREN + "\n\n"
    auftrag += "Scene: " + motiv
    befehl = [CODEX, "exec", "--skip-git-repo-check", "-s", "workspace-write", "-C", str(ZIEL), "--color", "never"]
    for b in bilder:
        befehl += ["-i", str(b)]
    befehl.append("-")
    try:
        lauf = subprocess.run(befehl, cwd=ZIEL, input=auftrag, text=True, capture_output=True, timeout=900)
        if not png.exists():
            print("   " + "\n   ".join((lauf.stdout + lauf.stderr).strip().splitlines()[-6:]))
    except subprocess.TimeoutExpired:
        print(f"   ⚠️  {name}: Zeitüberschreitung")
    if not png.exists():
        return False
    ziel = datei(name)
    if name == "schiff":
        png.rename(ziel)
    else:
        subprocess.run(["sips", "-Z", "1600", "-s", "format", "jpeg", "-s", "formatOptions", "85", str(png), "--out", str(ziel)],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if ziel.exists():
            png.unlink()
    return ziel.exists()


def main():
    p = argparse.ArgumentParser(description="Malt die Bilder für die Schatzinsel der Zahlen über Codex.")
    p.add_argument("--max", type=int, help="höchstens so viele Bilder malen")
    p.add_argument("--nur", nargs="+", metavar="NAME", help="nur diese Bilder malen (z. B. film4)")
    p.add_argument("--liste", action="store_true", help="nur anzeigen, was fertig ist")
    a = p.parse_args()
    ZIEL.mkdir(exist_ok=True)
    if a.liste:
        for name, *_ in BILDER:
            print(f"{'✅' if datei(name).exists() else '⬜'} {name}")
        return
    if not pathlib.Path(CODEX).exists():
        sys.exit(f"Codex nicht gefunden: {CODEX}\nIst die ChatGPT-App installiert?")
    if not LISI.exists():
        sys.exit(f"Lisi-Vorlage fehlt: {LISI}")
    offen = [b for b in BILDER if (a.nur and b[0] in a.nur) or (not a.nur and not datei(b[0]).exists())]
    if a.max is not None:
        offen = offen[:a.max]
    print(f"{len(offen)} Bilder werden gemalt (je ca. 1–2 Minuten).")
    fehler = 0
    for name, format_, mit_lisi, motiv in offen:
        vorlage = datei("muschelbucht") if name != "muschelbucht" and datei("muschelbucht").exists() else None
        print(f"{name}: wird gemalt …", flush=True)
        if codex(name, format_, mit_lisi, motiv, vorlage):
            print(f"{name}: fertig")
            fehler = 0
        else:
            fehler += 1
            print(f"   ⚠️  {name}: kein Bild erhalten. Vielleicht ist das Nutzungslimit erreicht: später erneut starten.")
            if fehler >= 2:
                print("Zweimal hintereinander kein Bild – ich höre auf. Später einfach erneut starten.")
                break
    fertig = sum(datei(n).exists() for n, *_ in BILDER)
    print(f"\n{fertig} von {len(BILDER)} Bildern fertig.")
    sys.exit(0 if fertig == len(BILDER) else 1)


if __name__ == "__main__":
    main()
