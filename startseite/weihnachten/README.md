# Weihnachtlicher Look für lisi.lu – Entwurf vom 25.11.2026

Grundlage ist die echte Online-Seite vom 25.11.2026 (`index-live-2026-11-25.html`, unverändert gesichert).
Die Ordnerstruktur entspricht der Webseite: `index.html`, `stil.css`, `weihnachten.css`, `bilder/`, `schriften/`.

## Was sich gegenüber der Online-Seite ändert

- **Logo:** `bilder/lisis-world-weihnachten.png` (Lisi mit Weihnachtsmütze, Schriftzug unverändert).
- **Favicon/App-Symbol:** `bilder/favicon-weihnachten-32.png`, `-192.png`, `apple-touch-icon-weihnachten.png`.
  Die bisherigen Dateien bleiben liegen, damit man nach den Feiertagen einfach zurückstellen kann.
- **Kopfbild:** `bilder/kopfbild-weihnachten.jpg` (+ `-klein.jpg`): Lisi, Nora, Malik, Tian und Flocke im Schnee
  (ChatGPT, Stilblock Adventskalender, Original in `quellen/`). Auf dem Desktop ist das Banner dafür höher (2,35:1).
- **Girlande:** `bilder/girlande-weihnachten.webp`, gemalte Tannenzweige mit Kerzen, Zapfen und Beeren,
  freigestellt und gespiegelt gekachelt, damit keine Naht zu sehen ist. Ersetzt die Lichterkette.
- **weihnachten.css** (neu): Girlande, leise Sterne im Hintergrund, Banner-Anpassungen, Schneehauben auf den Kacheln.
- **Schneefall** über der Seite (Skript unten in `index.html`, aus bei „Bewegung reduzieren“).
- **Spruch im Banner:** entfällt in der Weihnachtszeit (Mikes Wunsch); das Spruch-Skript findet kein Element und tut nichts.
- **Kinder-News-Kachel** aus PR #4 übernommen (rechts neben „Bücher“, auf dem Handy vierte Kachel).
- Fußzeile: E-Mail als normaler `mailto:`-Link (Cloudflare verschlüsselt sie beim Ausliefern selbst).


## Rückbau nach den Feiertagen

`<link rel="stylesheet" href="/weihnachten.css">`, `.girlande`, `canvas.schnee` und das Skript
„Weihnachten“ entfernen, Kopfbild, Logo und Favicon-Links zurück auf die alten Dateien.
