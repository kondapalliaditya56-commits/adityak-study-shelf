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

(function(){var S=NBS;function upd(){var done=0;document.querySelectorAll('a.chcard[data-ch]').forEach(function(a){var n=+a.dataset.ch,t=+a.dataset.secs,p=S.pct('geography',n,t),rec=(S.get().nb.geography||{})[n],d=rec&&rec.dt?!!rec.done:p>=.999;var bar=a.querySelector('.cbar i');if(bar)bar.style.width=Math.round(p*100)+'%';var tk=a.querySelector('.tick');if(tk)tk.hidden=!d;if(d&&n>0)done++});var el=document.getElementById('progress');if(el)el.textContent=done}upd();S.onChange(upd);setTimeout(upd,2500)})();
