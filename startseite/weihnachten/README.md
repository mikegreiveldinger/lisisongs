# Weihnachtlicher Look für lisi.lu – Entwurf vom 25.11.2026

Grundlage ist die echte Online-Seite vom 25.11.2026 (`index-live-2026-11-25.html`, unverändert gesichert).
Die Ordnerstruktur entspricht der Webseite: `index.html`, `stil.css`, `weihnachten.css`, `bilder/`, `schriften/`.

## Was sich gegenüber der Online-Seite ändert

- **Logo:** `bilder/lisis-world-weihnachten.png` (Lisi mit Weihnachtsmütze, Schriftzug unverändert).
- **Favicon/App-Symbol:** `bilder/favicon-weihnachten-32.png`, `-192.png`, `apple-touch-icon-weihnachten.png`.
  Die bisherigen Dateien bleiben liegen, damit man nach den Feiertagen einfach zurückstellen kann.
- **weihnachten.css** (neu): Lichterkette unter dem Regenbogenstreifen, leise Sterne im Hintergrund,
  Banner mit kühlerem Himmel und Schneedecke, Schneehauben auf den Kacheln.
- **Schneefall** über der Seite (Skript unten in `index.html`, aus bei „Bewegung reduzieren“).
- **Spruch:** vom 1. bis 26. Dezember ein Countdown bis Heiligabend statt des Spruchs des Tages.
- **Kinder-News-Kachel** aus PR #4 übernommen (rechts neben „Bücher“, auf dem Handy vierte Kachel).
- Fußzeile: E-Mail als normaler `mailto:`-Link (Cloudflare verschlüsselt sie beim Ausliefern selbst).

## Noch offen

- **Banner-Bild:** zeigt noch die Sommerwiese. Ein Winterbild mit den Kindern und Flocke muss neu
  gemalt werden (ChatGPT, Aquarell-Kinderbuchstil). Wie Flocke aussieht, war in Repo, stories.lisi.lu
  und spiller.lisi.lu nicht zu finden.

## Rückbau nach den Feiertagen

`<link rel="stylesheet" href="/weihnachten.css">`, `.lichterkette`, `canvas.schnee`, `.schneedecke` und das Skript
„Weihnachten“ entfernen, Logo und Favicon-Links zurück auf die alten Dateien.
