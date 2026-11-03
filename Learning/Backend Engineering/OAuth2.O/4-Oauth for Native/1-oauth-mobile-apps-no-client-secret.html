<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>OAuth: Mobile Apps and Client Secrets</title>
<style>
:root{
  --bg:#f5f7f6; --surface:#ffffff; --ink:#14232b; --muted:#53666f; --line:#d3dcd9;
  --front:#1f6fb2; --front-bg:#dcebf8; --bad:#b3261e; --bad-bg:#fbe3e1;
  --ok:#0b6e5b; --ok-bg:#dff3ee; --note:#e9eef0; --warn:#8a5a00; --warn-bg:#fbefcf;
  box-sizing:border-box;
  padding-top:env(safe-area-inset-top,0px); padding-bottom:env(safe-area-inset-bottom,0px);
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#0f1a1f; --surface:#17262d; --ink:#e6eef0; --muted:#9db0b8; --line:#2b3d46;
    --front:#7fbaf0; --front-bg:#14304a; --bad:#ff9087; --bad-bg:#3b1c1a;
    --ok:#5fd3b8; --ok-bg:#12332d; --note:#1d2e36; --warn:#f2c36b; --warn-bg:#3a2e12;
  }
}
:root[data-theme="dark"]{
  --bg:#0f1a1f; --surface:#17262d; --ink:#e6eef0; --muted:#9db0b8; --line:#2b3d46;
  --front:#7fbaf0; --front-bg:#14304a; --bad:#ff9087; --bad-bg:#3b1c1a;
  --ok:#5fd3b8; --ok-bg:#12332d; --note:#1d2e36; --warn:#f2c36b; --warn-bg:#3a2e12;
}
html{scroll-padding-top:env(safe-area-inset-top,0px)}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 "Segoe UI",system-ui,-apple-system,Roboto,sans-serif}
main{max-width:900px;margin:0 auto;padding:28px 18px 64px}
h1,h2,h3{font-family:Charter,"Iowan Old Style",Georgia,serif;line-height:1.2;margin:0}
h1{font-size:clamp(28px,5vw,40px);margin-bottom:10px}
h2{font-size:25px;margin:48px 0 6px}
h3{font-size:18px;margin:0 0 6px}
p{margin:8px 0}
.lead{color:var(--muted);font-size:18px;max-width:64ch}
.sub{color:var(--muted);margin:0 0 16px;max-width:66ch}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
@media(max-width:720px){.grid2{grid-template-columns:1fr}}
.box{background:var(--surface);border:1px solid var(--line);border-radius:10px;padding:14px 18px}
.box.bad{border-left:6px solid var(--bad);background:var(--bad-bg)}
.box.ok{border-left:6px solid var(--ok)}
.box.front{border-left:6px solid var(--front)}
.box.warn{border-left:6px solid var(--warn);background:var(--warn-bg)}
.tag{display:inline-block;font-size:13px;font-weight:600;padding:2px 10px;border-radius:99px;margin-right:4px}
.tag.bad{background:var(--bad-bg);color:var(--bad)}
.tag.ok{background:var(--ok-bg);color:var(--ok)}
.tag.front{background:var(--front-bg);color:var(--front)}
ul{margin:8px 0;padding-left:20px}li{margin:4px 0}
.scroll{overflow-x:auto}
svg{max-width:100%;height:auto;display:block}
svg text{font-family:"Segoe UI",system-ui,sans-serif;fill:var(--ink)}
.s-box{fill:var(--surface);stroke:var(--line);stroke-width:1.5}
.s-bad{fill:var(--bad-bg);stroke:var(--bad);stroke-width:2}
.s-ok{fill:var(--ok-bg);stroke:var(--ok);stroke-width:2}
.a-neu{stroke:var(--muted);stroke-width:2.5;fill:none}
.a-bad{stroke:var(--bad);stroke-width:2.5;fill:none}
.t-bad{fill:var(--bad)!important;font-weight:600}
.t-ok{fill:var(--ok)!important;font-weight:600}
.t-muted{fill:var(--muted)!important}
table{width:100%;border-collapse:collapse;background:var(--surface);border:1px solid var(--line)}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top;font-size:15px}
th{background:var(--note)}
tr:last-child td{border-bottom:0}
.flow{display:flex;flex-direction:column;margin:14px 0}
.step{display:grid;grid-template-columns:42px 1fr;gap:12px;position:relative;padding-bottom:14px}
.step:not(:last-child)::before{content:"";position:absolute;left:20px;top:40px;bottom:0;width:2px;background:var(--line)}
.dot{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;font-weight:700;color:#fff;background:#5d6f78}
.dot.x{background:#b3261e}
.ex{background:var(--surface);border:1px dashed var(--line);border-radius:10px;padding:12px 18px;margin:14px 0}
.ex .lbl{font-weight:700;color:var(--muted);font-size:14px}
code{background:var(--note);padding:1px 6px;border-radius:4px;font-size:14px;word-break:break-word}
.tip{background:var(--note);border-radius:10px;padding:12px 16px;margin:14px 0}
</style>
</head>
<body>
<main>

<h1>Mobile apps and the client secret</h1>
<p class="lead">The authorization code flow you learned for web server apps hits one big snag on mobile: you cannot safely ship a client secret inside an app.</p>

<!-- 1 -->
<h2>1. Where we left off</h2>
<div class="box">
  <p>In the web server flow, one of the last steps was using a <b>client secret</b> to exchange the authorization code for an access token. The natural question for mobile: <em>why can't we do the same thing?</em></p>
</div>

<!-- 2 -->
<h2>2. Why a secret cannot live in a mobile app</h2>
<p class="sub">The shipping process itself leaks it.</p>

<div class="flow">
  <div class="step"><div class="dot">1</div>
    <div class="box"><b>Developer puts the client secret in the source code</b></div></div>
  <div class="step"><div class="dot">2</div>
    <div class="box"><b>The app is compiled and published to the App Store</b></div></div>
  <div class="step"><div class="dot">3</div>
    <div class="box"><b>Everybody downloads it</b>
      <p>That means <b>everybody has a copy</b> of the client secret.</p></div></div>
  <div class="step"><div class="dot x">4</div>
    <div class="box bad"><b>Anyone can decompile it</b>
      <p>Plenty of tools exist to decompile binaries shipped on the App Store, so the secret can be extracted. It is no longer secret.</p></div></div>
</div>

<div class="scroll">
<svg viewBox="0 0 860 170" role="img" aria-label="Secret in source code is compiled, published, downloaded by many users, and extracted by decompiling">
  <rect class="s-box" x="10" y="50" width="150" height="60" rx="10"/>
  <text x="85" y="76" text-anchor="middle" font-size="14" font-weight="700">Source code</text>
  <text x="85" y="95" text-anchor="middle" font-size="12" class="t-bad">contains secret</text>
  <rect class="s-box" x="210" y="50" width="150" height="60" rx="10"/>
  <text x="285" y="85" text-anchor="middle" font-size="14" font-weight="700">App Store</text>
  <rect class="s-box" x="410" y="50" width="150" height="60" rx="10"/>
  <text x="485" y="76" text-anchor="middle" font-size="14" font-weight="700">Every user's</text>
  <text x="485" y="95" text-anchor="middle" font-size="14" font-weight="700">phone</text>
  <rect class="s-bad" x="610" y="50" width="240" height="60" rx="10"/>
  <text x="730" y="76" text-anchor="middle" font-size="14" font-weight="700">Decompiler</text>
  <text x="730" y="95" text-anchor="middle" font-size="12" class="t-bad">secret extracted</text>
  <line class="a-neu" x1="162" y1="80" x2="206" y2="80"/>
  <line class="a-neu" x1="362" y1="80" x2="406" y2="80"/>
  <line class="a-bad" x1="562" y1="80" x2="606" y2="80"/>
  <text x="430" y="150" text-anchor="middle" font-size="13" class="t-muted">A secret that every user can obtain is not a secret.</text>
</svg>
</div>

<div class="ex">
  <div class="lbl">Real-life scenario</div>
  <p>Imagine a company printing the master key code on the box of every product it sells. The moment the first box is opened, the code is public. A mobile app binary is that box: every download comes with a copy, and tools can unpack it.</p>
</div>

<!-- 3 -->
<h2>3. The lecture's answer</h2>
<div class="grid2">
  <div class="box ok">
    <span class="tag ok">Solution</span>
    <p>Do <b>not use a client secret</b> in mobile apps.</p>
    <p>The logic: if anyone can use the secret, it is not providing secrecy, so there is no reason to have it at all.</p>
  </div>
  <div class="box front">
    <span class="tag front">Reminder from earlier lessons</span>
    <p>Mobile apps are <b>public clients</b> (no secret). Without a secret, the identity guarantees are weaker, and this is where <b>PKCE</b> and a registered <b>redirect URI</b> come in. This lecture does not go into those details.</p>
  </div>
</div>

<h3 style="margin-top:22px">Web server app vs mobile app</h3>
<div class="scroll">
<table>
  <tr><th></th><th>Web server app</th><th>Mobile app</th></tr>
  <tr><td><b>Code runs</b></td><td>On your server, out of users' reach</td><td>On every user's device</td></tr>
  <tr><td><b>Can keep a secret?</b></td><td><span class="tag ok">Yes</span></td><td><span class="tag bad">No</span> (decompilable)</td></tr>
  <tr><td><b>Client type</b></td><td>Confidential</td><td>Public</td></tr>
  <tr><td><b>Token request</b></td><td>Includes client secret</td><td>No client secret</td></tr>
</table>
</div>

<!-- 4 -->
<h2>4. What comes next</h2>
<div class="box warn">
  The lecture says there are <b>a few other things unique to the mobile environment</b>, covered in the <b>next two lessons</b>. They are not described here, so this page leaves them out rather than guessing.
</div>

<!-- 5 -->
<h2>5. Key takeaways</h2>
<div class="box">
<ul>
  <li>The web flow uses a <b>client secret</b> to exchange the authorization code for an access token.</li>
  <li>Mobile apps cannot safely include one: it ends up in source code, then in the compiled binary on the App Store, then on every user's device.</li>
  <li>Binaries can be <b>decompiled</b>, so the secret is extractable and no longer secret.</li>
  <li>Therefore mobile apps <b>do not use a client secret</b> in the flow.</li>
  <li>More mobile-specific differences follow in the next two lessons.</li>
</ul>
</div>

</main>
</body>
</html>
