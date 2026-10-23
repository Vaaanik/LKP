
function sendForm(f){
  var d=new FormData(f);
  var body="Ім'я: "+d.get("name")+"\nТелефон: "+d.get("phone")+"\nАвто: "+d.get("car")+"\n\n"+(d.get("msg")||"");
  location.href="mailto:"+(window.__EMAIL||"")+"?subject="+encodeURIComponent("Оцінка ремонту ЛКП")+"&body="+encodeURIComponent(body);
  return false;
}
document.querySelectorAll("nav a").forEach(function(a){a.addEventListener("click",function(){document.body.classList.remove("menu")})});
