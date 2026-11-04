"""Bereitet die Geräusche für Wörterwelt und Wörterzug auf.

Rohdateien (mp3, wav, ogg, m4a … von Pixabay, Freesound o. ä.) kommen nach klaenge/roh/ und heißen wie unten
(z. B. roh/pfiff.mp3). Das Skript schneidet Stille am Anfang und Ende ab, kürzt auf die Höchstlänge, blendet aus,
gleicht die Lautstärke an und speichert eine kleine Datei klaenge/<name>.mp3 (mono, 64 kbit/s).
Danach in lisis-woerterwelt/ und woerterzug/ jeweils python3 baue.py ausführen – die Geräusche werden eingebettet.
Fehlt ein Geräusch, spielt das Spiel an dieser Stelle das bisherige Piepsen.
Aufruf: python3 aufbereiten.py
"""
import pathlib, subprocess, sys

hier = pathlib.Path(__file__).parent
# Name: (Höchstlänge in Sekunden, Ziel-Lautheit in LUFS, wofür)
KLAENGE = {
    "pfiff":     (2.5, -16, "Lok pfeift beim Start eines Bahnhofs"),
    "tschu":     (2.5, -18, "Zug fährt an, neuer Waggon"),
    "ankoppeln": (1.0, -18, "Waggon wird angehängt"),
    "klick":     (0.4, -20, "Kärtchen / Buchstabe abgelegt, Karte umgedreht"),
    "richtig":   (1.2, -18, "Antwort richtig"),
    "nochmal":   (0.8, -22, "sanfter Hinweis bei Fehler"),
    "jubel":     (3.5, -16, "Überraschung / Siegersequenz"),
    "geschenk":  (1.5, -18, "Geschenk geht auf"),
    "trost":     (2.5, -20, "Trostsequenz (Wörterwelt)"),
}

# Bei langen Aufnahmen: ab welcher Sekunde der passende Abschnitt beginnt
AB = {"tschu": 27.6, "klick": 0.33}

def main():
    gemacht = 0
    for name, (laenge, lufs, wofuer) in KLAENGE.items():
        quellen = [p for p in (hier / "roh").glob(f"{name}.*")]
        if not quellen:
            print(f"–  {name:10} fehlt ({wofuer})"); continue
        q, ziel = quellen[0], hier / f"{name}.mp3"
        ab = AB.get(name, 0)
        filter_ = (f"atrim=start={ab},asetpts=PTS-STARTPTS,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.02,"
                   f"areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,areverse,"
                   f"atrim=0:{laenge},afade=t=out:st={max(0, laenge - 0.25)}:d=0.25,"
                   f"loudnorm=I={lufs}:TP=-1.5:LRA=11")
        lauf = subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(q), "-af", filter_, "-ac", "1", "-ar", "32000",
                               "-b:a", "64k", str(ziel)], capture_output=True, text=True)
        if lauf.returncode:
            print(f"⚠️  {name}: {lauf.stderr.strip()[-200:]}"); continue
        dauer = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(ziel)],
                               capture_output=True, text=True).stdout.strip()
        print(f"✓  {name:10} {float(dauer):.1f} s, {ziel.stat().st_size // 1024} KB  ({wofuer})"); gemacht += 1
    print(f"\n{gemacht} von {len(KLAENGE)} Geräuschen fertig.")

if __name__ == "__main__":
    main()
