/* Study Shelf read aloud: tap the speaker to listen to the chapter from where you are,
   or select some text and tap "Listen" to hear only that. Picks the most natural Indian English voice your device has; you can change it in the panel. */
(function () {
  'use strict';
  if (window.__RA || !('speechSynthesis' in window) || typeof SpeechSynthesisUtterance === 'undefined') return;
  window.__RA = 1;
  var synth = window.speechSynthesis;
  var root = document.querySelector('main.page') || document.querySelector('main') || document.querySelector('.notes') || document.body;
  var SKIP = 'svg,script,style,noscript,button,input,select,textarea,nav,.ra-ui,.hl-ui,.hl-pop,.hl-fab,.hl-panel,.hl-penbar,.hl-penfab,.anchor,#lightbox,[hidden],[aria-hidden="true"]';
  var BLK = 'p,li,h1,h2,h3,h4,h5,h6,td,th,dt,dd,blockquote,figcaption,summary,pre,div,article,section,label';
  var KEY = 'ra:v1', RATES = [0.75, 1, 1.25, 1.5, 1.75, 2];

  var S = { rate: 1, voice: '' };
  try { var sv = JSON.parse(localStorage.getItem(KEY)); if (sv) { S.rate = sv.rate || 1; S.voice = sv.voice || ''; } } catch (e) {}
  function persist() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }

  /* ---------- styles ---------- */
  var css = document.createElement('style');
  css.textContent =
    '.ra-fab{position:fixed;left:14px;bottom:84px;z-index:99990;width:46px;height:46px;border-radius:50%;border:1px solid rgba(0,0,0,.2);background:var(--acc,#0E6B5C);color:#fff;box-shadow:0 4px 14px rgba(0,0,0,.28);cursor:pointer;display:flex;align-items:center;justify-content:center;padding:0;-webkit-tap-highlight-color:transparent}' +
    '.ra-fab svg{width:22px;height:22px;fill:currentColor}' +
    '.ra-pill{position:fixed;z-index:99991;display:flex;align-items:center;gap:6px;padding:8px 14px;border-radius:22px;border:1px solid rgba(0,0,0,.18);background:var(--acc,#0E6B5C);color:#fff;font:600 14px/1 system-ui,sans-serif;box-shadow:0 6px 20px rgba(0,0,0,.3);cursor:pointer}' +
    '.ra-pill svg{width:16px;height:16px;fill:currentColor}' +
    '.ra-panel{position:fixed;left:10px;bottom:138px;z-index:99992;width:min(360px,calc(100vw - 20px));box-sizing:border-box;padding:10px 12px;border-radius:16px;border:1px solid var(--line,#dad6c8);background:var(--surface,#fff);color:var(--ink,#1f2a2a);box-shadow:0 8px 28px rgba(0,0,0,.3);font:14px/1.3 system-ui,sans-serif}' +
    '.ra-panel[hidden]{display:none}' +
    '.ra-row{display:flex;align-items:center;gap:8px}.ra-row+.ra-row{margin-top:8px}' +
    '.ra-st{flex:1;min-width:0;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}' +
    '.ra-b{width:40px;height:40px;border-radius:50%;border:1px solid var(--line,#dad6c8);background:var(--surface2,#f3f1ea);color:var(--ink,#1f2a2a);display:flex;align-items:center;justify-content:center;cursor:pointer;padding:0}' +
    '.ra-b svg{width:18px;height:18px;fill:currentColor}.ra-b.main{background:var(--acc,#0E6B5C);color:#fff;border-color:transparent}' +
    '.ra-sel{flex:1;min-width:0;height:36px;border-radius:10px;border:1px solid var(--line,#dad6c8);background:var(--surface,#fff);color:var(--ink,#1f2a2a);font:13px system-ui,sans-serif;padding:0 6px}' +
    '.ra-help{margin-top:8px;padding:8px 10px;border-radius:10px;background:var(--surface2,#f3f1ea);font-size:12.5px;line-height:1.45;max-height:42vh;overflow:auto}.ra-help[hidden]{display:none}.ra-help b{display:block;margin-top:6px}.ra-help b:first-child{margin-top:0}.ra-lnk{border:0;background:none;color:var(--acc,#0E6B5C);font:600 12.5px system-ui,sans-serif;padding:4px 0;cursor:pointer;text-decoration:underline}' +
    '::highlight(ra-cur){background-color:rgba(255,196,0,.5);color:inherit}' +
    '.ra-cur{background:rgba(255,196,0,.45)!important;border-radius:4px}' +
    '@media print{.ra-fab,.ra-pill,.ra-panel{display:none!important}}';
  document.head.appendChild(css);

  var I = {
    spk: '<svg viewBox="0 0 24 24"><path d="M3 9v6h4l5 5V4L7 9H3zm13.5 3A4.5 4.5 0 0 0 14 8v8a4.5 4.5 0 0 0 2.5-4zM14 3.2v2.1a7 7 0 0 1 0 13.4v2.1a9 9 0 0 0 0-17.6z"/></svg>',
    play: '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>',
    pause: '<svg viewBox="0 0 24 24"><path d="M6 5h4v14H6zm8 0h4v14h-4z"/></svg>',
    stop: '<svg viewBox="0 0 24 24"><path d="M6 6h12v12H6z"/></svg>',
    prev: '<svg viewBox="0 0 24 24"><path d="M6 6h2v12H6zm3.5 6L18 18V6z"/></svg>',
    next: '<svg viewBox="0 0 24 24"><path d="M16 6h2v12h-2zM6 18l8.5-6L6 6z"/></svg>'
  };

  /* ---------- UI ---------- */
  var fab = document.createElement('button');
  fab.type = 'button'; fab.className = 'ra-fab ra-ui'; fab.title = 'Read aloud'; fab.setAttribute('aria-label', 'Read aloud'); fab.innerHTML = I.spk;
  var panel = document.createElement('div');
  panel.className = 'ra-panel ra-ui'; panel.hidden = true;
  panel.innerHTML =
    '<div class="ra-row"><span class="ra-st" id="ra-st" aria-live="polite"></span></div>' +
    '<div class="ra-row"><button type="button" class="ra-b" data-a="prev" aria-label="Previous paragraph">' + I.prev + '</button>' +
    '<button type="button" class="ra-b main" data-a="tog" aria-label="Pause or play">' + I.pause + '</button>' +
    '<button type="button" class="ra-b" data-a="next" aria-label="Next paragraph">' + I.next + '</button>' +
    '<button type="button" class="ra-b" data-a="stop" aria-label="Stop and close">' + I.stop + '</button></div>' +
    '<div class="ra-row"><select class="ra-sel" id="ra-rate" aria-label="Speed"></select><select class="ra-sel" id="ra-voice" aria-label="Voice"></select></div>' +
    '<div class="ra-row"><span class="ra-st" id="ra-vn" style="font-weight:500;font-size:12px;opacity:.75"></span><button type="button" class="ra-lnk" data-a="help">More natural voices</button></div>' +
    '<div class="ra-help" id="ra-help" hidden></div>';
  var pill = document.createElement('button');
  pill.type = 'button'; pill.className = 'ra-pill ra-ui'; pill.innerHTML = I.spk + '<span>Listen</span>'; pill.hidden = true; pill.style.display = 'none';
  document.body.appendChild(fab); document.body.appendChild(panel); document.body.appendChild(pill);
  var elSt = panel.querySelector('#ra-st'), elRate = panel.querySelector('#ra-rate'), elVoice = panel.querySelector('#ra-voice'), btnTog = panel.querySelector('[data-a="tog"]');
  elRate.innerHTML = RATES.map(function (r) { return '<option value="' + r + '"' + (r === S.rate ? ' selected' : '') + '>' + r + 'x speed</option>'; }).join('');

  /* rank voices: Indian English first, then neural / natural / online ones, old robotic engines last */
  function vscore(v) {
    var n = v.name || '', l = (v.lang || '').replace('_', '-'), sc = 0;
    if (/^en-IN$/i.test(l)) sc += 100; else if (/^en-(GB|AU|ZA|SG|NZ|IE)/i.test(l)) sc += 30; else if (/^en/i.test(l)) sc += 15; else return -1;
    if (/india/i.test(n) && !/^en-IN$/i.test(l)) sc += 40;
    if (/natural|neural|wavenet|studio|premium|enhanced|multilingual/i.test(n)) sc += 60;
    if (/online/i.test(n)) sc += 25;
    if (/neerja|prabhat|swara|kajal|aditi|kalpana|rishi|veena|isha|tara|lekha/i.test(n)) sc += 20;
    if (v.localService === false) sc += 8;
    if (/espeak|festival|compact|hemant|ravi\b|heera|\bsam\b|novelty|bad news|bahh|bells|boing|bubbles|cellos|deranged|good news|hysterical|junior|kathy|organ|princess|ralph|trinoids|whisper|zarvox|albert|fred|superstar/i.test(n)) sc -= 80;
    return sc;
  }
  function isNat(v) { return /natural|neural|wavenet|studio|premium|enhanced|multilingual/i.test(v.name) || (/online/i.test(v.name)); }
  function ranked() {
    return (synth.getVoices() || []).map(function (v) { return { v: v, s: vscore(v) }; }).filter(function (x) { return x.s >= 0; })
      .sort(function (a, b) { return b.s - a.s; }).map(function (x) { return x.v; });
  }
  function short(v) { return v.name.replace(/^Microsoft\s+/, '').replace(/\s+-\s+English.*$/, '').replace(/^Google\s+/, 'Google '); }
  function opt(v, star) {
    return '<option value="' + v.voiceURI.replace(/"/g, '&quot;') + '"' + (v.voiceURI === S.voice ? ' selected' : '') + '>' + (star ? '★ ' : '') +
      short(v).replace(/</g, '&lt;') + (isNat(v) ? ' · natural' : '') + ' (' + (v.lang || '').replace('_', '-') + ')</option>';
  }
  function fillVoices() {
    var all = ranked(), ind = all.filter(function (v) { return /^en[-_]IN$/i.test(v.lang); }), rest = all.filter(function (v) { return ind.indexOf(v) < 0; });
    var best = all[0];
    elVoice.innerHTML = '<option value="">Auto: best Indian English voice' + (best ? ' (' + short(best).replace(/</g, '&lt;') + ')' : '') + '</option>' +
      (ind.length ? '<optgroup label="Indian English">' + ind.map(function (v, i) { return opt(v, i === 0); }).join('') + '</optgroup>' : '') +
      (rest.length ? '<optgroup label="Other English voices">' + rest.map(function (v) { return opt(v, false); }).join('') + '</optgroup>' : '');
    showVoiceName();
  }
  function pickVoice() {
    var vs = synth.getVoices() || [], v = null;
    if (S.voice) v = vs.filter(function (x) { return x.voiceURI === S.voice; })[0];
    return v || ranked()[0] || null;
  }
  function showVoiceName() {
    var v = pickVoice(), el = panel.querySelector('#ra-vn'); if (!el) return;
    el.textContent = v ? 'Voice: ' + short(v) + (/^en[-_]IN$/i.test(v.lang) ? '' : ' · no Indian English voice found') : '';
  }
  fillVoices();
  if (synth.addEventListener) synth.addEventListener('voiceschanged', fillVoices); else synth.onvoiceschanged = fillVoices;

  var ua = navigator.userAgent || '', isIOS = /iPad|iPhone|iPod/.test(ua) || (/Mac/.test(ua) && navigator.maxTouchPoints > 1), isAnd = /Android/.test(ua), isEdge = /Edg\//.test(ua);
  var HELP = '<b>Best on a laptop or tablet: Microsoft Edge</b>Open Study Shelf in Edge. It adds "Neerja" and "Prabhat" (natural, Indian English) to the voice list. They need internet and sound close to a real person.' +
    '<b>Android</b>Settings, then Text-to-speech output, Google Speech Services, Install voice data, English (India). Pick the high quality voices, then reopen the page.' +
    '<b>iPhone / iPad</b>Settings, Accessibility, Spoken Content, Voices, English, India. Download "Rishi" or "Veena" in the Enhanced or Premium version, then reopen the page.' +
    '<b>Windows (Chrome)</b>Chrome only shows the older offline voices. Use Edge for the natural ones.';
  var elHelp = panel.querySelector('#ra-help');
  elHelp.innerHTML = (isEdge ? '<b>You are in Edge</b>Choose a voice marked "natural" from the list above. If none shows, check your internet and reopen the page.' : '') + HELP;

  /* ---------- text model ---------- */
  var visCache;
  function shown(el) { if (!visCache.has(el)) visCache.set(el, el.getClientRects().length > 0); return visCache.get(el); }
  var SPELL = /\b(UPSC|APPSC|PYQs?|GS|CSE|IAS|IPS|IFS|RBI|GDP|GNP|GST|FDI|FII|OBCs?|EWS|NRC|CAA|CBI|NIA|WTO|IMF|BJP|INC|NDA|UPA|DPSP|PIL|RTI|CAG|ECI|NHRC|MSP|PDS|SDGs?|CPI|WPI|IIP|FRBM|NPAs?|NBFCs?|SEZs?|PMLA|SC|ST|NCERT|CCLA)\b/g;
  function spell(m) { var pl = /^(PYQ|OBC|SDG|NPA|NBFC|SEZ)s$/.test(m), base = pl ? m.slice(0, -1) : m; return base.split('').join(' ') + (pl ? "'s" : ''); }
  function clean(t) {
    return t.replace(/[\u{1F000}-\u{1FFFF}\u{2600}-\u{27BF}️]/gu, ' ')
      .replace(/\bArt\.?\s*(?=\d)/g, 'Article ').replace(/\bSec\.?\s*(?=\d)/g, 'Section ').replace(/\bCh\.?\s*(?=\d)/g, 'Chapter ')
      .replace(/\bvs\.?(?=\s)/gi, 'versus')
      .replace(/\be\.g\./gi, 'for example').replace(/\bi\.e\./gi, 'that is').replace(/\betc\./gi, 'etcetera')
      .replace(/₹\s?([\d,]+(?:\.\d+)?)/g, '$1 rupees').replace(/\bRs\.?\s?(?=\d)/g, 'rupees ').replace(/(\d)\s?%/g, '$1 percent')
      .replace(/\bCr\b\.?/g, 'crore')
      .replace(/(\d{1,4})\s?[-–]\s?(\d{1,4})(?![-–\d])/g, function (m, a, b, off, str) { return /[-–\d]/.test(str.charAt(off - 1)) ? m : a + ' to ' + b; })
      .replace(SPELL, spell)
      .replace(/[→⇒➜➔]/g, ', ').replace(/&/g, ' and ').replace(/[|•▪◆■]/g, ', ').replace(/\s[–—]\s/g, ', ')
      .replace(/\s+/g, ' ').trim();
  }
  function chunks(t) {
    var out = [];
    t.replace(/([.!?;:])\s+/g, '$1\u0001').split('\u0001').forEach(function (p) {
      while (p.length > 200) {
        var k = p.lastIndexOf(', ', 200); if (k < 60) k = p.lastIndexOf(' ', 200); if (k < 1) k = 200;
        out.push(p.slice(0, k + 1).trim()); p = p.slice(k + 1);
      }
      if (p.trim()) out.push(p.trim());
    });
    return out;
  }
  /* collect readable blocks, in order; with a range, only the selected part */
  function collect(range) {
    visCache = new Map();
    var items = [], cur = null;
    var w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!n.nodeValue || !n.nodeValue.trim()) return NodeFilter.FILTER_REJECT;
        var p = n.parentElement;
        if (!p || p.closest(SKIP)) return NodeFilter.FILTER_REJECT;
        if (range && !range.intersectsNode(n)) return NodeFilter.FILTER_REJECT;
        if (!shown(p)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    }), n;
    while ((n = w.nextNode())) {
      var s = 0, e = n.nodeValue.length;
      if (range) { if (n === range.startContainer) s = range.startOffset; if (n === range.endContainer) e = range.endOffset; if (e <= s) continue; }
      var blk = n.parentElement.closest(BLK) || root;
      if (cur && cur.blk === blk) { cur.parts.push({ n: n, s: s, e: e }); }
      else { cur = { blk: blk, parts: [{ n: n, s: s, e: e }] }; items.push(cur); }
    }
    return items.map(function (it) {
      it.text = clean(it.parts.map(function (p) { return p.n.nodeValue.slice(p.s, p.e); }).join(' '));
      return it;
    }).filter(function (it) { return /[A-Za-z0-9ऀ-෿]/.test(it.text); }).map(function (it) { it.ch = chunks(it.text); return it; });
  }

  /* ---------- highlight current block ---------- */
  var HL = (window.CSS && CSS.highlights && window.Highlight) ? new Highlight() : null;
  if (HL) CSS.highlights.set('ra-cur', HL);
  var lastEl = null;
  function clearHi() { if (HL) HL.clear(); if (lastEl) { lastEl.classList.remove('ra-cur'); lastEl = null; } }
  function hi(it) {
    clearHi();
    var a = it.parts[0], b = it.parts[it.parts.length - 1], r = document.createRange();
    try { r.setStart(a.n, a.s); r.setEnd(b.n, b.e); } catch (e) { return; }
    if (HL) HL.add(r);
    else if (it.blk !== root && it.blk.getBoundingClientRect().height < 260) { it.blk.classList.add('ra-cur'); lastEl = it.blk; }
    var rc = r.getBoundingClientRect();
    if (rc.height && (rc.top < 70 || rc.bottom > innerHeight - 150)) window.scrollTo({ top: window.scrollY + rc.top - innerHeight * 0.3, behavior: 'smooth' });
  }

  /* ---------- playback ---------- */
  var items = [], ii = 0, ci = 0, state = 'idle', tok = 0, mode = 'page';
  function setUi() {
    fab.innerHTML = state === 'playing' ? I.pause : (state === 'paused' ? I.play : I.spk);
    fab.title = state === 'playing' ? 'Pause' : (state === 'paused' ? 'Resume' : 'Read aloud');
    btnTog.innerHTML = state === 'playing' ? I.pause : I.play;
    panel.hidden = state === 'idle';
    if (state !== 'idle') elSt.textContent = (state === 'paused' ? 'Paused · ' : (mode === 'selection' ? 'Reading selection · ' : 'Reading · ')) + 'part ' + (ii + 1) + ' of ' + items.length;
  }
  function speak() {
    var my = ++tok; synth.cancel();
    if (ii >= items.length) { finish(); return; }
    var it = items[ii]; hi(it); setUi();
    var v = pickVoice(), lim = v && /online|natural|neural/i.test(v.name) ? 320 : 200, txt = it.ch[ci], k = ci + 1;
    while (k < it.ch.length && txt.length + 1 + it.ch[k].length <= lim) { txt += ' ' + it.ch[k]; k++; }
    var u = new SpeechSynthesisUtterance(txt); u.rate = S.rate;
    if (v) { u.voice = v; u.lang = v.lang; } else u.lang = 'en-IN';
    var done = function () { if (my !== tok || state !== 'playing') return; ci = k; if (ci >= it.ch.length) { ii++; ci = 0; } speak(); };
    u.onend = done;
    u.onerror = function (ev) { if (my !== tok) return; if (ev && (ev.error === 'interrupted' || ev.error === 'canceled')) return; done(); };
    setTimeout(function () { if (my === tok && state === 'playing') synth.speak(u); }, 30);
  }
  function finish() { tok++; synth.cancel(); clearHi(); state = 'idle'; setUi(); }
  function stop() { finish(); }
  function pause() { if (state !== 'playing') return; tok++; synth.cancel(); state = 'paused'; setUi(); }
  function resume() { if (state !== 'paused') return; state = 'playing'; speak(); }
  function jump(d) {
    if (state === 'idle') return;
    ii = Math.max(0, Math.min(items.length - 1, ii + d)); ci = 0; state = 'playing'; speak();
  }
  function firstVisible(list) {
    for (var k = 0; k < list.length; k++) {
      var a = list[k].parts[0], r = document.createRange();
      try { r.setStart(a.n, a.s); r.setEnd(a.n, Math.min(a.e, a.s + 1)); } catch (e) { continue; }
      var rc = r.getBoundingClientRect(); if (rc.bottom > 80) return k;
    }
    return 0;
  }
  function start(range) {
    var list = collect(range);
    if (!list.length) { state = 'idle'; panel.hidden = false; elSt.textContent = 'Nothing to read here.'; setTimeout(function () { if (state === 'idle') panel.hidden = true; }, 2200); return; }
    items = list; mode = range ? 'selection' : 'page'; ii = range ? 0 : firstVisible(list); ci = 0; state = 'playing';
    hidePill(); speak();
  }

  /* ---------- selection ---------- */
  var lastSel = null, uiTouch = 0, st;
  function selRange() {
    var s = window.getSelection(); if (!s || !s.rangeCount || s.isCollapsed) return null;
    var r = s.getRangeAt(0);
    if (!r.intersectsNode(root)) return null;
    var anc = r.commonAncestorContainer; anc = anc.nodeType === 1 ? anc : anc.parentElement;
    if (anc && anc.closest && anc.closest('.ra-ui')) return null;
    if (s.toString().trim().length < 2) return null;
    return r.cloneRange();
  }
  function hidePill() { pill.hidden = true; pill.style.display = 'none'; }
  function showPill(r) {
    var rc = r.getBoundingClientRect(); if ((!rc.width && !rc.height) || rc.bottom < 0 || rc.top > innerHeight) return hidePill();
    pill.hidden = false; pill.style.display = 'flex';
    var w = pill.offsetWidth || 96, x = Math.max(8, Math.min(innerWidth - w - 8, rc.left + rc.width / 2 - w / 2));
    var y = rc.bottom + 14; if (y > innerHeight - 70) y = Math.max(8, rc.top - 56 - 44);
    pill.style.left = x + 'px'; pill.style.top = y + 'px';
  }
  document.addEventListener('selectionchange', function () {
    clearTimeout(st);
    st = setTimeout(function () {
      var r = selRange();
      if (r) { lastSel = r; showPill(r); }
      else if (Date.now() - uiTouch > 700) { lastSel = null; hidePill(); }
    }, 250);
  });
  [fab, pill, panel].forEach(function (el) {
    el.addEventListener('pointerdown', function (e) { uiTouch = Date.now(); if (el !== panel || !/SELECT|OPTION/.test(e.target.tagName)) e.preventDefault(); });
    el.addEventListener('mousedown', function (e) { if (el !== panel || !/SELECT|OPTION/.test(e.target.tagName)) e.preventDefault(); });
  });

  fab.addEventListener('click', function () {
    var live = selRange();
    if (live) { start(live); return; }
    if (state === 'playing') pause();
    else if (state === 'paused') resume();
    else if (lastSel) start(lastSel);
    else start(null);
  });
  pill.addEventListener('click', function () { var r = selRange() || lastSel; if (r) start(r); });
  panel.addEventListener('click', function (e) {
    var b = e.target.closest('[data-a]'); if (!b) return; var a = b.getAttribute('data-a');
    if (a === 'tog') { if (state === 'playing') pause(); else if (state === 'paused') resume(); }
    else if (a === 'help') { elHelp.hidden = !elHelp.hidden; b.textContent = elHelp.hidden ? 'More natural voices' : 'Hide tips'; }
    else if (a === 'prev') jump(-1); else if (a === 'next') jump(1); else if (a === 'stop') stop();
  });
  elRate.addEventListener('change', function () { S.rate = parseFloat(elRate.value) || 1; persist(); if (state === 'playing') speak(); });
  elVoice.addEventListener('change', function () { S.voice = elVoice.value; persist(); showVoiceName(); if (state === 'playing') speak(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && state !== 'idle') stop(); });
  window.addEventListener('pagehide', function () { try { synth.cancel(); } catch (e) {} });
})();
