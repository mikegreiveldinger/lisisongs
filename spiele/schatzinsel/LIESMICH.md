# Schatzinsel der Zahlen (überarbeitet wie Lunas Regenbogenreise)

`index.html` ist das ganze Spiel (für spiller.lisi.lu unter `/rechenspiele/schatzinsel/`).

Neu gegenüber der bisherigen Fassung:
- **Geschichte:** Ein Sturm hat Ottos Schatzkarte in fünf Stücke gerissen. Kapitänin Lisi und Papagei Kiki holen sie zurück.
  Vorgeschichte, je Gebiet ein Kapitel mit Vor- und Nach-Text, und nach jedem Gebiet ein Kartenstück (wie die Regenbogenfarben).
- **Namensbildschirm** („Wie heißt du?“), Name oben auf dem Bildschirm und im Film.
- **Musik** live erzeugt (Marimba), je Gebiet anders, mit Knopf zum Ausschalten.
- **Hintergründe je Gebiet** (Farbe, Wellen; gemalt, sobald `bilder/<gebiet>.jpg` da ist).
- **Abschlussfilm** in 5 Szenen mit Untertiteln: Karte setzt sich zusammen, Segelfahrt, Otto taucht mit der Kiste auf,
  die Kiste geht auf, Schatzfest mit Feuerwerk und „Bravo, Name!“. Danach jederzeit über „Film ansehen“ auf der Karte.

Der gespeicherte Fortschritt (`schatzinsel-v1`) bleibt erhalten.

Gemalte Bilder: siehe `PROMPTS-CHATGPT.md`. Ohne Bilder zeichnet das Spiel alles selbst.
Veröffentlichen: `index.html` (und ggf. `bilder/`) nach `Webseite/rechenspiele/schatzinsel/` kopieren und mit
`spiller-webseite.py veroeffentlichen` hochladen.
