/* auto-update: keep the service worker fresh and reload once when a new version takes over */
(function(){if(!('serviceWorker' in navigator)||location.protocol.indexOf('http')!==0||window.__swAuto)return;window.__swAuto=1;
var had=!!navigator.serviceWorker.controller,done=false;
function go(){var a=document.activeElement,t=a&&a.tagName;if(t==='INPUT'||t==='TEXTAREA'||(a&&a.isContentEditable)){setTimeout(go,3000);return}location.reload()}
navigator.serviceWorker.addEventListener('controllerchange',function(){if(!had||done)return;done=true;go()});
navigator.serviceWorker.register('sw.js',{updateViaCache:'none'}).then(function(r){var u=function(){try{r.update()}catch(e){}};u();setInterval(u,60000);
document.addEventListener('visibilitychange',function(){if(!document.hidden)u()});window.addEventListener('online',u);window.addEventListener('focus',u)}).catch(function(){});
})();
