# lisi.lu – Weihnachts-Look 2026: Übergabe

Stand: 25.11.2026. Von Mike freigegeben als Entwurf („Gut so“), **noch nicht live**.
Entwurf und alle Dateien: GitHub `mikegreiveldinger/lisisongs`, PR #5, Branch `claude/project-thread-y5dquq`, Ordner `startseite/weihnachten/`.
Grundlage ist die echte Startseite von lisi.lu vom 25.11.2026 (gesichert als `startseite/weihnachten/index-live-2026-11-25.html`).
Die fertige Startseite liegt als `startseite/weihnachten/index.html` bereit; die Ordnerstruktur dort entspricht dem Webserver.

## Was sich ändert

1. **Logo:** Lisi mit Weihnachtsmütze im Logo „Lisi's World“ (Schriftzug unverändert).
2. **Favicon und App-Symbol** aus dem Mützen-Logo.
3. **Banner:** neues Winterbild (ChatGPT, Stilblock Adventskalender): Lisi, Nora, Malik, Tian und Flocke am Abend im Schnee. Auf dem Desktop ist das Banner höher (2,35 : 1), auf dem Handy 1,6 : 1 mit Ausschnitt nach rechts. **Der Spruch im Banner entfällt** (Mikes Wunsch).
4. **Christbaumkugeln:** fünf gemalte Kugeln mit Lisi, Nora, Malik, Tian und Flocke hängen an roten Bändern links im Himmel des Banners (wo vorher der Spruch stand) und pendeln leicht (aus bei „Bewegung reduzieren“). Das **Logo** sitzt dafür unten links im Banner.
5. **Girlande:** gemalte Tannenzweige mit Kerzen, Zapfen, Beeren und Schnee über die ganze Breite, hängt über den oberen Rand des Banners.
6. **Schneefall:** leise Flocken über der Seite (aus bei „Bewegung reduzieren“).
7. **Hintergrund:** ganz blasse Sterne und Punkte; **Kacheln** tragen eine kleine Schneehaube.
8. **Kinder-News-Kachel** (aus PR #4) rechts neben „Bücher“, auf dem Handy vierte Kachel. Holt die Meldungen aus `https://stories.lisi.lu/neu.json` (Einträge mit `"kategorie": "Kinder-News"`), verlinkt auf `https://stories.lisi.lu/nachrichten`. Im Test kamen echte Meldungen an.

Flocke: junges Rentier aus dem Adventskalender (Dateien „Lisis Winterreise“), Material in Nextcloud unter `Lisi Media/Claude Projekte/lisi-spiele/Adventskalender/`. Quellbilder der neuen Bilder: `Lisi Media/Claude Projekte/lisi.lu Weihnachten 2026/`.

## 1. Dateien hochladen

| Pfad auf lisi.lu | Inhalt | Download |
|---|---|---|
| `/bilder/lisis-world-weihnachten.png` | Logo mit Lisi in Weihnachtsmütze (593×180) | https://raw.githubusercontent.com/mikegreiveldinger/lisisongs/claude/project-thread-y5dquq/startseite/weihnachten/bilder/lisis-world-weihnachten.png |
| `/bilder/favicon-weihnachten-32.png` | Favicon 32 px | https://raw.githubusercontent.com/mikegreiveldinger/lisisongs/claude/project-thread-y5dquq/startseite/weihnachten/bilder/favicon-weihnachten-32.png |
| `/bilder/favicon-weihnachten-192.png` | Favicon 192 px | https://raw.githubusercontent.com/mikegreiveldinger/lisisongs/claude/project-thread-y5dquq/startseite/weihnachten/bilder/favicon-weihnachten-192.png |
| `/bilder/apple-touch-icon-weihnachten.png` | App-Symbol 180 px | https://raw.githubusercontent.com/mikegreiveldinger/lisisongs/claude/project-thread-y5dquq/startseite/weihnachten/bilder/apple-touch-icon-weihnachten.png |
| `/bilder/kopfbild-weihnachten.jpg` | Winterbanner 1672×941 (Kinder und Flocke) | https://raw.githubusercontent.com/mikegreiveldinger/lisisongs/claude/project-thread-y5dquq/startseite/weihnachten/bilder/kopfbild-weihnachten.jpg |
| `/bilder/kopfbild-weihnachten-klein.jpg` | Winterbanner 836×470 | https://raw.githubusercontent.com/mikegreiveldinger/lisisongs/claude/project-thread-y5dquq/startseite/weihnachten/bilder/kopfbild-weihnachten-klein.jpg |
| `/bilder/girlande-weihnachten.webp` | Gemalte Girlande, freigestellt, nahtlos kachelbar (2400×147) | https://raw.githubusercontent.com/mikegreiveldinger/lisisongs/claude/project-thread-y5dquq/startseite/weihnachten/bilder/girlande-weihnachten.webp |
| `/bilder/kugel-lisi.webp` | Christbaumkugel mit Lisi (freigestellt) | https://raw.githubusercontent.com/mikegreiveldinger/lisisongs/claude/project-thread-y5dquq/startseite/weihnachten/bilder/kugel-lisi.webp |
| `/bilder/kugel-nora.webp` | Christbaumkugel mit Nora (freigestellt) | https://raw.githubusercontent.com/mikegreiveldinger/lisisongs/claude/project-thread-y5dquq/startseite/weihnachten/bilder/kugel-nora.webp |
| `/bilder/kugel-malik.webp` | Christbaumkugel mit Malik (freigestellt) | https://raw.githubusercontent.com/mikegreiveldinger/lisisongs/claude/project-thread-y5dquq/startseite/weihnachten/bilder/kugel-malik.webp |
| `/bilder/kugel-tian.webp` | Christbaumkugel mit Tian (freigestellt) | https://raw.githubusercontent.com/mikegreiveldinger/lisisongs/claude/project-thread-y5dquq/startseite/weihnachten/bilder/kugel-tian.webp |
| `/bilder/kugel-flocke.webp` | Christbaumkugel mit Flocke (freigestellt) | https://raw.githubusercontent.com/mikegreiveldinger/lisisongs/claude/project-thread-y5dquq/startseite/weihnachten/bilder/kugel-flocke.webp |
| `/weihnachten.css` | Alle Weihnachts-Stile (kommt ins Wurzelverzeichnis neben stil.css) | https://raw.githubusercontent.com/mikegreiveldinger/lisisongs/claude/project-thread-y5dquq/startseite/weihnachten/weihnachten.css |

Die alten Dateien (`lisis-world-bunt.png`, `favicon-32.png`, `favicon-192.png`, `apple-touch-icon.png`, `kopfbild-freunde*.jpg`) bleiben liegen, damit man nach den Feiertagen zurückwechseln kann.

## 2. Änderungen in `index.html` (Startseite)

**a) Im `<head>`** die drei Icon-Zeilen ersetzen und nach `stil.css` die Weihnachts-CSS einbinden:

```html
<link rel="icon" type="image/png" sizes="32x32" href="/bilder/favicon-weihnachten-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/bilder/favicon-weihnachten-192.png">
<link rel="apple-touch-icon" href="/bilder/apple-touch-icon-weihnachten.png">
```

```html
<link rel="stylesheet" href="/stil.css">
<link rel="stylesheet" href="/weihnachten.css">
```

**b) Direkt nach `<div class="regenbogen"></div>`** einfügen:

```html
<div class="girlande" aria-hidden="true"></div>
<canvas class="schnee" aria-hidden="true"></canvas>
```

**c) Im Banner** das ganze `<picture>…</picture>` ersetzen durch:

```html
<picture>
  <img src="/bilder/kopfbild-weihnachten.jpg" srcset="/bilder/kopfbild-weihnachten-klein.jpg 836w, /bilder/kopfbild-weihnachten.jpg 1672w" sizes="(max-width: 1120px) 100vw, 1090px"
       width="1672" height="941" alt="Lisi, ihre Schwester Nora und ihre Freunde Tian und Malik stehen am Abend im Schnee bei Laternen. Nora streichelt das kleine Rentier Flocke mit dem gestreiften Schal.">
</picture>
```

(Das `<source media="(max-width: 559px)" …kopfbild-freunde-handy.jpg>` fällt weg, das Winterbild wird auch auf dem Handy benutzt.)

**d) Logo** im Banner: `src="/bilder/lisis-world-bunt.png"` → `src="/bilder/lisis-world-weihnachten.png"`. (Die Position unten links regelt `weihnachten.css`.)

**d2) Kugeln:** direkt vor dem Logo-Link (`<a class="logo" …>`) im `<div class="kopfbild">` einfügen:

```html
<div class="kugeln" aria-hidden="true">
  <img class="k1" src="/bilder/kugel-lisi.webp" width="218" height="464" alt="">
  <img class="k2" src="/bilder/kugel-nora.webp" width="214" height="462" alt="">
  <img class="k3" src="/bilder/kugel-malik.webp" width="214" height="464" alt="">
  <img class="k4" src="/bilder/kugel-tian.webp" width="214" height="463" alt="">
  <img class="k5" src="/bilder/kugel-flocke.webp" width="220" height="464" alt="">
</div>
```

**e) Spruch entfernen:** die Zeile `<p class="spruch" id="spruch">…</p>` löschen. Das Spruch-Skript unten findet dann kein Element und tut nichts; es kann für später stehen bleiben.

**f) Kinder-News-Kachel** als vierte Kachel vor `</main>` einfügen:

```html
    <a class="kachel news" href="https://stories.lisi.lu/nachrichten" id="news-kachel" data-quelle="https://stories.lisi.lu/neu.json">
      <div class="newsfenster" aria-hidden="true">
        <span class="live">Neues aus Luxemburg</span>
        <ul class="meldungen">
          <li class="meldung aktiv"><strong>Die neuesten Kinder-News aus Luxemburg</strong><small>Hier tippen zum Lesen</small></li>
        </ul>
        <div class="punkte"></div>
      </div>
      <h2>Kinder-News</h2>
      <p>Neues aus Luxemburg</p>
    </a>

```

**g) Vor `</body>`** die zwei Skripte einfügen:

```html
<script>
/* Kinder-News-Kachel (aus dem Entwurf PR 4): holt https://stories.lisi.lu/neu.json, nimmt die Einträge mit
   "kategorie": "Kinder-News" (neueste zuerst, höchstens 5) und zeigt sie abwechselnd alle 4 Sekunden.
   Braucht auf stories.lisi.lu den CORS-Header Access-Control-Allow-Origin für lisi.lu. */
(function(){
  var kachel=document.getElementById('news-kachel'); if(!kachel||!window.fetch) return;
  var quelle=kachel.getAttribute('data-quelle');
  var liste=kachel.querySelector('.meldungen'), punkte=kachel.querySelector('.punkte');
  var ruhig=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  function feld(o,n){for(var i=0;i<n.length;i++){if(o[n[i]])return o[n[i]]}return ''}
  function eintraege(d){if(Array.isArray(d))return d;if(d&&Array.isArray(d.liste))return d.liste;for(var k in d){if(Array.isArray(d[k]))return d[k]}return []}
  function datumText(d){var t=new Date(d);return isNaN(t)?d:t.toLocaleDateString('de-DE',{day:'numeric',month:'long'})}
  fetch(quelle,{cache:'no-cache'}).then(function(r){if(!r.ok)throw r;return r.json()}).then(function(daten){
    var news=eintraege(daten).filter(function(n){return String(n.kategorie||'').toLowerCase()==='kinder-news'})
      .map(function(n){return{titel:feld(n,['titel','title']),datum:feld(n,['iso','datum','date']),bild:feld(n,['bild','image','img'])}})
      .filter(function(n){return n.titel})
      .sort(function(a,b){return String(b.datum).localeCompare(String(a.datum))}).slice(0,5);
    if(!news.length) return;
    liste.innerHTML='';
    news.forEach(function(n){
      var li=document.createElement('li'); li.className='meldung';
      if(n.bild){var im=document.createElement('img');im.src=new URL(n.bild,quelle).href;im.alt='';im.loading='lazy';li.appendChild(im)}
      var t=document.createElement('strong'); t.textContent=n.titel;
      var s=document.createElement('small'); s.textContent=n.datum?datumText(n.datum):'';
      li.append(t,s); liste.appendChild(li); punkte.appendChild(document.createElement('span'));
    });
    var m=liste.children,p=punkte.children,i=0,pause=false;
    m[0].classList.add('aktiv'); p[0].classList.add('aktiv');
    kachel.setAttribute('aria-label','Kinder-News. Neu: '+news[0].titel);
    if(ruhig||m.length<2){punkte.innerHTML='';return}
    kachel.addEventListener('mouseenter',function(){pause=true});
    kachel.addEventListener('mouseleave',function(){pause=false});
    setInterval(function(){
      if(pause||document.hidden) return;
      var alt=m[i]; alt.classList.remove('aktiv'); alt.classList.add('weg'); p[i].classList.remove('aktiv');
      setTimeout(function(){alt.classList.remove('weg')},650);
      i=(i+1)%m.length; m[i].classList.add('aktiv'); p[i].classList.add('aktiv');
    },4000);
  }).catch(function(){});
})();
</script>
<script>
/* Weihnachten: leiser Schneefall über der Seite (bei „Bewegung reduzieren“ aus) */
(function () {
  var c = document.querySelector('canvas.schnee'); if (!c || !c.getContext) return;
  if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) { c.remove(); return; }
  var g = c.getContext('2d'), flocken = [], w, h, dpr = Math.min(window.devicePixelRatio || 1, 2);
  function groesse() {
    w = c.width = innerWidth * dpr; h = c.height = innerHeight * dpr;
    var soll = Math.round(Math.min(70, innerWidth / 22));
    while (flocken.length < soll) flocken.push(neu(true));
    flocken.length = soll;
  }
  function neu(irgendwo) {
    var r = (1.2 + Math.random() * 2.6) * dpr;
    return { x: Math.random() * w, y: irgendwo ? Math.random() * h : -r * 2, r: r,
             v: (0.25 + Math.random() * 0.55) * dpr, phase: Math.random() * 6.3, wind: 0.3 + Math.random() * 0.5 };
  }
  function bild(t) {
    if (!document.hidden) {
      g.clearRect(0, 0, w, h);
      for (var i = 0; i < flocken.length; i++) {
        var f = flocken[i];
        f.y += f.v; f.x += Math.sin(t / 1600 + f.phase) * f.wind * dpr * 0.4;
        if (f.y > h + f.r) flocken[i] = f = neu(false);
        g.beginPath(); g.arc(f.x, f.y, f.r, 0, 6.2832);
        g.fillStyle = 'rgba(255,255,255,.95)'; g.shadowColor = 'rgba(90,130,180,.45)'; g.shadowBlur = 3 * dpr; g.fill();
      }
    }
    requestAnimationFrame(bild);
  }
  groesse(); addEventListener('resize', groesse); requestAnimationFrame(bild);
})();
</script>
```

Hinweis: Die Fußzeilen-Adresse info@lisi.lu verschlüsselt Cloudflare beim Ausliefern selbst; daran ist nichts zu ändern.

## 3. Neue Datei `/weihnachten.css`

```css
/* Lisi's World – Weihnachtszeit. Ergänzt /stil.css, ändert daran nichts.
   Nach den Feiertagen: <link> auf diese Datei entfernen, dann ist alles wie vorher. */

:root {
  --tanne: #2f7a52;
  --beere: #c8423b;
  --gold: #e9b33b;
  --news: #1f7fb8;
}

/* Papier mit ganz leisen Sternen */
body {
  background-color: var(--papier);
  background-image:
    url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cg fill='%23e9b33b' fill-opacity='.16'%3E%3Cpath d='M30 22l2.4 5 5.4.6-4 3.7 1.1 5.3-4.9-2.7-4.9 2.7 1.1-5.3-4-3.7 5.4-.6z'/%3E%3Cpath d='M132 104l1.8 3.7 4 .5-3 2.8.8 4-3.6-2-3.6 2 .8-4-3-2.8 4-.5z'/%3E%3C/g%3E%3Cg fill='%2395bfdf' fill-opacity='.22'%3E%3Ccircle cx='96' cy='38' r='2.2'/%3E%3Ccircle cx='58' cy='132' r='1.8'/%3E%3Ccircle cx='160' cy='20' r='1.5'/%3E%3Ccircle cx='12' cy='96' r='1.6'/%3E%3C/g%3E%3C/svg%3E");
}

/* Gemalte Girlande (Tannenzweige, Kerzen, Zapfen, Beeren) hängt über den oberen Rand bis ins Kopfbild */
.girlande {
  position: absolute; left: 0; right: 0; top: 8px; height: clamp(54px, 7.4vw, 112px); z-index: 3; pointer-events: none;
  background: url(/bilder/girlande-weihnachten.webp) repeat-x center top / auto 100%;
}
body { position: relative; }
.seite { padding-top: clamp(40px, 5.4vw, 80px); }

/* Schneefall über der ganzen Seite (wird im Skript gezeichnet) */
canvas.schnee { position: fixed; inset: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 50; }

/* Banner: Winterbild mit den vier Kindern und Flocke (höher als das Sommerbild, damit niemand abgeschnitten wird) */
.kopf.banner .kopfbild { aspect-ratio: 2.35 / 1; }
.kopf.banner .kopfbild img { object-position: 50% 55%; }
.banner .logo { background: rgba(255, 255, 255, .88); }
/* Christbaumkugeln mit Lisi, Nora, Malik, Tian und Flocke hängen links im Himmel; das Logo rückt nach unten links */
.kopf.banner .logo { top: auto; bottom: 6%; }
.kugeln { position: absolute; left: 1.5%; top: 0; width: 35%; height: 100%; overflow: hidden; pointer-events: none; }
.kopf.banner .kugeln img { position: absolute; width: 22%; height: auto; object-fit: contain; border-radius: 0; transform-origin: 50% 0; }
.kugeln .k1 { left: 0%;    top: 2%; }
.kugeln .k2 { left: 16.5%; top: -8%; }
.kugeln .k3 { left: 33%;   top: 12%; }
.kugeln .k4 { left: 49.5%; top: -4%; }
.kugeln .k5 { left: 66%;   top: 8%; }
@media (prefers-reduced-motion: no-preference) {
  .kugeln img { animation: pendeln 5s ease-in-out infinite alternate; }
  .kugeln .k2 { animation-delay: -1.3s; } .kugeln .k3 { animation-delay: -2.6s; }
  .kugeln .k4 { animation-delay: -0.7s; } .kugeln .k5 { animation-delay: -3.4s; }
}
@keyframes pendeln { from { transform: rotate(-2.5deg); } to { transform: rotate(2.5deg); } }
@media (max-width: 559px) {
  .kopf.banner .kopfbild { aspect-ratio: 1.6 / 1; margin-bottom: 0; }
  .kopf.banner .kopfbild img { object-position: 72% 50%; }
  .kugeln { left: 1%; width: 42%; border-radius: 20px 0 0 0; }
}

/* „Neu bei Lisi“: Karten mit kleinem Goldrand-Schimmer */
.neu-karte { box-shadow: var(--schatten), 0 0 0 2px rgba(233, 179, 59, .18); }

/* Kacheln: jede trägt eine kleine Schneehaube */
.kachel { position: relative; }
.kachel::before {
  content: ""; position: absolute; left: 18px; right: 18px; top: -9px; height: 22px; pointer-events: none; z-index: 2;
  background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 22' preserveAspectRatio='none'%3E%3Cpath d='M0 14 C10 2 30 2 45 8 C60 0 85 0 100 7 C118 -1 140 2 152 9 C170 0 196 1 210 8 C226 0 252 0 266 8 C280 2 296 4 300 14 V22 H0Z' fill='%23ffffff'/%3E%3C/svg%3E") no-repeat top / 100% 100%;
  filter: drop-shadow(0 -2px 3px rgba(90, 130, 180, .18));
}

/* ===== KINDER-NEWS-Kachel (aus Entwurf PR 4, an stil.css angepasst) ===== */
@media (min-width: 600px) { .kacheln { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 900px) { .kacheln { grid-template-columns: repeat(4, 1fr); gap: 22px; } }
.news h2 { color: var(--news); }
.newsfenster {
  position: relative; overflow: hidden; width: 100%; aspect-ratio: 1; border-radius: 18px;
  background: radial-gradient(circle at 85% 12%, #ffe38a 0 9%, transparent 10%), linear-gradient(#bfe3f7, #e6f3fb 60%, #fff8ec);
  display: flex; flex-direction: column; text-align: left; padding: 12px 12px 22px;
}
.newsfenster .live {
  position: relative; z-index: 2; align-self: flex-start; display: flex; align-items: center; gap: 6px;
  background: #fff; border-radius: 999px; padding: 3px 10px 3px 8px;
  font: 600 13px Fredoka, sans-serif; color: var(--news); box-shadow: 0 2px 8px rgba(31, 127, 184, .15);
}
.newsfenster .live::before { content: ""; width: 8px; height: 8px; border-radius: 50%; background: #e8493f; animation: puls 1.6s ease-in-out infinite; }
.meldungen { position: relative; flex: 1; min-height: 9.5em; list-style: none; margin: 8px 0 0; padding: 0; }
.meldung {
  position: absolute; left: 0; right: 0; top: 50%; background: #fff; border-radius: 16px; padding: 10px 12px;
  box-shadow: 0 6px 18px rgba(31, 127, 184, .15); opacity: 0; transform: translateY(-30%) scale(.96);
  transition: opacity .6s ease, transform .6s ease; pointer-events: none;
}
.meldung.aktiv { opacity: 1; transform: translateY(-50%) scale(1); pointer-events: auto; }
.meldung.weg { opacity: 0; transform: translateY(-75%) scale(.96); }
.meldung img { width: 100%; aspect-ratio: 2 / 1; object-fit: cover; border-radius: 10px; margin-bottom: 8px; }
.meldung strong { display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; font: 600 17px/1.25 Fredoka, sans-serif; color: var(--tinte); }
.meldung small { display: block; color: var(--sanft); font-size: 14px; margin-top: 4px; }
.punkte { position: absolute; bottom: 8px; left: 0; right: 0; display: flex; justify-content: center; gap: 6px; }
.punkte span { width: 8px; height: 8px; border-radius: 50%; background: rgba(31, 127, 184, .25); transition: background .3s, width .3s; }
.punkte span.aktiv { background: var(--news); width: 20px; border-radius: 999px; }
@keyframes puls { 50% { opacity: .35; } }
@media (min-width: 900px) { .meldung img { aspect-ratio: 5 / 2; } .meldung strong { font-size: 16px; } }

@media (prefers-reduced-motion: reduce) {
  .newsfenster .live::before { animation: none; }
  .meldung { transition: none; }
}
```

## 4. Prüfen

- Desktop und Handy: Girlande oben, Banner mit allen fünf Figuren ganz sichtbar, fünf Kugeln links im Himmel, Logo unten links, kein Spruch, vier Kacheln.
- Kinder-News-Kachel zeigt echte Meldungen (sonst den Platzhalter „Die neuesten Kinder-News aus Luxemburg“). Falls nicht: CORS-Header für lisi.lu auf `stories.lisi.lu/neu.json` prüfen.
- Vorschaubilder: `startseite/weihnachten/vorschau/` im Repo.

## 5. Rückbau nach den Feiertagen

`<link … weihnachten.css>`, `.girlande`, `canvas.schnee`, `.kugeln` und das Skript „Weihnachten: leiser Schneefall“ entfernen; Kopfbild, Logo und Icons zurück auf die alten Dateien; `<p class="spruch" id="spruch">Hallo! Was machen wir heute?</p>` wieder ins Banner setzen. Die Kinder-News-Kachel bleibt (ihre Stile stehen dann noch in `weihnachten.css` und müssten nach `stil.css` umziehen).

## Noch offen

Nichts am Design. Fehlt nur Mikes Freigabe und das Hochladen auf den Webserver.
