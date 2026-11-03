import sys
GEMEINSAM = """<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:Fredoka;font-weight:700;src:url(../../lisis-woerterwelt/schriften/fredoka-latin-700-normal.woff2)}
@font-face{font-family:Fredoka;font-weight:600;src:url(../../lisis-woerterwelt/schriften/fredoka-latin-600-normal.woff2)}
html,body{margin:0}
.k{width:1080px;height:1080px;position:relative;overflow:hidden;font-family:Fredoka,sans-serif;background:var(--bg)}
.eyebrow{position:absolute;top:64px;left:0;right:0;text-align:center;font-weight:600;font-size:32px;letter-spacing:6px;color:#5a3d8a}
h1{position:absolute;top:110px;left:0;right:0;margin:0;text-align:center;font-size:var(--gr,170px);line-height:1;letter-spacing:2px;
 text-shadow:0 7px 0 #fff,0 -3px 0 #fff,5px 0 0 #fff,-5px 0 0 #fff,5px 5px 0 #fff,-5px 5px 0 #fff,0 14px 22px rgba(47,42,68,.28)}
h1 span:nth-child(6n+1){color:#ef6f6c}h1 span:nth-child(6n+2){color:#f7a541}h1 span:nth-child(6n+3){color:#e0a800}
h1 span:nth-child(6n+4){color:#4fb984}h1 span:nth-child(6n+5){color:#4ea8de}h1 span:nth-child(6n+6){color:#9b7fd4}
.wiese{position:absolute;left:-60px;right:-60px;bottom:-150px;height:400px;border-radius:50% 50% 0 0;background:#bfe6a8}
.wiese2{position:absolute;left:-220px;right:320px;bottom:-210px;height:420px;border-radius:50% 50% 0 0;background:#a6dc8c}
.wolke{position:absolute;background:#fff;border-radius:999px}.wolke::before,.wolke::after{content:"";position:absolute;background:#fff;border-radius:50%}
.w1{left:46px;top:330px;width:150px;height:50px}.w1::before{width:70px;height:70px;left:25px;top:-35px}.w1::after{width:50px;height:50px;left:80px;top:-22px}
.w2{right:56px;top:40px;width:170px;height:56px}.w2::before{width:80px;height:80px;left:30px;top:-40px}.w2::after{width:56px;height:56px;left:95px;top:-26px}
.lisi{position:absolute;filter:drop-shadow(0 10px 12px rgba(47,42,68,.2))}
.logo{position:absolute;left:34px;bottom:30px;width:130px;height:130px;border-radius:50%;box-shadow:0 0 0 7px #fff,0 0 0 12px #f3bb1c}
.rund{position:absolute;width:150px;height:150px;border-radius:50%;display:grid;place-items:center;color:#fff;font-weight:700;font-size:96px;line-height:1;
 box-shadow:0 8px 0 rgba(0,0,0,.18),0 0 0 8px #fff}
.zahl{position:absolute;font-weight:700;font-size:110px;color:#fff;-webkit-text-stroke:6px #5a3d8a;paint-order:stroke fill;text-shadow:0 8px 0 rgba(47,42,68,.15)}
.karte{position:absolute;width:200px;height:200px;background:#fff;border-radius:30px;box-shadow:0 10px 0 rgba(47,42,68,.10),0 18px 30px rgba(47,42,68,.18);
 display:grid;place-items:center;border:6px solid var(--f)}
.karte img{width:172px;height:172px;object-fit:contain}
.art{position:absolute;width:140px;height:140px;border-radius:50%;display:grid;place-items:center;color:#fff;font-weight:700;font-size:50px;box-shadow:0 8px 0 rgba(0,0,0,.18),0 0 0 8px #fff}
</style></head><body><div class="k">"""
def bunt(t): return "".join(f"<span>{c}</span>" if c!=" " else " " for c in t)
RECHNEN = GEMEINSAM.replace("var(--bg)","linear-gradient(180deg,#8fd0f5 0%,#d8f2fd 62%,#fff8ec 100%)") + f"""
<div class="wiese2"></div><div class="wiese"></div><div class="wolke w1"></div><div class="wolke w2"></div>
<div class="eyebrow">ZAHLENABENTEUER MIT LISI</div>
<h1 style="--gr:158px">{bunt("Rechenspiele")}</h1>
<div class="rund" style="left:70px;top:430px;background:#ef6f6c">+</div>
<div class="rund" style="left:250px;top:470px;background:#4fb984">−</div>
<div class="rund" style="left:430px;top:430px;background:#f2b31a">×</div>
<div class="rund" style="left:610px;top:470px;background:#2f5f73">÷</div>
<div class="zahl" style="left:200px;top:660px">3</div><div class="zahl" style="left:350px;top:720px">7</div><div class="zahl" style="left:500px;top:650px">5</div>
<img class="lisi" src="lisi-hockt.png" style="right:20px;bottom:30px;height:560px">
<img class="logo" src="../../lisis-woerterwelt/marke/lisi-logo.png">
</div></body></html>"""
DEUTSCH = GEMEINSAM.replace("var(--bg)","linear-gradient(180deg,#ffd9a0 0%,#ffe9c7 58%,#fff8ec 100%)") + f"""
<div class="wiese2"></div><div class="wiese"></div><div class="wolke w1"></div><div class="wolke w2"></div>
<div class="eyebrow">WÖRTERABENTEUER MIT LISI</div>
<h1 style="--gr:200px">{bunt("Deutsch")}</h1>
<div class="art" style="left:80px;top:410px;background:#2f7fb3">der</div>
<div class="art" style="left:250px;top:440px;background:#d9504c">die</div>
<div class="art" style="left:420px;top:410px;background:#33946a">das</div>
<div class="karte" style="left:60px;top:640px;transform:rotate(-7deg);--f:#4ea8de"><img src="../../lisis-woerterwelt/bilder-gemalt/natur-schmetterling.webp"></div>
<div class="karte" style="left:290px;top:680px;transform:rotate(5deg);--f:#ef6f6c"><img src="../../lisis-woerterwelt/bilder-gemalt/essen-erdbeere.webp"></div>
<div class="zahl" style="left:560px;top:600px;font-size:92px">ABC</div>
<img class="lisi" src="lisi-liest.png" style="right:40px;bottom:30px;height:560px">
<img class="logo" src="../../lisis-woerterwelt/marke/lisi-logo.png">
</div></body></html>"""
open(sys.argv[1]+"/rechenspiele.html","w").write(RECHNEN); open(sys.argv[1]+"/deutsch.html","w").write(DEUTSCH)
