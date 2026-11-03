# Gemalte Wortbilder für Lisis Wörterwelt

Das Skript `woerter-bilder.py` malt die Bilder für 159 Wörter über Codex mit dem ChatGPT-Abo, genauso wie `bilder.py` bei der Märchenzeit.
Farben, Zahlen und die Thermometer (heiß, warm, kühl, kalt) bleiben gezeichnet und werden nicht gemalt.

## Damit es dein Nutzungslimit schont

- Pro Aufruf entsteht **ein Bogen mit bis zu 9 Wörtern** (3 × 3). Für alle 159 Wörter sind das nur **22 Bögen** statt 159 Einzelbilder.
- Fertige Bögen werden übersprungen. Bricht das Skript ab, einfach später erneut starten.
- Nach zwei Fehlversuchen hintereinander (meist: Limit erreicht) hört das Skript von selbst auf.

## So geht's

Terminal öffnen, in diesen Ordner wechseln (`cd …/Spiller/Wörterwelt (Claude)`), dann:

1. **Erst einen Probebogen malen:**
   `python3 woerter-bilder.py --max 1`
   Das Ergebnis liegt in `bilder-gemalt/boegen/tiere-1.jpg`. Dieser erste Bogen ist die **Stilvorlage für alle weiteren**.
   Gefällt er dir nicht, lösch ihn und starte nochmal. Gefällt er dir, sag Claude kurz Bescheid oder mach direkt weiter.
2. **Den Rest in Portionen malen**, z. B. 5 Bögen pro Durchgang:
   `python3 woerter-bilder.py --max 5`
   Oder alles auf einmal: `python3 woerter-bilder.py` (ca. 30–45 Minuten).
3. **Stand ansehen:** `python3 woerter-bilder.py --liste`
4. **Ein einzelnes missratenes Wort neu malen:** `python3 woerter-bilder.py --einzeln tiere-hund`
   (Die Wort-IDs zeigt `--liste` nicht an; sie stehen in `woerter-bilder.json`, z. B. `essen-apfel`, `geographie-luxemburg`.)
5. **Nur ein Thema:** `python3 woerter-bilder.py --thema schule`

Danach Claude Bescheid geben. Claude holt `bilder-gemalt/` aus der Nextcloud, schneidet die Bögen in Einzelbilder,
prüft jedes Bild und baut sie ins Spiel ein. Wo noch kein gemaltes Bild da ist, zeigt das Spiel vorerst das 3D-Bild.

## Motive ändern

In `woerter-bilder.json` steht für jedes Wort eine englische Motivbeschreibung (`motiv`). Wer ein Motiv ändern will,
ändert dort den Text und malt danach den Bogen (Bogen-Datei löschen und neu starten) oder das Wort einzeln neu.
