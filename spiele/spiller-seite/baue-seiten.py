"""Baut die drei Seiten von spiller.lisi.lu: Startseite (zwei Kategorien), /rechenspiele/ und /deutsch/."""
import pathlib
hier = pathlib.Path(__file__).parent

def seite(titel, beschreibung, wurzel, kopf_links, inhalt):
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titel}</title>
<meta name="description" content="{beschreibung}">
<link rel="icon" type="image/png" href="{wurzel}marke/favicon.png">
<style>
@font-face{{font-family:Andika;font-weight:400;font-display:swap;src:url({wurzel}schriften/andika-latin-400-normal.woff2) format("woff2")}}
@font-face{{font-family:Andika;font-weight:700;font-display:swap;src:url({wurzel}schriften/andika-latin-700-normal.woff2) format("woff2")}}
@font-face{{font-family:Fredoka;font-weight:600;font-display:swap;src:url({wurzel}schriften/fredoka-latin-600-normal.woff2) format("woff2")}}
@font-face{{font-family:Fredoka;font-weight:700;font-display:swap;src:url({wurzel}schriften/fredoka-latin-700-normal.woff2) format("woff2")}}
:root{{--papier:#fff8ec;--tinte:#2f2a44;--sanft:#6b6480;--linie:#e6e0f0;--rot:#ef6f6c;--orange:#f7a541;--gelb:#f2c14e;
  --gruen:#4fb984;--blau:#4ea8de;--lila:#9b7fd4;--marke:#f3bb1c;--marke-dunkel:#d99a00;color-scheme:light}}
*{{box-sizing:border-box}}
html,body{{margin:0}}
body{{color:var(--tinte);font-family:Andika,"Trebuchet MS",system-ui,sans-serif;font-size:18px;line-height:1.5;background-color:var(--papier);
  background-image:radial-gradient(circle at 12% 18%,#ffe3c2 0 6px,transparent 7px),radial-gradient(circle at 82% 8%,#d9f0ff 0 8px,transparent 9px),
  radial-gradient(circle at 70% 70%,#e4f6e9 0 7px,transparent 8px),radial-gradient(circle at 30% 85%,#f1e6ff 0 6px,transparent 7px);background-size:260px 260px}}
a{{color:inherit}}
.regenbogen{{height:8px;background:linear-gradient(90deg,var(--rot),var(--orange),var(--gelb),var(--gruen),var(--blau),var(--lila))}}
.seite{{max-width:1100px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:16px 40px}}
h1,h2,h3{{font-family:Fredoka,"Trebuchet MS",sans-serif;font-weight:600;line-height:1.15;margin:0;text-wrap:balance}}
.kopf{{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}}
.marke{{display:flex;align-items:center;gap:10px;font:600 20px Fredoka,sans-serif;text-decoration:none;background:#fff;border-radius:999px;padding:4px 18px 4px 4px;box-shadow:0 3px 0 rgba(47,42,68,.08)}}
.marke img{{width:44px;height:44px;border-radius:50%;box-shadow:0 0 0 3px #fff,0 0 0 5px var(--marke)}}
.marke b{{color:var(--marke-dunkel);font-weight:700}}
.pille{{font:600 16px Fredoka,sans-serif;color:var(--sanft);text-decoration:none;background:#fff;border-radius:999px;padding:7px 15px;box-shadow:0 3px 0 rgba(47,42,68,.08);display:inline-flex;align-items:center;gap:8px}}
.pille img{{height:1em;transform:scaleX(-1)}}
.hallo{{display:flex;align-items:flex-end;gap:12px;margin:26px 0 10px}}
.hallo img{{width:116px;flex:none}}
.blase{{position:relative;background:#fff;border:3px solid var(--linie);border-radius:22px;padding:14px 18px;margin-bottom:24px;max-width:580px}}
.blase::after{{content:"";position:absolute;left:-12px;bottom:22px;width:18px;height:18px;background:#fff;border-left:3px solid var(--linie);border-bottom:3px solid var(--linie);transform:rotate(45deg)}}
.titel{{font-size:clamp(34px,6.5vw,54px);font-weight:700;margin-bottom:4px}}
.titel span:nth-child(6n+1){{color:var(--rot)}}.titel span:nth-child(6n+2){{color:var(--orange)}}.titel span:nth-child(6n+3){{color:var(--gruen)}}
.titel span:nth-child(6n+4){{color:var(--blau)}}.titel span:nth-child(6n+5){{color:var(--lila)}}.titel span:nth-child(6n+6){{color:#e0a800}}
.raster{{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:20px;margin-top:12px}}
.raster.zwei{{grid-template-columns:repeat(4,minmax(0,260px));justify-content:center;gap:20px}}
@media (max-width:1000px){{.raster.zwei{{grid-template-columns:repeat(2,minmax(0,340px))}}}}
.kachel{{--f:var(--blau);display:flex;flex-direction:column;background:#fff;border:5px solid var(--f);border-radius:28px;overflow:hidden;text-decoration:none;
  box-shadow:0 8px 0 rgba(47,42,68,.07),0 16px 30px rgba(47,42,68,.08);transition:transform .15s}}
.kachel:hover,.kachel:focus-visible{{transform:translateY(-4px)}}
.kachel:focus-visible{{outline:4px solid var(--blau);outline-offset:3px}}
.kachel img{{display:block;width:100%;aspect-ratio:1;object-fit:cover}}
.kachel .text{{padding:12px 16px 16px}}
.kachel h3{{font-size:1.25rem;hyphens:auto;overflow-wrap:break-word}}
.kachel .text p{{font-size:.95rem;color:var(--sanft);margin:2px 0 0}}
.zwei .kachel h3{{font-size:1.6rem}}
.raster .kachel:nth-child(4n+2){{--f:var(--orange)}}.raster .kachel:nth-child(4n+3){{--f:var(--lila)}}.raster .kachel:nth-child(4n+4){{--f:var(--rot)}}
.neu{{display:inline-block;font:600 13px Fredoka,sans-serif;color:#fff;background:var(--rot);border-radius:999px;padding:2px 10px;margin-left:6px;vertical-align:2px}}
.fuss{{margin-top:48px;text-align:center;font-size:14px;color:var(--sanft)}}
@media (max-width:560px){{.raster{{grid-template-columns:1fr 1fr;gap:12px}}.raster.zwei{{grid-template-columns:1fr 1fr;gap:12px}}
  .raster.zwei .kachel:nth-child(3):last-child{{grid-column:1/-1;justify-self:center;width:calc(50% - 6px)}}
  .kachel{{border-width:4px;border-radius:20px}}.kachel .text{{padding:8px 10px 12px}}.kachel h3,.zwei .kachel h3{{font-size:1.05rem}}.kachel .text p{{display:none}}.hallo img{{width:92px}}}}
@media (prefers-reduced-motion: reduce){{.kachel{{transition:none}}}}
</style>
</head>
<body>
<div class="regenbogen"></div>
<div class="seite">
  <header class="kopf">
    <a class="marke" href="{wurzel}"><img src="{wurzel}marke/lisi-logo.png" alt=""><span><b>Lisi</b> Spiele</span></a>
    {kopf_links}
  </header>
{inhalt}
  <footer class="fuss">© 2026 Mike Greiveldinger · <a href="https://lisi.lu">lisi.lu</a> · info@lisi.lu</footer>
</div>
</body>
</html>
"""

def bunt(t):
    return "".join(f"<span>{c}</span>" if c != " " else " " for c in t)

def hallo(wurzel, ueberschrift, text):
    return f"""  <div class="hallo">
    <img src="{wurzel}marke/symbol-lisi-lacht.png" alt="Lisi">
    <div class="blase"><h1 class="titel" aria-label="{ueberschrift}">{bunt(ueberschrift)}</h1>{text}</div>
  </div>"""

def kachel(href, bild, titel, text, extra=""):
    return f"""      <a class="kachel" href="{href}"><img src="{bild}" alt="" loading="lazy">
        <div class="text"><h3>{titel}{extra}</h3><p>{text}</p></div></a>"""

zurueck = '<a class="pille" href="../"><img src="../marke/symbol-finger.png" alt=""> Alle Spiele</a>'
zu_lisi = '<a class="pille" href="https://lisi.lu"><img src="marke/symbol-finger.png" alt=""> Zu lisi.lu</a>'

start = seite("Lisi Spiele", "Lisi Spiele: Rechenspiele, Deutsch, Englisch und Französisch für Kinder von 4 bis 8 Jahren, direkt auf Tablet oder Computer.", "", zu_lisi,
  hallo("", "Spielen und lernen", "Hallo, ich bin Lisi! Möchtest du rechnen, Deutsch, Englisch oder Französisch lernen? Tipp auf ein Bild. <i lang=\"en\">Hello!</i> <i lang=\"fr\">Bonjour !</i>") + f"""
  <div class="raster zwei">
{kachel("rechenspiele/", "kacheln/kategorie-rechenspiele.jpg", "Rechenspiele", "Zählen, Plus und Minus, Mal und Geteilt")}
{kachel("deutsch/", "kacheln/kategorie-deutsch.jpg", "Deutsch", "Wörter hören, lesen und lernen")}
{kachel("english/", "kacheln/kategorie-english.jpg", "English", "Learn English words with Lisi")}
{kachel("francais/", "kacheln/kategorie-francais.jpg", "Français", "Apprends des mots français avec Lisi")}
  </div>""")

rechnen = seite("Rechenspiele – Lisi Spiele", "Rechenspiele mit Lisi: Regenbogenreise, Schatzinsel der Zahlen, Karte der Wunder und Perlentaucher.", "../", zurueck,
  hallo("../", "Rechenspiele", "Such dir ein Rechenspiel aus. Jede richtige Antwort bringt dich weiter!") + f"""
  <div class="raster">
{kachel("regenbogenreise/", "../kacheln/regenbogenreise.jpg", "Lunas Regenbogenreise", "Flieg mit dem Einhorn Luna zum Herz mit der richtigen Zahl.")}
{kachel("schatzinsel/", "../kacheln/schatzinsel.jpg", "Schatzinsel der Zahlen", "Rechne dich zum Schatz: Plus, Minus, Mal und Geteilt.")}
{kachel("https://lisi.lu/abenteuerliches-rechenspiel", "../kacheln/karte-der-wunder.jpg", "Karte der Wunder", "Ein abenteuerliches Rechenspiel mit Lisi.")}
{kachel("perlentaucher/", "../kacheln/perlentaucher.jpg", "Perlentaucher", "Steuere das U-Boot zur Blase mit der richtigen Zahl.")}
  </div>""")

deutsch = seite("Deutsch – Lisi Spiele", "Deutsch lernen mit Lisi: Lisis Wörterwelt mit Hören, Lesen, der/die/das, Buchstaben und Memory.", "../", zurueck,
  hallo("../", "Deutsch", "Hier lernst du deutsche Wörter. Hören, lesen und spielen!") + f"""
  <div class="raster">
{kachel("woerterwelt/", "../kacheln/woerterwelt.jpg", "Lisis Wörterwelt", "Deutsche Wörter hören, lesen und legen: der, die, das, Buchstaben und Memory.", '<span class="neu">Neu</span>')}
  </div>""")

english = seite("English – Lisi Spiele", "Learn English with Lisi: Lisi’s Word World with listening, reading, a or an, spelling and memory.", "../",
  '<a class="pille" href="../"><img src="../marke/symbol-finger.png" alt=""> All games</a>',
  hallo("../", "English", "Hello! Here you can learn English words. Listen, read and play!") + f"""
  <div class="raster">
{kachel("word-world/", "../kacheln/word-world.jpg", "Lisi’s Word World", "Listen, read and spell English words: a or an, letters and memory.", '<span class="neu">New</span>')}
  </div>""").replace('<html lang="de">', '<html lang="en">')

francais = seite("Français – Lisi Spiele", "Apprendre le français avec Lisi : le monde des mots de Lisi, avec écoute, lecture, un ou une, lettres et memory.", "../",
  '<a class="pille" href="../"><img src="../marke/symbol-finger.png" alt=""> Tous les jeux</a>',
  hallo("../", "Français", "Bonjour ! Ici, tu apprends des mots français. Écoute, lis et joue !") + f"""
  <div class="raster">
{kachel("monde-des-mots/", "../kacheln/monde-des-mots.jpg", "Le monde des mots de Lisi", "Écoute, lis et écris des mots français : un ou une, lettres et memory.", '<span class="neu">Nouveau</span>')}
  </div>""").replace('<html lang="de">', '<html lang="fr">')

(hier / "index.html").write_text(start, encoding="utf-8")
(hier / "francais").mkdir(exist_ok=True)
(hier / "francais" / "index.html").write_text(francais, encoding="utf-8")
(hier / "english").mkdir(exist_ok=True)
(hier / "english" / "index.html").write_text(english, encoding="utf-8")
(hier / "rechenspiele" / "index.html").write_text(rechnen, encoding="utf-8")
(hier / "deutsch" / "index.html").write_text(deutsch, encoding="utf-8")
print("OK: 5 Seiten gebaut")
