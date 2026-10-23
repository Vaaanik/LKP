(function(){
  var d=document, root=d.documentElement;
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  // меню
  var b=d.querySelector('.burger');
  if(b){
    b.addEventListener('click',function(){
      var open=d.body.classList.toggle('menu');
      b.setAttribute('aria-expanded',open?'true':'false');
    });
    d.querySelectorAll('nav.main a').forEach(function(a){a.addEventListener('click',function(){d.body.classList.remove('menu');b.setAttribute('aria-expanded','false');});});
  }

  // лабораторія кольору: вибір кольору
  var name=d.getElementById('colname');
  d.querySelectorAll('.sw input').forEach(function(i){
    i.addEventListener('change',function(){
      root.style.setProperty('--paint',i.value);
      if(name) name.textContent=i.getAttribute('data-name');
    });
  });

  // до / після
  d.querySelectorAll('.ba').forEach(function(ba){
    var r=ba.querySelector('.ba-range');
    if(!r) return;
    function set(v){ba.style.setProperty('--pos',v+'%');}
    r.addEventListener('input',function(){set(r.value);});
    set(r.value);
    if(!reduce && ba.hasAttribute('data-intro')){
      var from=94,to=50,t0=null,dur=1500;
      r.value=from;set(from);
      function step(t){
        if(t0===null) t0=t;
        var p=Math.min((t-t0)/dur,1), e=1-Math.pow(1-p,3), v=from+(to-from)*e;
        r.value=v;set(v);
        if(p<1) requestAnimationFrame(step);
      }
      setTimeout(function(){requestAnimationFrame(step);},500);
    }
  });

  // вкладки
  d.querySelectorAll('[role=tablist]').forEach(function(list){
    var tabs=[].slice.call(list.querySelectorAll('[role=tab]'));
    function show(t,focus){
      tabs.forEach(function(x){
        var sel=x===t;
        x.setAttribute('aria-selected',sel?'true':'false');
        x.tabIndex=sel?0:-1;
        var p=d.getElementById(x.getAttribute('aria-controls'));
        if(p) p.hidden=!sel;
      });
      if(focus) t.focus();
    }
    tabs.forEach(function(t,i){
      t.addEventListener('click',function(){show(t,false);});
      t.addEventListener('keydown',function(e){
        var k=e.key, n=null;
        if(k==='ArrowDown'||k==='ArrowRight') n=tabs[(i+1)%tabs.length];
        if(k==='ArrowUp'||k==='ArrowLeft') n=tabs[(i-1+tabs.length)%tabs.length];
        if(k==='Home') n=tabs[0];
        if(k==='End') n=tabs[tabs.length-1];
        if(n){e.preventDefault();show(n,true);}
      });
    });
  });

  // фільтр блогу
  var fb=d.querySelectorAll('.chipb');
  if(fb.length){
    fb.forEach(function(c){
      c.addEventListener('click',function(){
        fb.forEach(function(x){x.setAttribute('aria-pressed',x===c?'true':'false');});
        var tag=c.getAttribute('data-tag');
        d.querySelectorAll('.post').forEach(function(p){
          p.hidden = !(tag==='all' || p.getAttribute('data-tag')===tag);
        });
      });
    });
  }
})();

function sendForm(f){
  var d=new FormData(f);
  var body="Ім'я: "+d.get("name")+"\nТелефон: "+d.get("phone")+"\nАвто: "+d.get("car")+"\n\n"+(d.get("msg")||"");
  location.href="mailto:"+(window.__EMAIL||"")+"?subject="+encodeURIComponent("Оцінка ремонту ЛКП")+"&body="+encodeURIComponent(body);
  return false;
}
