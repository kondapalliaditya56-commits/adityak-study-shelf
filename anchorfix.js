/* Study Shelf: when a link opens a page at a section (#anchor), keep that section in view while the page's
   lazy images load and shift the layout. Stops as soon as you touch, scroll or press a key. */
(function () {
  'use strict';
  var h = location.hash; if (h.length < 2) return;
  var id; try { id = decodeURIComponent(h.slice(1)); } catch (e) { id = h.slice(1); }
  var stop = false, ticks = 0, timer = null;
  ['wheel', 'touchstart', 'keydown', 'pointerdown', 'mousedown'].forEach(function (ev) { addEventListener(ev, function () { stop = true; }, { passive: true, once: true }); });
  function align() {
    if (stop) return;
    var e = document.getElementById(id); if (!e) return;
    var m = parseFloat(getComputedStyle(e).scrollMarginTop) || 70, d = e.getBoundingClientRect().top - m;
    if (Math.abs(d) > 6) window.scrollTo({ top: window.scrollY + d, behavior: 'instant' });
  }
  function run() {
    if (timer) return;
    timer = setInterval(function () { align(); if (stop || ++ticks > 30) { clearInterval(timer); } }, 200);
    align();
  }
  document.addEventListener('load', function (e) { if (e.target && e.target.tagName === 'IMG') align(); }, true);
  if (document.readyState === 'complete') run(); else { addEventListener('load', run); setTimeout(run, 300); }
})();
