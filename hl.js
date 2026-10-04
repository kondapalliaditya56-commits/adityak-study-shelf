/* Study Shelf highlighter: coloured highlights for every notebook page.
   Select text, tap a colour. Tap a highlight to change or remove it. Saved on this device. */
(function () {
  'use strict';
  var KEY = 'nbhl:v1';
  var root = document.querySelector('.notes') || document.querySelector('main.page') || document.querySelector('main');
  if (!root || !window.__NB) return;
  var page = (location.pathname.split('/').pop() || 'index.html').replace(/\.html$/, '');

  var COLORS = [
    { k: 'yellow', name: 'Important', hex: '#ffd60a' },
    { k: 'pink', name: 'VV important', hex: '#ff5d8f' },
    { k: 'green', name: 'Fact to know', hex: '#34c759' },
    { k: 'blue', name: 'Revise or doubt', hex: '#4aa3ff' },
    { k: 'orange', name: 'Mains angle', hex: '#ff9f0a' }
  ];

  // ---------- storage
  function load() { try { return JSON.parse(localStorage.getItem(KEY)) || {}; } catch (e) { return {}; } }
  function saveAll(all) { try { localStorage.setItem(KEY, JSON.stringify(all)); } catch (e) {} }
  var ALL = load();
  var H = ALL[page] || [];
  function persist() { if (H.length) ALL[page] = H; else delete ALL[page]; saveAll(ALL); updateBadge(); renderList(); }

  // ---------- text model
  var SKIP = 'svg,script,style,button,.anchor,#quiz,.deck,#lightbox,.hl-ui,.seg,input,textarea,select';
  function nodes() {
    var out = [], w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!n.nodeValue) return NodeFilter.FILTER_REJECT;
        var p = n.parentElement;
        if (!p || p.closest(SKIP)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    }), n;
    while ((n = w.nextNode())) out.push(n);
    return out;
  }
  function fullText(ns) { return ns.map(function (n) { return n.nodeValue; }).join(''); }

  function unwrap() {
    root.querySelectorAll('mark.nbhl').forEach(function (m) {
      var p = m.parentNode; while (m.firstChild) p.insertBefore(m.firstChild, m); p.removeChild(m); p.normalize();
    });
  }

  function apply() {
    unwrap();
    if (!H.length) return;
    var ns = nodes(), txt = fullText(ns);
    // re-anchor if the text moved
    H.forEach(function (h) {
      if (txt.substr(h.s, h.e - h.s) === h.t) { h.lost = 0; return; }
      var best = -1, bd = 1e9, i = -1;
      while ((i = txt.indexOf(h.t, i + 1)) >= 0) {
        var pre = txt.substring(Math.max(0, i - (h.p || '').length), i), score = (pre === h.p ? 0 : 1e6) + Math.abs(i - h.s);
        if (score < bd) { bd = score; best = i; }
      }
      if (best >= 0) { h.s = best; h.e = best + h.t.length; h.lost = 0; } else h.lost = 1;
    });
    var acc = 0, spans = ns.map(function (n) { var s = { n: n, a: acc, b: acc + n.nodeValue.length }; acc = s.b; return s; });
    H.slice().sort(function (x, y) { return y.s - x.s; }).forEach(function (h) { // right to left keeps offsets valid
      if (h.lost) return;
      for (var i = spans.length - 1; i >= 0; i--) {
        var sp = spans[i];
        if (sp.b <= h.s || sp.a >= h.e) continue;
        var from = Math.max(h.s, sp.a) - sp.a, to = Math.min(h.e, sp.b) - sp.a;
        if (to <= from) continue;
        var r = document.createRange();
        r.setStart(sp.n, from); r.setEnd(sp.n, to);
        var m = document.createElement('mark');
        m.className = 'nbhl c-' + h.c; m.setAttribute('data-h', h.id);
        try { r.surroundContents(m); } catch (e) {}
      }
    });
  }

  // selection -> offsets
  function selectionOffsets(range) {
    var ns = nodes(), acc = 0, s = -1, e = -1;
    for (var i = 0; i < ns.length; i++) {
      var n = ns[i], len = n.nodeValue.length;
      if (range.intersectsNode(n)) {
        var a = n === range.startContainer ? range.startOffset : 0;
        var b = n === range.endContainer ? range.endOffset : len;
        if (b > a) { if (s < 0) s = acc + a; e = acc + b; }
      }
      acc += len;
    }
    return s >= 0 && e > s ? { s: s, e: e, txt: fullText(ns) } : null;
  }

  function newId() { return 'h' + Date.now().toString(36) + Math.random().toString(36).slice(2, 5); }

  function subtract(s, e) { // remove [s,e) from all highlights, keeping remnants
    var out = [];
    H.forEach(function (h) {
      if (h.e <= s || h.s >= e) { out.push(h); return; }
      if (h.s < s) { var l = clone(h); l.e = s; l.t = h.t.substr(0, s - h.s); out.push(l); }
      if (h.e > e) { var r = clone(h); r.id = newId(); r.s = e; r.t = h.t.substr(e - h.s); r.p = ''; out.push(r); }
    });
    H = out;
  }
  function clone(o) { return JSON.parse(JSON.stringify(o)); }

  function addHighlight(off, color) {
    subtract(off.s, off.e);
    var t = off.txt.substring(off.s, off.e);
    H.push({ id: newId(), s: off.s, e: off.e, c: color, t: t, p: off.txt.substring(Math.max(0, off.s - 24), off.s) });
    H.sort(function (a, b) { return a.s - b.s; });
    persist(); apply();
  }
  function eraseRange(off) { subtract(off.s, off.e); persist(); apply(); }

  // ---------- UI
  var css = document.createElement('style');
  css.textContent =
    'mark.nbhl{color:inherit;border-radius:3px;padding:0;-webkit-box-decoration-break:clone;box-decoration-break:clone;cursor:pointer;-webkit-print-color-adjust:exact;print-color-adjust:exact}' +
    COLORS.map(function (c) { return 'mark.nbhl.c-' + c.k + '{background:' + rgba(c.hex, .42) + '}'; }).join('') +
    '@media (prefers-color-scheme:dark){:root:not([data-theme]) mark.nbhl{filter:saturate(.9) brightness(1.05)}}' +
    ':root[data-theme=dark] mark.nbhl{filter:saturate(.9) brightness(1.05)}' +
    '.hl-ui{font:600 14px/1.2 system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#1d2a27;-webkit-user-select:none;user-select:none}' +
    '.hl-pop{position:fixed;z-index:100000;display:flex;gap:6px;align-items:center;padding:7px 9px;background:#fff;border:1px solid rgba(0,0,0,.18);border-radius:26px;box-shadow:0 6px 22px rgba(0,0,0,.28)}' +
    '.hl-pop[hidden],.hl-panel[hidden]{display:none}' +
    '.hl-dot{width:32px;height:32px;border-radius:50%;border:2px solid rgba(0,0,0,.18);cursor:pointer;padding:0;touch-action:manipulation}' +
    '.hl-dot:active{transform:scale(.9)}' +
    '.hl-tool{height:32px;min-width:32px;border-radius:16px;border:1px solid rgba(0,0,0,.2);background:#f3f1ea;cursor:pointer;padding:0 9px;font:inherit}' +
    '.hl-fab{position:fixed;right:14px;bottom:84px;z-index:99990;width:46px;height:46px;border-radius:50%;border:1px solid rgba(0,0,0,.2);background:#ffd60a;color:#1d2a27;font-size:21px;box-shadow:0 4px 14px rgba(0,0,0,.28);cursor:pointer;padding:0}' +
    '.hl-fab b{position:absolute;top:-6px;right:-6px;min-width:20px;height:20px;border-radius:10px;background:#1d2a27;color:#fff;font:700 11px/20px system-ui;text-align:center;padding:0 4px}' +
    '.hl-panel{position:fixed;z-index:99995;right:10px;bottom:140px;width:min(380px,calc(100vw - 20px));max-height:min(70vh,560px);display:flex;flex-direction:column;background:#fff;border:1px solid rgba(0,0,0,.18);border-radius:16px;box-shadow:0 10px 34px rgba(0,0,0,.32);overflow:hidden}' +
    '.hl-ph{display:flex;align-items:center;gap:8px;padding:10px 12px;border-bottom:1px solid rgba(0,0,0,.1)}.hl-ph strong{flex:1;font-size:15px}' +
    '.hl-chips{display:flex;gap:6px;padding:8px 12px;flex-wrap:wrap;border-bottom:1px solid rgba(0,0,0,.08)}' +
    '.hl-chip{border:2px solid transparent;border-radius:14px;padding:4px 9px;font:inherit;font-size:12px;cursor:pointer}.hl-chip[aria-pressed=true]{border-color:#1d2a27}' +
    '.hl-list{overflow:auto;padding:6px 8px;flex:1}.hl-item{display:flex;gap:8px;align-items:flex-start;padding:8px 6px;border-radius:10px;cursor:pointer;font-weight:500}.hl-item:hover{background:#f3f1ea}' +
    '.hl-item i{flex:none;width:12px;height:12px;border-radius:50%;margin-top:3px}.hl-item span{font-size:13.5px;line-height:1.4}.hl-item small{display:block;color:#7a6a3a;font-size:11px}' +
    '.hl-empty{padding:14px;color:#555;font-weight:500;font-size:13.5px;line-height:1.5}' +
    '.hl-foot{display:flex;gap:6px;flex-wrap:wrap;padding:8px 12px;border-top:1px solid rgba(0,0,0,.1)}' +
    '@media print{.hl-ui{display:none!important}}';
  document.head.appendChild(css);

  function rgba(hex, a) { var n = parseInt(hex.slice(1), 16); return 'rgba(' + (n >> 16) + ',' + ((n >> 8) & 255) + ',' + (n & 255) + ',' + a + ')'; }
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }

  // popup near selection or tapped highlight
  var pop = el('div', 'hl-ui hl-pop'); pop.hidden = true; pop.setAttribute('role', 'toolbar'); pop.setAttribute('aria-label', 'Highlight colours');
  COLORS.forEach(function (c) {
    var b = el('button', 'hl-dot'); b.type = 'button'; b.style.background = c.hex; b.title = c.name; b.setAttribute('aria-label', c.name); b.dataset.c = c.k; pop.appendChild(b);
  });
  var eraser = el('button', 'hl-tool', 'Erase'); eraser.type = 'button'; eraser.dataset.act = 'erase'; eraser.title = 'Remove highlight'; pop.appendChild(eraser);
  document.body.appendChild(pop);

  var target = null; // {off} for selection or {id} for tapped highlight
  function hidePop() { pop.hidden = true; target = null; }
  function showPopAt(rect) {
    pop.hidden = false;
    var w = pop.offsetWidth, h = pop.offsetHeight;
    var x = Math.min(Math.max(8, rect.left + rect.width / 2 - w / 2), window.innerWidth - w - 8);
    var y = rect.top - h - 10; if (y < 8) y = rect.bottom + 10;
    y = Math.max(8, Math.min(window.innerHeight - h - 8, y));
    pop.style.left = x + 'px'; pop.style.top = y + 'px';
  }
  ['pointerdown', 'mousedown', 'touchstart'].forEach(function (ev) { pop.addEventListener(ev, function (e) { e.preventDefault(); }, { passive: false }); });
  pop.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b || !target) return;
    if (target.id) {
      var h = H.filter(function (x) { return x.id === target.id; })[0];
      if (h) { if (b.dataset.act === 'erase') H = H.filter(function (x) { return x.id !== h.id; }); else h.c = b.dataset.c; persist(); apply(); }
    } else if (target.off) {
      if (b.dataset.act === 'erase') eraseRange(target.off); else addHighlight(target.off, b.dataset.c);
      var sel = window.getSelection(); if (sel) sel.removeAllRanges();
    }
    hidePop();
  });

  var selT = null;
  document.addEventListener('selectionchange', function () {
    clearTimeout(selT);
    selT = setTimeout(function () {
      var sel = window.getSelection();
      if (!sel || sel.isCollapsed || !sel.rangeCount) { if (target && target.off) hidePop(); return; }
      var r = sel.getRangeAt(0);
      if (!root.contains(r.commonAncestorContainer)) return;
      if (r.commonAncestorContainer.nodeType === 1 && r.commonAncestorContainer.closest && r.commonAncestorContainer.closest(SKIP)) return;
      var off = selectionOffsets(r); if (!off) return;
      target = { off: off };
      var rects = r.getClientRects(), rc = rects.length ? rects[0] : r.getBoundingClientRect();
      showPopAt(rc);
    }, 280);
  });
  document.addEventListener('click', function (e) {
    var m = e.target.closest && e.target.closest('mark.nbhl');
    var sel = window.getSelection();
    if (m && (!sel || sel.isCollapsed)) { target = { id: m.getAttribute('data-h') }; showPopAt(m.getBoundingClientRect()); return; }
    if (!e.target.closest('.hl-ui') && (!sel || sel.isCollapsed)) hidePop();
  });
  window.addEventListener('scroll', function () { if (target && target.id) hidePop(); }, { passive: true });

  // floating button and panel
  var fab = el('button', 'hl-ui hl-fab', '✎<b hidden>0</b>'); fab.type = 'button'; fab.title = 'My highlights'; fab.setAttribute('aria-label', 'My highlights');
  document.body.appendChild(fab);
  var panel = el('div', 'hl-ui hl-panel'); panel.hidden = true;
  panel.innerHTML = '<div class="hl-ph"><strong>Highlights on this page</strong><button class="hl-tool" type="button" data-a="close">Close</button></div>' +
    '<div class="hl-chips"></div><div class="hl-list"></div>' +
    '<div class="hl-foot"><button class="hl-tool" type="button" data-a="clear">Clear this page</button><button class="hl-tool" type="button" data-a="backup">Backup all</button><button class="hl-tool" type="button" data-a="restore">Restore</button><input type="file" accept="application/json" hidden></div>';
  document.body.appendChild(panel);
  var chips = panel.querySelector('.hl-chips'), list = panel.querySelector('.hl-list'), file = panel.querySelector('input'), filt = null;
  COLORS.forEach(function (c) {
    var b = el('button', 'hl-chip', c.name); b.type = 'button'; b.style.background = rgba(c.hex, .5); b.dataset.c = c.k; b.setAttribute('aria-pressed', 'false'); chips.appendChild(b);
  });
  chips.addEventListener('click', function (e) {
    var b = e.target.closest('.hl-chip'); if (!b) return;
    filt = filt === b.dataset.c ? null : b.dataset.c;
    chips.querySelectorAll('.hl-chip').forEach(function (x) { x.setAttribute('aria-pressed', x.dataset.c === filt ? 'true' : 'false'); });
    renderList();
  });
  function updateBadge() { var b = fab.querySelector('b'); b.textContent = H.length; b.hidden = !H.length; }
  function renderList() {
    var items = H.filter(function (h) { return !filt || h.c === filt; });
    if (!items.length) { list.innerHTML = '<div class="hl-empty">' + (H.length ? 'No highlights in this colour.' : 'Nothing highlighted yet. Select any text, then tap a colour. Tap a highlight later to change its colour or remove it.') + '</div>'; return; }
    list.innerHTML = '';
    items.forEach(function (h) {
      var cname = COLORS.filter(function (c) { return c.k === h.c; })[0], hex = cname.hex;
      var it = el('div', 'hl-item'); it.dataset.id = h.id;
      var t = h.t.length > 140 ? h.t.slice(0, 137) + '…' : h.t;
      it.innerHTML = '<i style="background:' + hex + '"></i><span></span>';
      it.querySelector('span').textContent = t;
      if (h.lost) { var s = el('small', '', 'Text changed; cannot place this highlight'); it.querySelector('span').appendChild(s); }
      list.appendChild(it);
    });
  }
  list.addEventListener('click', function (e) {
    var it = e.target.closest('.hl-item'); if (!it) return;
    var m = root.querySelector('mark.nbhl[data-h="' + it.dataset.id + '"]');
    if (m) { m.scrollIntoView({ behavior: 'smooth', block: 'center' }); m.style.outline = '3px solid #1d2a27'; setTimeout(function () { m.style.outline = ''; }, 1400); panel.hidden = true; }
  });
  fab.addEventListener('click', function () { panel.hidden = !panel.hidden; if (!panel.hidden) renderList(); });
  panel.addEventListener('click', function (e) {
    var b = e.target.closest('button[data-a]'); if (!b) return;
    var a = b.dataset.a;
    if (a === 'close') panel.hidden = true;
    if (a === 'clear') { if (H.length && confirm('Remove all ' + H.length + ' highlights on this page?')) { H = []; persist(); apply(); } }
    if (a === 'backup') {
      var blob = new Blob([JSON.stringify({ app: 'study-shelf-highlights', v: 1, data: ALL }, null, 1)], { type: 'application/json' });
      var u = URL.createObjectURL(blob), x = document.createElement('a'); x.href = u; x.download = 'study-shelf-highlights.json'; document.body.appendChild(x); x.click(); x.remove(); setTimeout(function () { URL.revokeObjectURL(u); }, 2000);
    }
    if (a === 'restore') file.click();
  });
  file.addEventListener('change', function () {
    var f = file.files[0]; if (!f) return;
    var rd = new FileReader();
    rd.onload = function () {
      try {
        var j = JSON.parse(rd.result), d = j && j.data; if (!d || typeof d !== 'object') throw 0;
        var cur = load(), n = 0;
        Object.keys(d).forEach(function (k) { // merge by id
          var have = {}; (cur[k] || []).forEach(function (h) { have[h.id] = 1; });
          (d[k] || []).forEach(function (h) { if (h && h.id && !have[h.id]) { (cur[k] = cur[k] || []).push(h); n++; } });
        });
        ALL = cur; saveAll(ALL); H = ALL[page] || []; updateBadge(); apply(); renderList(); alert('Restored ' + n + ' highlights.');
      } catch (e) { alert('That file is not a highlights backup.'); }
      file.value = '';
    };
    rd.readAsText(f);
  });

  updateBadge(); apply();
  window.addEventListener('load', function () { apply(); });
})();
