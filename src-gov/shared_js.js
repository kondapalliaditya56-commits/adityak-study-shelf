/* Shared store: reading progress, preferences, optional cross-device sync. */
(function(){
var KEY='nbapp:v1',root=document.documentElement;
function today(){var d=new Date();return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2)}
function fresh(){return{v:1,prefs:{fs:1,lh:1.65,w:780,font:'serif',theme:'auto',pt:0},last:null,nb:{},days:{}}}
function lsGet(k){try{return localStorage.getItem(k)}catch(e){return null}}
function lsSet(k,v){try{localStorage.setItem(k,v)}catch(e){}}
var S;
try{S=JSON.parse(lsGet(KEY))}catch(e){S=null}
if(!S||!S.v)S=fresh();
S.prefs=Object.assign(fresh().prefs,S.prefs||{});
// one-time import of the older done list and theme
if(!S.migrated){
  try{var od=JSON.parse(lsGet('nb-done')||'[]');od.forEach(function(n){var c=chap('modern-india',n);c.done=1;c.dt=1})}catch(e){}
  var ot=lsGet('nb-theme');if(ot&&!S.prefs.pt){S.prefs.theme=ot;S.prefs.pt=1}
  S.migrated=1;
}
function chap(nb,n){var b=S.nb[nb]||(S.nb[nb]={});return b[n]||(b[n]={read:{},done:0,dt:0,pos:null,t:0})}
var listeners=[],dirty=false,saveT=null,syncT=null;
function save(){
  dirty=true;clearTimeout(saveT);
  saveT=setTimeout(function(){lsSet(KEY,JSON.stringify(S));listeners.forEach(function(f){try{f()}catch(e){}});scheduleSync()},250);
}
function flush(){lsSet(KEY,JSON.stringify(S))}
function merge(a,b){ // a local, b remote; returns merged
  var o=fresh();
  o.prefs=((b.prefs&&b.prefs.pt||0)>(a.prefs&&a.prefs.pt||0))?Object.assign({},a.prefs,b.prefs):Object.assign({},b.prefs,a.prefs);
  o.last=(!a.last||(b.last&&b.last.ts>a.last.ts))?b.last:a.last;
  o.migrated=1;
  var ids={};Object.keys(a.nb||{}).concat(Object.keys(b.nb||{})).forEach(function(k){ids[k]=1});
  Object.keys(ids).forEach(function(id){
    o.nb[id]={};var ca=(a.nb||{})[id]||{},cb=(b.nb||{})[id]||{},ks={};
    Object.keys(ca).concat(Object.keys(cb)).forEach(function(k){ks[k]=1});
    Object.keys(ks).forEach(function(k){
      var x=ca[k],y=cb[k];if(!x||!y){o.nb[id][k]=x||y;return}
      var r=Object.assign({},x.read,y.read),done=(y.dt||0)>(x.dt||0)?y:x,pos=(y.t||0)>(x.t||0)?y.pos:x.pos;
      o.nb[id][k]={read:r,done:done.done,dt:done.dt||0,pos:pos,t:Math.max(x.t||0,y.t||0)};
    });
  });
  var dk={};Object.keys(a.days||{}).concat(Object.keys(b.days||{})).forEach(function(k){dk[k]=1});
  Object.keys(dk).forEach(function(k){o.days[k]=Math.max((a.days||{})[k]||0,(b.days||{})[k]||0)});
  return o;
}
var syncState='off';
function scheduleSync(){clearTimeout(syncT);syncT=setTimeout(function(){sync()},4000)}
var dbp=null;
function getRef(){
  if(dbp)return dbp;
  dbp=(async function(){
    if(!window.claude||!claude.use)return null;
    var db=await claude.use('db'),u=await claude.use('user');
    if(!db||!u||!u.id)return null;
    var id=await u.id();if(!id)return null;
    return db.doc('data/users/'+id+'/nbapp');
  })().catch(function(){return null});
  return dbp;
}
var busy=false;
async function sync(){
  if(busy)return;busy=true;
  try{
    var ref=await getRef();if(!ref){syncState='local';return}
    var snap=await ref.get(),rem=null;
    if(snap.exists){var d=snap.data();try{rem=JSON.parse(d.state)}catch(e){}}
    var m=rem?merge(S,rem):S;
    var changed=JSON.stringify(m)!==JSON.stringify(S);
    S=m;
    if(changed){flush();listeners.forEach(function(f){try{f()}catch(e){}})}
    var out=JSON.stringify(S);
    if(!rem||JSON.stringify(rem)!==out)await ref.set({v:1,updated:Date.now(),state:out});
    syncState='synced';
  }catch(e){syncState='local'}
  finally{busy=false}
}
var API={
  get:function(){return S},
  chap:chap,
  save:save,flush:flush,sync:sync,
  onChange:function(f){listeners.push(f)},
  syncState:function(){return syncState},
  setPref:function(k,v){S.prefs[k]=v;S.prefs.pt=Date.now();applyPrefs();save()},
  reset:function(){S=fresh();S.migrated=1;flush();save()},
  today:today,
  pct:function(nb,n,total){var c=(S.nb[nb]||{})[n];if(!c||!total)return 0;var r=0;Object.keys(c.read||{}).forEach(function(k){if(c.read[k])r++});return Math.min(1,r/total)},
  isDone:function(nb,n,total){var c=(S.nb[nb]||{})[n];if(!c)return false;if(c.dt)return !!c.done;return false}
};
window.NBS=API;
function applyPrefs(){
  var p=S.prefs;
  var th=p.theme;
  if(th==='auto')root.removeAttribute('data-theme');else root.setAttribute('data-theme',th);
  root.style.setProperty('--zoom',p.fs);root.style.setProperty('--lh',p.lh);root.style.setProperty('--pw',p.w+'px');
  root.setAttribute('data-font',p.font);
}
API.applyPrefs=applyPrefs;applyPrefs();
// studied time, counted while the page is visible and touched in the last minute
var lastAct=Date.now();
['scroll','pointerdown','keydown','touchstart'].forEach(function(e){addEventListener(e,function(){lastAct=Date.now()},{passive:true})});
setInterval(function(){
  if(document.hidden||Date.now()-lastAct>60000||!window.__NB)return;
  var t=today();S.days[t]=(S.days[t]||0)+15;save();
},15000);
document.addEventListener('visibilitychange',function(){if(document.hidden){flush();sync()}else{sync()}});
addEventListener('pagehide',flush);
setTimeout(sync,800);
})();
(function(){var b=document.getElementById('themebtn');if(!b)return;var o=['auto','light','sepia','dark'];b.addEventListener('click',function(){var t=NBS.get().prefs.theme,i=(o.indexOf(t)+1)%o.length;NBS.setPref('theme',o[i]);b.textContent='Theme: '+o[i]})})();
(function(){
var D=JSON.parse(document.getElementById('data').textContent);
// map/outline toggle
document.querySelectorAll('.seg button').forEach(function(bt){bt.addEventListener('click',function(){var v=bt.dataset.v;document.querySelectorAll('.seg button').forEach(function(x){x.setAttribute('aria-pressed',x===bt)});document.getElementById('mm-map').hidden=v!=='map';document.getElementById('mm-outline').hidden=v!=='outline'})});
if(window.innerWidth<640){var ob=document.querySelector('.seg button[data-v="outline"]');if(ob)ob.click()}
// lightbox
var lb=document.getElementById('lightbox'),li=lb.querySelector('img');
document.querySelectorAll('a.zoom').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();li.src=a.getAttribute('href');lb.hidden=false})});
lb.addEventListener('click',function(){lb.hidden=true});document.addEventListener('keydown',function(e){if(e.key==='Escape')lb.hidden=true});
// quiz
var qz=document.getElementById('quiz'),score=document.getElementById('score'),right=0,answered=0;
if(qz)D.mcq.forEach(function(m,i){var d=document.createElement('div');d.className='q';var t=document.createElement('div');t.className='qt';t.textContent=(i+1)+'. '+m.q;d.appendChild(t);var ex=document.createElement('div');ex.className='ex';ex.hidden=true;ex.textContent=m.explain;var btns=[];
m.options.forEach(function(o,j){var b=document.createElement('button');b.type='button';b.className='opt';b.textContent='ABCD'[j]+'. '+o;b.addEventListener('click',function(){if(d.dataset.done)return;d.dataset.done=1;answered++;if(j===m.answer){right++;b.classList.add('right')}else{b.classList.add('wrong');btns[m.answer].classList.add('right')}ex.hidden=false;score.textContent=right+' / '+answered+' correct'});btns.push(b);d.appendChild(b)});d.appendChild(ex);qz.appendChild(d)});
// flashcards
var fc=document.getElementById('fc');
if(fc){var all=D.cards.map(function(c,i){return{q:c.q,a:c.a,i:i}}),deck=all.slice(),pos=0,back=false,missed={};
function show(){if(!deck.length){fc.textContent='No cards in this deck.';document.getElementById('fccount').textContent='';return}var c=deck[pos];fc.textContent=back?c.a:c.q;fc.classList.toggle('back',back);document.getElementById('fccount').textContent='Card '+(pos+1)+' of '+deck.length+(back?' (answer)':' (question)')}
function go(d){if(!deck.length)return;pos=(pos+d+deck.length)%deck.length;back=false;show()}
fc.addEventListener('click',function(){back=!back;show()});fc.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();back=!back;show()}});
document.getElementById('fcnext').onclick=function(){go(1)};document.getElementById('fcprev').onclick=function(){go(-1)};
document.getElementById('fcmiss').onclick=function(){if(deck.length){missed[deck[pos].i]=1;go(1)}};
document.getElementById('fcshuf').onclick=function(){for(var i=deck.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=deck[i];deck[i]=deck[j];deck[j]=t}pos=0;back=false;show()};
document.getElementById('fconlymiss').onclick=function(){deck=all.filter(function(c){return missed[c.i]});pos=0;back=false;show()};
document.getElementById('fcall').onclick=function(){deck=all.slice();pos=0;back=false;show()};show()}
// side toc highlight
var links=[].slice.call(document.querySelectorAll('.sidetoc a'));
if('IntersectionObserver' in window&&links.length){var map={};links.forEach(function(a){map[a.getAttribute('href').slice(1)]=a});var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){links.forEach(function(a){a.classList.remove('on')});var a=map[e.target.id];if(a)a.classList.add('on')}})},{rootMargin:'-70px 0px -70% 0px'});Object.keys(map).forEach(function(id){var el=document.getElementById(id);if(el)io.observe(el)})}
})();
(function(){
var N=window.__NB,S=window.NBS;if(!N||!S)return;
var root=document.documentElement,body=document.body;
var rec=function(){return S.chap(N.id,N.ch)};
var heads=[].slice.call(document.querySelectorAll('.page h2[id]'));
var titles=heads.map(function(h){return h.firstChild?h.firstChild.textContent.trim():h.id});
var ids=heads.map(function(h){return h.id});
var seen={},manual={};
// Done box
var box=document.getElementById('donebox');
if(box){box.checked=!!(rec().done);box.addEventListener('change',function(){var r=rec();r.done=box.checked?1:0;r.dt=Date.now();S.save()})}
// progress bar
var bar=document.createElement('div');bar.className='rbar';body.appendChild(bar);
// per-section read buttons
heads.forEach(function(h,i){
  var b=document.createElement('button');b.type='button';b.className='h2read';
  function paint(){var on=!!rec().read[h.id];b.setAttribute('aria-pressed',on);b.textContent=on?'Read ✓':'Mark read'}
  b.addEventListener('click',function(){var r=rec();manual[h.id]=1;if(r.read[h.id])delete r.read[h.id];else r.read[h.id]=1;r.t=Date.now();S.save();paint();refresh()});
  h.insertBefore(b,h.firstChild);paint();b._paint=paint;h._b=b;
});
function repaint(){heads.forEach(function(h){h._b._paint()});refresh()}
// caption clamp
document.querySelectorAll('figcaption').forEach(function(c){if(c.textContent.length>170){c.classList.add('clamp');c.addEventListener('click',function(){c.classList.toggle('open')})}});
// dock
var dock=document.createElement('div');dock.className='dock';
dock.innerHTML='<button type="button" id="dprev" aria-label="Previous section">‹ Prev</button><button type="button" class="mid" id="dmid"></button><button type="button" id="dnext" aria-label="Next section">Next ›</button>';
body.appendChild(dock);body.classList.add('has-dock');
var dmid=dock.querySelector('#dmid');
function curIdx(){var y=innerHeight*0.25,c=-1;for(var i=0;i<heads.length;i++){if(heads[i].getBoundingClientRect().top<=y)c=i;else break}return c}
function goto(i){if(i<0||i>=heads.length)return;heads[i].scrollIntoView({behavior:'smooth',block:'start'})}
dock.querySelector('#dprev').onclick=function(){var c=curIdx(),h=heads[c];goto(h&&h.getBoundingClientRect().top<-40?c:c-1)};
dock.querySelector('#dnext').onclick=function(){goto(curIdx()+1)};
function refresh(){
  var c=curIdx(),r=rec().read,n=0;ids.forEach(function(id){if(r[id])n++});
  dmid.innerHTML='<b>'+(c<0?'Top':(c+1)+'/'+heads.length)+'</b> · '+(c<0?'Start of chapter':esc(titles[c]))+' · '+n+' read';
}
function esc(s){return String(s).replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
// sheets
function sheet(html){var s=document.createElement('div');s.className='sheet';s.hidden=true;s.innerHTML='<div class="sheetin">'+html+'</div>';s.addEventListener('click',function(e){if(e.target===s)s.hidden=true});body.appendChild(s);return s}
var cs=sheet('<h3>Sections</h3><div class="secl" id="secl"></div>');
dmid.onclick=function(){
  var r=rec().read,c=curIdx(),h='';
  ids.forEach(function(id,i){h+='<a href="#'+id+'" data-i="'+i+'" class="'+(r[id]?'rd ':'')+(i===c?'cur':'')+'"><span class="tk">'+(r[id]?'✓':'')+'</span><span>'+esc(titles[i])+'</span></a>'});
  cs.querySelector('#secl').innerHTML=h;cs.hidden=false;
  var cur=cs.querySelector('.cur');if(cur)cur.scrollIntoView({block:'center'});
};
cs.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[data-i]');if(a){e.preventDefault();cs.hidden=true;goto(+a.dataset.i)}});
var ps=sheet('<h3>Reading settings</h3><div id="pbody"></div>');
function grp(key,label,opts){var p=S.get().prefs;return '<div class="srow"><label>'+label+'</label><div class="grp">'+opts.map(function(o){return '<button type="button" data-k="'+key+'" data-v="'+o[0]+'" aria-pressed="'+(String(p[key])===String(o[0]))+'">'+o[1]+'</button>'}).join('')+'</div></div>'}
function drawPrefs(){
  ps.querySelector('#pbody').innerHTML=
    grp('fs','Text size',[[0.88,"A−"],[1,"A"],[1.12,"A+"],[1.25,"A++"],[1.4,"A+++"]])+
    grp('lh','Spacing',[[1.45,'Tight'],[1.65,'Normal'],[1.85,'Roomy']])+
    grp('w','Width',[[640,'Narrow'],[780,'Medium'],[980,'Wide']])+
    grp('font','Font',[['serif','Serif'],['sans','Sans']])+
    grp('theme','Theme',[['auto','Auto'],['light','Light'],['sepia','Sepia'],['dark','Dark']])+
    '<div class="srow"><label>Extras</label><div class="grp"><button type="button" id="pfocus" aria-pressed="'+body.classList.contains('focus')+'">Focus mode</button>'+('wakeLock' in navigator?'<button type="button" id="pwake" aria-pressed="'+!!wl+'">Keep screen on</button>':'')+'</div></div>';
}
var wl=null;
ps.addEventListener('click',function(e){
  var b=e.target.closest&&e.target.closest('button');if(!b)return;
  if(b.dataset.k){var v=b.dataset.v;S.setPref(b.dataset.k,b.dataset.k==='font'||b.dataset.k==='theme'?v:+v);drawPrefs();return}
  if(b.id==='pfocus'){body.classList.toggle('focus');drawPrefs();return}
  if(b.id==='pwake'){
    if(wl){wl.release();wl=null;drawPrefs()}else{navigator.wakeLock.request('screen').then(function(l){wl=l;l.addEventListener('release',function(){wl=null});drawPrefs()}).catch(function(){})}
  }
});
function openPrefs(){drawPrefs();ps.hidden=false}
var aa=document.getElementById('aabtn');if(aa)aa.onclick=openPrefs;
document.addEventListener('keydown',function(e){if(e.key==='Escape'){ps.hidden=true;cs.hidden=true;body.classList.remove('focus')}});
// focus-mode exit: tap the top edge area
var fx=document.createElement('button');fx.type='button';fx.textContent='Exit focus';fx.className='h2read';fx.style.cssText='position:fixed;right:10px;top:10px;z-index:45;float:none;display:none';fx.onclick=function(){body.classList.remove('focus')};body.appendChild(fx);
new MutationObserver(function(){fx.style.display=body.classList.contains('focus')?'block':'none'}).observe(body,{attributes:true,attributeFilter:['class']});
// scroll handling
var tick=false,saveAt=0;
function onScroll(){
  if(tick)return;tick=true;requestAnimationFrame(function(){
    tick=false;
    var doc=document.documentElement,max=doc.scrollHeight-innerHeight;
    bar.style.width=(max>0?Math.min(100,scrollY/max*100):0)+'%';
    var vh=innerHeight,r=rec(),ch=false;
    heads.forEach(function(h,i){
      var t=h.getBoundingClientRect().top;
      if(t<vh&&t>-40)seen[h.id]=1;
      var nt=i+1<heads.length?heads[i+1].getBoundingClientRect().top:(scrollY>=max-160?-1:1e9);
      if(seen[h.id]&&nt<vh*0.35&&!r.read[h.id]&&!manual[h.id]){r.read[h.id]=1;ch=true;h._b._paint()}
    });
    if(ch){r.t=Date.now();S.save()}
    refresh();
    var now=Date.now();
    if(now-saveAt>1500){saveAt=now;var c=curIdx(),rr=rec();
      if(c>=0){var hh=heads[c].getBoundingClientRect().top;rr.pos={s:ids[c],o:Math.round(-hh)};rr.t=now}
      S.get().last={nb:N.id,ch:N.ch,s:c>=0?ids[c]:'',st:c>=0?titles[c]:'',ts:now};S.save()}
  })}
addEventListener('scroll',onScroll,{passive:true});addEventListener('resize',onScroll);
S.onChange(function(){if(box)box.checked=!!rec().done;repaint()});
refresh();onScroll();
// resume offer
var p=rec().pos;
if(!location.hash&&p&&p.s&&ids.indexOf(p.s)>0){
  var el=document.getElementById(p.s);
  var t=document.createElement('div');t.className='toast';t.innerHTML='<span>Resume at “'+esc(titles[ids.indexOf(p.s)])+'”?</span><button type="button" id="tgo">Resume</button><button type="button" id="tx">Dismiss</button>';
  body.appendChild(t);
  t.querySelector('#tgo').onclick=function(){if(el){el.scrollIntoView({block:'start'});scrollBy(0,(p.o||0))}t.remove()};
  t.querySelector('#tx').onclick=function(){t.remove()};
  setTimeout(function(){if(t.parentNode)t.remove()},12000);
}
})();
