# -*- coding: utf-8 -*-
import os, shutil, json, datetime
from articles import ARTICLES

HERE = os.path.dirname(os.path.abspath(__file__))

# ====== НАЛАШТУВАННЯ ======
BRAND = "Точний Тон"
TAGLINE = "Локальний ремонт ЛКП та детейлінг для преміальних авто"
CITY = "Кривий Ріг"
CITY_LOC = "Кривому Розі"
DOMAIN = "https://vaaanik.github.io/LKP"
PHONE_DISPLAY = "+38 (095) 590-88-08"
PHONE_TEL = "+380955908808"
TELEGRAM = "https://t.me/+380955908808"
VIBER = "viber://chat?number=%2B380955908808"
EMAIL = "v2394454@gmail.com"
ADDRESS = "м. Кривий Ріг, Дніпропетровська область"
HOURS = "Пн–Сб: 09:00–19:00"
OUT = "/home/claude/site"
# ==========================

MONTHS = ["січня","лютого","березня","квітня","травня","червня","липня","серпня","вересня","жовтня","листопада","грудня"]
def fdate(s):
    d = datetime.date.fromisoformat(s)
    return f"{d.day} {MONTHS[d.month-1]} {d.year}"

LOGO = ('<svg class="logo" viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="17.5" fill="none" stroke="#CDB48A" stroke-width="1.4"/>'
        '<circle cx="20" cy="20" r="4.6" fill="#CDB48A"/><path d="M20 1.5v7M20 31.5v7M1.5 20h7M31.5 20h7" stroke="#CDB48A" stroke-width="1.2" stroke-linecap="round"/></svg>')

NAV = [("uslugy.html","Послуги"),("tsiny.html","Ціни"),("yak-ce-pratsyuye.html","Як працюємо"),
       ("materialy.html","Матеріали"),("blog/index.html","Блог"),("kontakty.html","Контакти")]
FOOT_MORE = [("pro-nas.html","Про нас"),("blog/index.html","Блог"),("kontakty.html","Контакти")]

SWATCHES = [("#ECEAE4","Білий перламутр"),("#0E0F12","Чорний металік"),("#4A515C","Графіт"),("#B9C0C9","Срібло"),
            ("#1B2A4A","Темно-синій"),("#6E1420","Бордо"),("#1F4A3A","Британський зелений"),("#8A6A4A","Бронза")]

# ---------- розрізи покриття ----------
BGX = "#1C1F24"
def _notch(cx, depth, w, fill=BGX):
    pts = [(cx-w,78),(cx-w*0.5,(78+depth)/2-4),(cx-w*0.12,depth),(cx+w*0.3,depth-5),(cx+w*0.55,(78+depth)/2+3),(cx+w,78)]
    return " ".join(f"{x:.1f},{y:.1f}" for x,y in pts)

def xsection(kind):
    metal = "#5E6978"; sub_label = "Метал"
    if kind == "bumper": metal = "#454B58"; sub_label = "Пластик"
    top = 78
    s = ['<svg viewBox="0 40 470 190" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="__ALT__">']
    # шари
    s.append(f'<rect x="16" y="78" width="336" height="28" fill="#B9C6DD"/>')
    s.append(f'<rect x="16" y="106" width="336" height="32" style="fill:var(--paint)"/>')
    s.append(f'<rect x="16" y="138" width="336" height="22" fill="#7C8594"/>')
    s.append(f'<rect x="16" y="160" width="336" height="54" fill="{metal}"/>')
    alt = ""
    cx = 183
    if kind == "skol":
        alt = "Розріз покриття: скол пройшов крізь лак, фарбу й ґрунт до металу, на металі видно корозію"
        s.append(f'<polygon points="{_notch(cx,170,17)}" fill="{BGX}"/>')
        s.append(f'<circle cx="{cx-5}" cy="167" r="3.2" fill="#B5532A"/><circle cx="{cx+6}" cy="169" r="2.6" fill="#B5532A"/>')
    elif kind == "scratch":
        alt = "Розріз покриття: ліворуч поверхнева подряпина тільки в лаку, праворуч глибока подряпина до ґрунту"
        s.append(f'<polygon points="{_notch(105,98,6)}" fill="{BGX}"/>')
        s.append(f'<polygon points="{_notch(262,148,6)}" fill="{BGX}"/>')
        s.append('<text x="105" y="62" text-anchor="middle" font-size="12.5" fill="#EDE9E2" font-weight="600">лак</text>')
        s.append('<text x="262" y="62" text-anchor="middle" font-size="12.5" fill="#EDE9E2" font-weight="600">до ґрунту</text>')
    elif kind == "paint":
        alt = "Розріз покриття: пошкоджена зона заново заповнена ґрунтом, фарбою й лаком"
        poly = _notch(cx,170,26)
        s.append(f'<defs><clipPath id="nc"><polygon points="{poly}"/></clipPath></defs>')
        s.append(f'<g clip-path="url(#nc)"><rect x="100" y="138" width="170" height="40" fill="#8E96A5"/><rect x="100" y="106" width="170" height="32" style="fill:var(--paint)"/><rect x="100" y="78" width="170" height="28" fill="#B9C6DD"/></g>')
        s.append(f'<polygon points="{poly}" fill="none" stroke="#CDB48A" stroke-width="1.4" stroke-dasharray="4 3"/>')
        s.append(f'<text x="{cx}" y="62" text-anchor="middle" font-size="12.5" fill="#EDE9E2" font-weight="600">нові шари</text>')
    elif kind == "bumper":
        alt = "Розріз бампера: пластикова основа, задир із втратою фарби до пластика"
        s.append(f'<polygon points="{_notch(cx,166,20)}" fill="{BGX}"/>')
    elif kind == "polish":
        alt = "Розріз покриття: дрібні подряпини на поверхні лаку, пунктиром позначено тонкий шар, який знімається поліруванням"
        for x in (60,110,150,205,250,300):
            s.append(f'<polygon points="{_notch(x,86,3.2)}" fill="{BGX}"/>')
        s.append('<line x1="16" y1="88" x2="352" y2="88" stroke="#CDB48A" stroke-width="1.4" stroke-dasharray="5 4"/>')
        s.append('<text x="16" y="62" font-size="12.5" fill="#EDE9E2" font-weight="600">пунктир: тонкий шар лаку, що знімається</text>')
    elif kind == "protect":
        alt = "Розріз покриття: поверх лаку нанесено тонкий захисний шар"
        s.append('<rect x="16" y="70" width="336" height="8" fill="#CDB48A"/>')
    s.append(f'<rect x="16" y="78" width="336" height="0.0" fill="none"/>')
    # підписи
    labels = [(92,"Лак"),(122,"Фарба (база)"),(149,"Ґрунт"),(187,sub_label)]
    if kind == "protect": labels = [(74,"Захист")] + [(y+2,t) for y,t in labels]
    for y,t in labels:
        s.append(f'<line x1="354" y1="{y}" x2="362" y2="{y}" stroke="#9C9890" stroke-width="1.2"/>')
        s.append(f'<text x="368" y="{y+4.5}" font-size="13" fill="#EDE9E2">{t}</text>')
    s.append('</svg>')
    return "".join(s).replace("__ALT__", alt)

SERVICES = [
 dict(id="skoly", tab="Сколи", small="від 1 500 ₴", kind="skol",
      h="Скол доходить до металу — і починається корозія",
      p="Вода потрапляє в оголений метал, і за кілька тижнів навколо скола з'являється бульбашка. Очищаємо, за потреби обробляємо метал, заповнюємо кратер ґрунтом, базою та лаком і вирівнюємо поверхню до рівня заводської.",
      spec=[("Ціна","від 1 500 ₴"),("Час","3–4 год"),("Обсяг","до 3 сколів на деталі")],
      link=("blog/skol-na-kapoti-koroziya.html","Чому не варто чекати до весни")),
 dict(id="podryapyny", tab="Подряпини", small="від 2 500 ₴", kind="scratch",
      h="Ніготь не чіпляється — це лак. Чіпляється — глибше",
      p="Поверхневу подряпину прибираємо поліруванням: так зберігається максимум заводського лаку. Глибоку, до ґрунту чи металу, поліруванням не зняти, а знімати лак до нуля небезпечно, тому фарбуємо локально. Що підходить вашому випадку, скажемо на огляді.",
      spec=[("Полірування","від 2 500 ₴"),("Локальне фарбування","від 5 000 ₴"),("Час","1–2 год або 1 день")],
      link=("blog/podryapina-polirovka-chy-farbuvannya.html","Полірування чи фарбування")),
 dict(id="farbuvannya", tab="Локальне фарбування", small="від 5 000 ₴", kind="paint",
      h="Фарбуємо тільки пошкоджену зону, не всю деталь",
      p="Видаляємо пошкоджене покриття, відновлюємо ґрунт, наносимо базу в колір кузова з плавним переходом і закриваємо лаком. Заводська фарба навколо зони лишається недоторканою. Якщо пошкодження велике, чесно скажемо, що краще перефарбувати елемент.",
      spec=[("Локальна зона","від 5 000 ₴"),("Елемент повністю","від 12 000 ₴"),("Час","1 день")],
      link=("blog/lokalne-farbuvannya-yak-pratsyuye.html","Як це працює крок за кроком")),
 dict(id="bampery", tab="Бампери", small="від 6 000 ₴", kind="bumper",
      h="Пластик ремонтуємо іншими матеріалами, ніж метал",
      p="Потертості від бордюрів, задири, невеликі тріщини. Використовуємо адгезійні ґрунти для пластика й еластичні склади, щоб фарба трималась. Якщо бампер розколотий, підкажемо, що вигідніше: ремонт чи заміна.",
      spec=[("Ціна","від 6 000 ₴"),("Час","1 день")],
      link=("blog/remont-bampera-plastyk.html","Ремонт чи заміна")),
 dict(id="polirovanya", tab="Полірування", small="від 1 200 ₴", kind="polish",
      h="Знімаємо тонкий шар лаку, щоб вирівняти поверхню",
      p="Прибирає «павутинку» від мийок, дрібні подряпини й матовість. Перед роботою вимірюємо товщину покриття, щоб не зняти зайвого. Глибокі подряпини, сколи й облізання лаку поліруванням не лікуються.",
      spec=[("Елемент","від 1 200 ₴"),("Освіжаюче, весь кузов","від 6 000 ₴"),("Відновлювальне","від 10 000 ₴")],
      link=("blog/vidnovlyuvalne-poliruvannya.html","Що вміє полірування")),
 dict(id="zakhyst", tab="Захист", small="від 800 ₴", kind="protect",
      h="Захист після ремонту: віск, кварц, кераміка, антидощ",
      p="Свіжий лак потребує кількох тижнів, щоб повністю затвердіти, тому захист наносимо за нашою рекомендацією. Антидощ на скло можна наносити будь-коли.",
      spec=[("Антидощ","від 800 ₴"),("Віск","від 2 000 ₴"),("Кварц, кераміка","від 8 000 ₴")],
      link=("blog/zakhyst-pislya-remontu.html","Віск, кварц чи кераміка")),
]

PRICES = [
 ("Сколи та подряпини", [
  ("Усунення сколів", "до 3 сколів на одній деталі", "від 1 500 ₴", "3–4 год"),
  ("Усунення подряпин поліруванням", "поверхневі, без глибоких пошкоджень", "від 2 500 ₴", "1–2 год"),
  ("Усунення глибокої подряпини", "локальне фарбування зони", "від 5 000 ₴", "1 день")]),
 ("Локальне та повне фарбування", [
  ("Локальне фарбування", "ділянка до ~15×15 см", "від 5 000 ₴", "1 день"),
  ("Фарбування елемента кузова", "матеріали включено у вартість", "від 12 000 ₴", "1–2 дні"),
  ("Ремонт і фарбування бампера", "пластик, потертості, задири", "від 6 000 ₴", "1 день")]),
 ("Полірування", [
  ("Освіжаюче полірування кузова", "дрібні подряпини, блиск", "від 6 000 ₴", "1 день"),
  ("Відновлювальне полірування кузова", "середні подряпини, «павутинка»", "від 10 000 ₴", "1–2 дні"),
  ("Полірування окремого елемента", "двері, капот, крило", "від 1 200 ₴", "1–2 год")]),
 ("Захист", [
  ("Антидощ на скло", "лобове або бокові скла", "від 800 ₴", "30–60 хв"),
  ("Віск на кузов", "блиск і легка гідрофобність", "від 2 000 ₴", "2–3 год"),
  ("Кварцеве / керамічне покриття", "залежить від покриття та авто", "від 8 000 ₴", "1–2 дні")]),
]

MATERIALS = [
 ("Лаки та ґрунти", "Акрилові лаки, швидкосохнучі ґрунти, адгезійні ґрунти для пластика і металу.", "Visman, Mipa, Carbo"),
 ("Полірування", "Полірувальні пасти, пади різної жорсткості, очисники поверхні.", "RUPES, LeadMax, Work Stuff, Visman"),
 ("Захисні покриття", "Віск, кварцові й нанокерамічні покриття, антидощ для скла.", "Nasiol, Soft99, K2, CoatPlus"),
 ("Нанесення фарби", "Професійні фарбопульти для рівного нанесення.", "Anest Iwata"),
 ("Підготовка", "Знежирювачі, розчинники, маскувальні матеріали, шпаклівки.", "різні виробники"),
 ("Герметики та клеї", "Шовні герметики й клеї для відновлення швів.", "Teroson та ін."),
]
BRANDS = ["Visman","Mipa","Carbo","RUPES","LeadMax","Nasiol","Soft99","K2","Anest Iwata","Teroson"]

DAY = [("09:00","Приймання й огляд","Оцінюємо глибину, називаємо ціну й час, уточнюємо код фарби."),
       ("09:30","Підготовка","Мийка, знежирення, маскування. Шліфуємо зону ремонту з плавними краями."),
       ("11:00","Ґрунт і колір","Захищаємо метал, готуємо фарбу за кодом, звіряємо зразок при денному світлі."),
       ("13:00","Фарба й лак","Наносимо базу, розтушовуємо перехід, закриваємо лаком."),
       ("14:30","Сушіння","Швидкосохнучі матеріали та інфрачервоне сушіння."),
       ("16:00","Полірування","Вирівнюємо поверхню, повертаємо блиск."),
       ("17:30","Видача","Показуємо результат при денному світлі, пояснюємо догляд.")]

FAQ = [
 ("Скільки триває ремонт?","Сколи, подряпини й невеликі ділянки зазвичай робимо за один день: привезли зранку, забрали ввечері. Цілу деталь, складні кольори (перламутр, тришарові) можуть потребувати 1–2 днів. Скажемо заздалегідь."),
 ("Чи збігатиметься колір?","Колір готуємо за кодом виробника і звіряємо зразок із вашим авто при денному світлі. Для складних кольорів і вигорілих авто ширше розтушовуємо перехід, щоб межу ремонту не було видно."),
 ("Чому ціна «від»?","Вартість залежить від розміру, глибини пошкодження, кольору та матеріалу деталі. У прайсі вказана мінімальна ціна роботи. Точну вартість називаємо після огляду, до початку робіт."),
 ("Чи можна мити авто після ремонту?","Перші кілька днів не мийте. Коли можна, скажемо під час видачі. Перший місяць уникайте автоматичних мийок зі щітками, а віск і захисні покриття на ремонтну ділянку наносьте після повного затвердіння лаку."),
 ("Ви працюєте з пластиком?","Так. Бампери й інші пластикові деталі ремонтуємо з адгезійними ґрунтами та еластичними складами. Якщо деталь розколота на кілька частин, підкажемо, що вигідніше: ремонт чи заміна."),
 ("Як дізнатися ціну без візиту?","Надішліть у Telegram чи Viber 2–3 фото (загальний план деталі й крупний план пошкодження), марку, модель і колір авто. Дамо вилку цін і запропонуємо час на огляд. Огляд безкоштовний."),
]

# ---------- шаблони ----------
def head(title, desc, root, path, extra=""):
    canon = f"{DOMAIN}/{path}"
    return f'''<!doctype html>
<html lang="uk"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0B0C0E">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:type" content="website"><meta property="og:locale" content="uk_UA"><meta property="og:url" content="{canon}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Onest:wght@300;400;500&display=swap&subset=cyrillic" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/style.css">
{extra}
</head><body><a class="skip" href="#main">До змісту</a>'''

def header(root, active):
    links = "".join(f'<a href="{root}{h}"{" aria-current=page" if h==active else ""}>{t}</a>' for h,t in NAV)
    return f'''<header class="top"><div class="wrap bar">
<a class="brand" href="{root}index.html" aria-label="{BRAND}, на головну">{LOGO}<span><b>{BRAND}</b><small>ремонт ЛКП та детейлінг</small></span></a>
<nav class="main" id="nav" aria-label="Основна навігація">{links}</nav>
<a class="btn pri sm" href="tel:{PHONE_TEL}" style="margin-left:8px" id="hdr-call">Записатися</a>
<button class="burger" aria-label="Меню" aria-expanded="false" aria-controls="nav">Меню</button>
</div></header><main id="main">'''

def cta(root):
    return f'''<section class="cta"><div class="wrap cta-in"><div><h2>Покажіть нам скол або подряпину</h2>
<p>Надішліть 2–3 фото та дані авто. Скажемо, чи вистачить локального ремонту, і назвемо вартість до початку робіт.</p></div>
<div class="btns" style="margin:0"><a class="btn pri" href="{TELEGRAM}">Написати в Telegram</a><a class="btn sec" href="{VIBER}">Viber</a><a class="btn sec" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></div></div></section>'''

def footer(root):
    mk = lambda items: "".join(f'<a href="{root}{h}">{t}</a>' for h,t in items)
    return f'''</main><footer class="foot"><div class="wrap fgrid">
<div><a class="brand" href="{root}index.html">{LOGO}<span><b>{BRAND}</b><small>ремонт ЛКП та детейлінг</small></span></a>
<p style="margin-top:16px">{TAGLINE}. Зберігаємо заводську фарбу: усуваємо сколи й подряпини локально.</p></div>
<div><h4>Послуги</h4>{mk(NAV[:3])}</div>
<div><h4>Сайт</h4>{"".join(f'<a href="{root}{h}">{t}</a>' for h,t in [("materialy.html","Матеріали")]+FOOT_MORE)}</div>
<div><h4>Контакти</h4><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><a href="{TELEGRAM}">Telegram</a><a href="{VIBER}">Viber</a><a href="mailto:{EMAIL}">{EMAIL}</a><span>{ADDRESS}</span><span>{HOURS}</span></div>
</div><div class="wrap legal">© {BRAND}, {CITY}. Ціни орієнтовні; остаточну вартість називаємо після огляду.</div></footer>
<div class="dock"><a class="btn pri" href="tel:{PHONE_TEL}">Зателефонувати</a><a class="btn sec" href="{TELEGRAM}">Telegram</a></div>
<script src="{root}assets/main.js"></script></body></html>'''

def page(fname, title, desc, body, active=None, extra="", with_cta=True):
    root = "../" * fname.count("/")
    html = head(title, desc, root, fname, extra) + header(root, active or fname) \
         + body.replace("{{root}}", root) + (cta(root) if with_cta else "") + footer(root)
    p = os.path.join(OUT, fname)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(html)

def page_head(h1, lead=""):
    return f'<section class="s tight"><div class="wrap"><h1 style="font-size:clamp(32px,4.6vw,56px)">{h1}</h1>{f"<p class=lead>{lead}</p>" if lead else ""}</div></section>'

def prices_html(groups):
    out = ""
    for g, rows in groups:
        out += f'<h2 class="pgroup">{g}</h2><div class="rows">'
        for n, d, p, t in rows:
            out += f'<div class="row"><div><b>{n}</b><span>{d}</span></div><div class="t">{t}</div><div class="p">{p}</div></div>'
        out += '</div>'
    return out

def post_rows(arts, tagged=False):
    return "".join(f'<a class="post" href="{{{{root}}}}blog/{a["slug"]}.html" data-tag="{a["tag"]}"><time datetime="{a["date"]}">{fdate(a["date"])}</time><div><span class="tagc">{a["tag"]}</span><h3>{a["title"]}</h3><p>{a["desc"]}</p></div><span class="m">{a["min"]} хв</span></a>' for a in arts)

def lab():
    sw = "".join(f'<label class="sw"><input type="radio" name="paint" value="{h}" data-name="{n}"{" checked" if h=="#1B2A4A" else ""} aria-label="{n}"><span style="--c:{h}"></span></label>' for h,n in SWATCHES)
    def panel(cls, dmg=""):
        return f'<div class="panel {cls}" aria-hidden="true"><div class="glass"></div><div class="gap"></div><div class="shoulder"></div><div class="handle-d"></div>{dmg}</div>'
    dmg = ('<span class="scratch" style="left:10%;top:62%;width:34%;transform:rotate(-12deg)"></span>'
           '<span class="scratch" style="left:22%;top:78%;width:24%;transform:rotate(7deg)"></span>'
           '<span class="scratch" style="left:31%;top:56%;width:13%;transform:rotate(-34deg)"></span>'
           '<span class="scratch" style="left:62%;top:68%;width:24%;transform:rotate(-9deg)"></span>'
           '<span class="chip" style="left:13%;top:52%"></span><span class="chip" style="left:36%;top:66%"></span>'
           '<span class="chip" style="left:25%;top:50%"></span><span class="chip" style="left:41%;top:78%"></span>'
           '<span class="chip" style="left:74%;top:52%"></span><span class="chip" style="left:84%;top:74%"></span>')
    return f'''<figure class="lab">
<div class="ba" data-intro style="--pos:50%">
{panel("after")}{panel("before", dmg)}
<span class="tag l">До</span><span class="tag r">Після</span>
<input class="ba-range" type="range" min="0" max="100" value="50" step="0.5" aria-label="Порівняння: до та після ремонту">
<div class="knob-line" aria-hidden="true"><div class="knob"></div></div>
</div>
<figcaption><span>Ілюстрація: двері авто, колір <b id="colname">Темно-синій</b></span><span>Тягніть повзунок</span></figcaption>
<fieldset class="swatches"><legend>Оберіть колір свого авто</legend>{sw}</fieldset>
</figure>'''

def home():
    latest = sorted(ARTICLES, key=lambda a:a["date"], reverse=True)[:3]
    tabs_btn = "".join(f'<button class="tab" role="tab" id="t-{s["id"]}" aria-controls="p-{s["id"]}" aria-selected="{"true" if i==0 else "false"}" tabindex="{0 if i==0 else -1}">{s["tab"]}<small>{s["small"]}</small></button>' for i,s in enumerate(SERVICES))
    def spec(s): return "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k,v in s["spec"])
    tabs_pan = "".join(f'''<div class="tabpanel" role="tabpanel" id="p-{s["id"]}" aria-labelledby="t-{s["id"]}"{"" if i==0 else " hidden"}>
<h3>{s["h"]}</h3><div class="xs">{xsection(s["kind"])}</div><p>{s["p"]}</p><dl class="spec">{spec(s)}</dl>
<p style="margin:0"><a class="lnk" href="{s["link"][0]}">{s["link"][1]}</a></p></div>''' for i,s in enumerate(SERVICES))
    day = "".join(f'<li><time>{t}</time><i></i><div><h3>{h}</h3><p>{d}</p></div></li>' for t,h,d in DAY)
    price_rows = "".join(f'<div class="row"><div><b>{n}</b><span>{d}</span></div><div class="t">{t}</div><div class="p">{p}</div></div>' for n,d,p,t in
                         [PRICES[0][1][0],PRICES[0][1][1],PRICES[1][1][0],PRICES[1][1][2],PRICES[2][1][2],PRICES[3][1][0]])
    faq = "".join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)
    brands = "".join(f"<span>{b}</span>" for b in BRANDS)
    body = f'''
<section class="hero"><div class="wrap hero-grid">
<div class="hero-copy">
<h1>Скол зникає.<br>Заводська фарба залишається.</h1>
<p class="lead">Локальний ремонт ЛКП та детейлінг для авто преміум-сегмента в Кривому Розі. Не перефарбовуємо деталь: відновлюємо лише пошкоджену зону, щоб її неможливо було знайти.</p>
<div class="btns"><a class="btn pri" href="tel:{PHONE_TEL}">Записатися на огляд</a><a class="btn sec" href="{TELEGRAM}">Надіслати фото</a></div>
</div>
{lab()}
</div>
<ul class="facts"><li><b>Заводський шар</b>зберігаємо навколо ремонту</li><li><b>Товщина покриття</b>вимірюємо до початку робіт</li><li><b>Колір</b>за кодом і під денне світло</li><li><b>Строк</b>сколи й подряпини за 1 день</li></ul></section>

<section class="s"><div class="wrap"><div class="s-head"><h2>Навіщо перефарбовувати всю деталь, якщо пошкоджено сантиметр</h2>
<p>Повне фарбування знімає заводський шар по всій площі. Локальний ремонт працює лише там, де є пошкодження, і залишає решту покриття як є.</p></div>
<div class="versus">
<div class="vs main"><h3>Локальний ремонт</h3><p>Наш підхід</p><ul>
<li>Заводські лак і фарба поруч із зоною залишаються недоторканими</li>
<li>Мінімальна площа втручання, а отже, мінімум слідів ремонту</li>
<li>Колір готуємо під ваш кузов, перехід розтушовуємо непомітно</li>
<li>Сколи й подряпини зазвичай за один день</li></ul></div>
<div class="vs"><h3>Фарбування всієї деталі</h3><p>Іноді потрібне, але не завжди</p><ul>
<li>Заводське покриття знімається по всій панелі</li>
<li>Складні кольори (перламутр, тришарові) важче збігти на великій площі</li>
<li>Більше матеріалів, часу й вартості</li>
<li>Ризик різниці з сусідніми деталями</li></ul></div></div>
<p class="mut" style="margin-top:28px;max-width:62ch">Якщо пошкодження велике і локальний ремонт не дасть результату, скажемо про це чесно й запропонуємо перефарбувати елемент.</p></div></section>

<section class="s alt"><div class="wrap"><div class="s-head"><h2>Що пошкоджено в покритті, те й лагодимо</h2>
<p>Покриття складається з чотирьох шарів. Від того, до якого шару дійшла подряпина чи скол, залежить, чи вистачить полірування, чи потрібне локальне фарбування.</p></div>
<div class="tabs"><div class="tablist" role="tablist" aria-label="Види ремонту" aria-orientation="vertical">{tabs_btn}</div><div>{tabs_pan}</div></div></div></section>

<section class="s"><div class="wrap"><div class="s-head"><h2>Стандарт роботи</h2><p>Те, що ми робимо щоразу, незалежно від розміру пошкодження.</p></div>
<div class="ledger">
<div><h3>Діагностика</h3><p>Розглядаємо пошкодження під світлом, вимірюємо товщину покриття, визначаємо глибину й чесно називаємо метод.</p><small>до початку робіт</small></div>
<div><h3>Колір</h3><p>Готуємо за кодом виробника, коригуємо під ваш кузов, зразок звіряємо при денному світлі.</p><small>непомітний перехід</small></div>
<div><h3>Мінімальна зона</h3><p>Працюємо на ділянці скола чи подряпини й розтушовуємо перехід, не чіпаючи решту деталі.</p><small>заводська фарба зберігається</small></div>
<div><h3>Видача</h3><p>Показуємо результат при денному світлі й пояснюємо, як доглядати за свіжим покриттям.</p><small>день у день</small></div>
</div></div></section>

<section class="s alt"><div class="wrap day"><div><h2>Як виглядає один день ремонту</h2>
<p class="lead">Типовий графік для сколів, подряпин і локальних ділянок. Цілу деталь або складний колір можемо вести 1–2 дні — скажемо заздалегідь.</p>
<div class="btns"><a class="btn sec" href="yak-ce-pratsyuye.html">Детальніше про процес</a></div></div>
<ol class="tl">{day}</ol></div></section>

<section class="s"><div class="wrap two"><div><h2>Один код фарби, кілька відтінків</h2>
<p class="lead">Навіть авто однієї моделі й року можуть мати трохи різний тон: заводські партії, сонце, час. Тому код — це лише початок. Ми готуємо зразок і звіряємо його з вашим кузовом при денному світлі, а перехід розтушовуємо так, щоб межі ремонту не було видно.</p>
<p style="margin-top:20px"><a class="lnk" href="blog/kod-farby-pidbir-koljoru.html">Де знайти код фарби і як ми підбираємо колір</a></p></div>
<div class="fan" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></div></div></section>

<section class="s alt"><div class="wrap"><div class="s-head"><h2>Популярні роботи й ціни</h2><p>Мінімальна вартість. Точну називаємо після огляду.</p></div>
<div class="rows">{price_rows}</div><p style="margin-top:24px"><a class="lnk" href="tsiny.html">Повний прайс</a></p></div></section>

<section class="s"><div class="wrap"><div class="s-head"><h2>Матеріали професійного рівня</h2><p>Лаки, ґрунти, полірувальні системи й захисні покриття відомих виробників. Це наш робочий інструмент: ми не продаємо матеріали, а застосовуємо їх у ремонті.</p></div>
<div class="brands">{brands}</div><p style="margin-top:28px"><a class="lnk" href="materialy.html">Усі категорії матеріалів</a></p></div></section>

<section class="s alt"><div class="wrap"><div class="s-head"><h2>Питання, які ставлять найчастіше</h2></div><div class="faq">{faq}</div></div></section>

<section class="s"><div class="wrap"><div class="s-head" style="display:flex;justify-content:space-between;align-items:end;max-width:none"><h2 style="margin:0">З блогу</h2><a class="lnk" href="blog/index.html">Усі статті</a></div>
<div class="posts">{post_rows(latest)}</div></div></section>
'''
    ld = {"@context":"https://schema.org","@type":"AutoBodyShop","name":BRAND,"description":TAGLINE,
          "address":{"@type":"PostalAddress","addressLocality":CITY,"addressCountry":"UA"},
          "telephone":PHONE_TEL,"url":DOMAIN,"email":EMAIL,"openingHours":"Mo-Sa 09:00-19:00","areaServed":CITY}
    fq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}
    extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(fq, ensure_ascii=False)}</script>'
    page("index.html", f"{BRAND}: локальний ремонт ЛКП та детейлінг преміум-авто у {CITY_LOC}", "Усуваємо сколи й подряпини локально, зберігаючи заводську фарбу. Колір за кодом, полірування, захист кузова. Кривий Ріг.", body, "index.html", extra)

def uslugy():
    rows = ""
    for s in SERVICES:
        sp = "".join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k,v in s["spec"])
        rows += f'''<section class="s tight" id="{s["id"]}" style="border-top:1px solid var(--line)"><div class="wrap two" style="align-items:start">
<div><h2>{s["tab"]}</h2><h3 style="font-weight:400;color:var(--mut);font-size:20px;line-height:1.4">{s["h"]}</h3><p>{s["p"]}</p><dl class="spec">{sp}</dl><p style="margin-top:18px"><a class="lnk" href="{{{{root}}}}{s["link"][0]}">{s["link"][1]}</a></p></div>
<div class="xs" style="padding:14px">{xsection(s["kind"])}</div></div></section>'''
    body = page_head("Послуги", f"Усе для відновлення лакофарбового покриття в {CITY_LOC}. На схемах показано, де саме в покритті йде робота.") + rows
    page("uslugy.html", f"Послуги з ремонту ЛКП: {BRAND}, {CITY}", f"Усунення сколів і подряпин, локальне фарбування, ремонт бамперів, полірування й захист кузова в {CITY_LOC}.", body)

def tsiny():
    body = page_head("Ціни", "Мінімальна вартість роботи. Остаточна ціна залежить від розміру, глибини пошкодження, кольору й матеріалу деталі.") + f'''
<section class="s tight" style="padding-top:0"><div class="wrap narrow" style="max-width:var(--wrap)">{prices_html(PRICES)}
<div class="note"><b>Як отримати точну ціну.</b> Надішліть 2–3 фото, марку, модель і колір авто. Огляд на місці безкоштовний. Якщо під час роботи обсяг зміниться, зупинимось і погодимо це з вами.</div>
<p class="mut small">Терміни типові для невеликих пошкоджень. Цілу деталь і складні кольори (перламутр, тришарові) можемо вести 1–2 дні.</p></div></section>'''
    page("tsiny.html", f"Ціни на ремонт ЛКП: {BRAND}, {CITY}", f"Прайс на усунення сколів і подряпин, локальне фарбування, полірування та захист кузова в {CITY_LOC}.", body)

def process():
    day = "".join(f'<li><time>{t}</time><i></i><div><h3>{h}</h3><p>{d}</p></div></li>' for t,h,d in DAY)
    body = f'''<section class="s"><div class="wrap"><h1 style="font-size:clamp(32px,4.6vw,56px)">Як ми працюємо</h1><p class="lead" style="margin-bottom:48px">Типовий графік для сколів, подряпин і локальних ділянок. Привезли зранку, забрали ввечері.</p>
<div class="day" style="grid-template-columns:1fr"><ol class="tl" style="max-width:760px">{day}</ol></div>
<p class="mut small" style="margin-top:32px;max-width:60ch">Цілу деталь, складні кольори (перламутр, тришарові) й великі пошкодження можуть потребувати 1–2 днів. Про це скажемо під час огляду.</p>
<p style="margin-top:20px"><a class="lnk" href="blog/lokalne-farbuvannya-yak-pratsyuye.html">Детальніше про технологію локального ремонту</a></p></div></section>'''
    page("yak-ce-pratsyuye.html", f"Як ми працюємо: {BRAND}, {CITY}", "Етапи локального ремонту ЛКП від огляду до видачі авто за один день.", body)

def materials():
    rows = "".join(f'<div><h3>{t}</h3><p>{d}</p><small>{b}</small></div>' for t,d,b in MATERIALS)
    body = page_head("Матеріали, з якими ми працюємо", "Результат залежить від матеріалів не менше, ніж від майстра. Це наш робочий інструмент: ми не продаємо матеріали, а застосовуємо їх у ремонті.") + f'''
<section class="s tight" style="padding-top:0"><div class="wrap"><div class="ledger">{rows}</div>
<div class="note" style="max-width:780px"><b>Чому це важливо.</b> Якісні ґрунти й лаки дають кращу адгезію та довговічність, а правильні полірувальні системи — рівну поверхню без голограм.</div></div></section>'''
    page("materialy.html", f"Матеріали для ремонту ЛКП: {BRAND}, {CITY}", "Лаки, ґрунти, полірувальні системи й захисні покриття, які ми використовуємо в роботі.", body)

def about():
    body = page_head("Про нас", f"{BRAND} — майстерня локального ремонту лакофарбового покриття в {CITY_LOC}. Працюємо з невеликими пошкодженнями і робимо їх швидко.") + f'''
<section class="s tight" style="padding-top:0"><div class="wrap narrow"><div class="prose"><h2>Наші принципи</h2>
<ul><li><b>Чесна оцінка.</b> Якщо вистачить полірування, не пропонуємо фарбування.</li>
<li><b>Зберігаємо заводську фарбу.</b> Ремонтуємо лише пошкоджену зону, а не перефарбовуємо всю деталь.</li>
<li><b>Ціна до початку робіт.</b> Якщо обсяг зміниться, зупинимось і погодимо.</li>
<li><b>Колір при денному світлі.</b> Звіряємо зразок із вашим кузовом до нанесення.</li></ul>
<h2>Чого ми не робимо</h2><p>Не беремося за кузовні роботи зі зварюванням і відновленням геометрії після серйозних ДТП. Якщо ваш випадок потребує цього, підкажемо, до кого звернутися.</p></div></div></section>'''
    page("pro-nas.html", f"Про нас: {BRAND}, {CITY}", f"{BRAND}: локальний ремонт ЛКП у {CITY_LOC}. Наші принципи й підхід до роботи.", body)

def contacts():
    body = page_head("Контакти") + f'''
<section class="s tight" style="padding-top:0"><div class="wrap two" style="align-items:start">
<div class="cinfo"><p><b>Телефон</b><a class="lnk" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
<p><b>Telegram і Viber</b><a class="lnk" href="{TELEGRAM}">Telegram</a> &nbsp; <a class="lnk" href="{VIBER}">Viber</a></p>
<p><b>Email</b><a class="lnk" href="mailto:{EMAIL}">{EMAIL}</a></p>
<p><b>Адреса</b>{ADDRESS}</p><p><b>Графік</b>{HOURS}</p></div>
<form class="form" onsubmit="return sendForm(this)"><h2 style="font-size:26px">Оцінка за фото</h2>
<label>Ім'я<input name="name" autocomplete="name" required></label>
<label>Телефон<input name="phone" type="tel" autocomplete="tel" required></label>
<label>Авто: марка, модель, рік, колір<input name="car" required></label>
<label>Що сталося<textarea name="msg" rows="4" placeholder="Наприклад: скол на капоті, подряпина на дверях"></textarea></label>
<button class="btn pri" type="submit">Надіслати</button>
<p class="mut small" style="margin:14px 0 0">Відкриється ваша пошта з готовим листом. Фото додайте до листа або надішліть у Telegram чи Viber.</p></form></div></section>
<script>window.__EMAIL="{EMAIL}";</script>'''
    page("kontakty.html", f"Контакти: {BRAND}, {CITY}", f"Телефон, адреса та форма для оцінки ремонту ЛКП за фото в {CITY_LOC}.", body, with_cta=False)

def blog():
    arts = sorted(ARTICLES, key=lambda a:a["date"], reverse=True)
    tags = []
    for a in arts:
        if a["tag"] not in tags: tags.append(a["tag"])
    chips = '<button class="chipb" data-tag="all" aria-pressed="true">Усі</button>' + "".join(f'<button class="chipb" data-tag="{t}" aria-pressed="false">{t}</button>' for t in tags)
    body = page_head("Блог", "Практичні поради про сколи, подряпини, колір і догляд за покриттям. Приклади — типові ситуації з практики.") + f'''
<section class="s tight" style="padding-top:0"><div class="wrap"><div class="filters" role="group" aria-label="Фільтр за темою">{chips}</div><div class="posts">{post_rows(arts).replace("{{root}}blog/","")}</div></div></section>'''
    page("blog/index.html", f"Блог про ремонт ЛКП: {BRAND}, {CITY}", "Статті про ремонт сколів, подряпин, підбір кольору, полірування й захист кузова.", body, "blog/index.html", with_cta=False)
    for a in ARTICLES:
        others = [x for x in arts if x["slug"] != a["slug"]][:3]
        ld = {"@context":"https://schema.org","@type":"Article","headline":a["title"],"description":a["desc"],
              "datePublished":a["date"],"dateModified":a["date"],"inLanguage":"uk",
              "author":{"@type":"Organization","name":BRAND},"publisher":{"@type":"Organization","name":BRAND},
              "mainEntityOfPage":f"{DOMAIN}/blog/{a['slug']}.html"}
        extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
        body = f'''<article class="s tight"><div class="wrap art"><div>
<p class="crumbs"><a class="lnk" href="index.html">Блог</a> / {a["tag"]}</p>
<h1>{a["title"]}</h1><p class="meta"><time datetime="{a["date"]}">{fdate(a["date"])}</time>, {a["min"]} хв читання</p>
<div class="prose">{a["body"]}</div></div>
<aside class="aside"><h3>Потрібен ремонт?</h3><p>Надішліть фото пошкодження — скажемо ціну й час.</p><a class="btn pri" href="{TELEGRAM}">Telegram</a><a class="btn sec" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></aside></div></article>
<section class="s alt"><div class="wrap"><div class="s-head"><h2>Читайте також</h2></div><div class="posts">{post_rows(others).replace("{{root}}blog/","")}</div></div></section>'''
        page(f"blog/{a['slug']}.html", f'{a["title"]}: {BRAND}', a["desc"], body, "blog/index.html", extra, with_cta=False)

def notfound():
    page("404.html", f"Сторінку не знайдено: {BRAND}", "Сторінку не знайдено.",
         page_head("Такої сторінки немає", 'Перевірте адресу або перейдіть <a class="lnk" href="{{root}}index.html">на головну</a>.'))

def static():
    os.makedirs(os.path.join(OUT,"assets"), exist_ok=True)
    for f in ("style.css","main.js"):
        shutil.copy(os.path.join(HERE,f), os.path.join(OUT,"assets",f))
    pages = ["index.html","uslugy.html","tsiny.html","yak-ce-pratsyuye.html","materialy.html","pro-nas.html","kontakty.html","blog/index.html"]
    urls = [(f"{DOMAIN}/{p}", "2026-10-23") for p in pages] + [(f"{DOMAIN}/blog/{a['slug']}.html", a["date"]) for a in ARTICLES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{u}</loc><lastmod>{d}</lastmod></url>\n" for u,d in urls) + "</urlset>\n"
    open(os.path.join(OUT,"sitemap.xml"),"w",encoding="utf-8").write(sm)
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    open(os.path.join(OUT,".nojekyll"),"w").close()

if __name__ == "__main__":
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    static(); home(); uslugy(); tsiny(); process(); materials(); about(); contacts(); blog(); notfound()
    print("OK", len(ARTICLES), "articles")
