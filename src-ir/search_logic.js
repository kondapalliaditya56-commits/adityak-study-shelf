
(function(){var D=JSON.parse(document.getElementById('sdata').textContent),q=document.getElementById('q'),res=document.getElementById('res'),cnt=document.getElementById('cnt');
cnt.textContent=D.length+' sections indexed. Tables are images and are not searchable.';
function esc(s){return s.replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
function run(){var v=q.value.trim().toLowerCase();res.innerHTML='';if(v.length<2)return;var ts=v.split(/\s+/),n=0,h='';
for(var i=0;i<D.length&&n<40;i++){var d=D[i],tx=(d.t+' '+d.x).toLowerCase(),ok=ts.every(function(t){return tx.indexOf(t)>=0});if(!ok)continue;n++;
var p=tx.indexOf(ts[0]),s=Math.max(0,p-60),sn=d.x.substr(s,180);
h+='<div class="hit"><a href="geo-ch'+('0'+d.c).slice(-2)+'.html#'+d.id+'"><b>'+esc(d.t)+'</b></a><br><small>'+esc(d.n)+'</small><br>…'+esc(sn)+'…</div>'}
res.innerHTML=h||'<p class="prog">No matches.</p>'}
q.addEventListener('input',run)})();