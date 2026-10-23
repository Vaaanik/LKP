# -*- coding: utf-8 -*-
import os, shutil, json, datetime
from articles import ARTICLES

# ====== НАЛАШТУВАННЯ (змініть на свої дані) ======
BRAND = "Точний Тон"
TAGLINE = "Локальний ремонт ЛКП день у день"
CITY = "Кривий Ріг"
DOMAIN = "https://vaaanik.github.io/LKP"
PHONE_DISPLAY = "+38 (095) 590-88-08"
PHONE_TEL = "+380955908808"
TELEGRAM = "https://t.me/+380955908808"
VIBER = "viber://chat?number=%2B380955908808"
EMAIL = "v2394454@gmail.com"
ADDRESS = "м. Кривий Ріг, Дніпропетровська область"
HOURS = "Пн–Сб: 09:00–19:00"
OUT = "/home/claude/site"
# =================================================

MONTHS = ["січня","лютого","березня","квітня","травня","червня","липня","серпня","вересня","жовтня","листопада","грудня"]
def fdate(s):
    d = datetime.date.fromisoformat(s)
    return f"{d.day} {MONTHS[d.month-1]} {d.year}"

LOGO = '''<svg class="logo-mark" viewBox="0 0 40 40" aria-hidden="true"><rect x="1" y="1" width="38" height="38" rx="10" fill="#14201c"/><path d="M8 28 L8 12 Q8 8 12 8 L28 8 Q32 8 32 12 L32 20 L20 20 L20 28 Z" fill="#f4f1ea"/><circle cx="27" cy="27" r="6" fill="#e8542a"/></svg>'''

NAV = [("uslugy.html","Послуги"),("tsiny.html","Ціни"),("yak-ce-pratsyuye.html","Як працюємо"),
       ("materialy.html","Матеріали"),("blog/index.html","Блог"),("pro-nas.html","Про нас"),("kontakty.html","Контакти")]

def head(title, desc, root, path, extra=""):
    canon = f"{DOMAIN}/{path}"
    return f'''<!doctype html>
<html lang="uk"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:type" content="website"><meta property="og:locale" content="uk_UA"><meta property="og:url" content="{canon}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600&family=Unbounded:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}assets/style.css">
{extra}
</head><body>'''

def header(root, active):
    links = "".join(f'<a href="{root}{h}"{" class=on" if h==active else ""}>{t}</a>' for h,t in NAV)
    return f'''<header class="top"><div class="wrap bar">
<a class="brand" href="{root}index.html">{LOGO}<span><b>{BRAND}</b><small>ремонт ЛКП · {CITY}</small></span></a>
<nav id="nav">{links}</nav>
<a class="tel" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
<button class="burger" aria-label="Меню" onclick="document.body.classList.toggle('menu')"><span></span><span></span><span></span></button>
</div></header>'''

def footer(root):
    return f'''<footer class="foot"><div class="wrap grid4">
<div><a class="brand" href="{root}index.html">{LOGO}<span><b>{BRAND}</b><small>ремонт ЛКП · {CITY}</small></span></a>
<p class="mut">{TAGLINE}. Сколи, подряпини, локальне фарбування, полірування.</p></div>
<div><h4>Сторінки</h4>{"".join(f'<a href="{root}{h}">{t}</a>' for h,t in NAV[:4])}</div>
<div><h4>Ще</h4>{"".join(f'<a href="{root}{h}">{t}</a>' for h,t in NAV[4:])}</div>
<div><h4>Контакти</h4><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a><a href="{TELEGRAM}">Telegram</a><a href="{VIBER}">Viber</a><span class="mut">{ADDRESS}</span><span class="mut">{HOURS}</span></div>
</div><div class="wrap legal">© {BRAND}, {CITY}. Ціни у прайсі орієнтовні; остаточна вартість — після огляду.</div></footer>
<script src="{root}assets/main.js"></script></body></html>'''

def cta(root):
    return f'''<section class="cta"><div class="wrap cta-in"><div><h2>Надішліть фото — скажемо ціну і час</h2>
<p>Напишіть марку, модель, колір авто та додайте 2–3 фото пошкодження. Відповімо в робочий час.</p></div>
<div class="btns"><a class="btn" href="{TELEGRAM}">Telegram</a><a class="btn ghost" href="{VIBER}">Viber</a><a class="btn ghost" href="tel:{PHONE_TEL}">Зателефонувати</a></div></div></section>'''

def page(fname, title, desc, body, active=None, extra=""):
    depth = fname.count("/")
    root = "../"*depth
    html = head(title, desc, root, fname, extra) + header(root, active or fname) + body.replace("{{root}}", root) + cta(root) + footer(root)
    p = os.path.join(OUT, fname)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(html)

# ---------- Ціни (орієнтовні) ----------
PRICES = [
 ("Сколи та подряпини", [
  ("Усунення сколів", "до 3 сколів на одній деталі", "від 1 000 ₴", "3–4 год"),
  ("Усунення подряпин поліруванням", "поверхневі, без глибоких пошкоджень", "від 1 500 ₴", "1–2 год"),
  ("Усунення глибокої подряпини", "локальне фарбування зони", "від 3 500 ₴", "1 день"),
 ]),
 ("Локальне та повне фарбування", [
  ("Локальне фарбування", "ділянка до ~15×15 см", "від 3 500 ₴", "1 день"),
  ("Фарбування елемента кузова", "матеріали включено у вартість", "від 9 000 ₴", "1–2 дні"),
  ("Ремонт і фарбування бампера", "пластик, потертості, задири", "від 4 500 ₴", "1 день"),
 ]),
 ("Полірування", [
  ("Освіжаюче полірування кузова", "дрібні подряпини, блиск", "від 4 000 ₴", "1 день"),
  ("Відновлювальне полірування кузова", "середні подряпини, «павутинка»", "від 7 000 ₴", "1–2 дні"),
  ("Полірування окремого елемента", "двері, капот, крило", "від 700 ₴", "1–2 год"),
 ]),
 ("Захист", [
  ("Антидощ на скло", "лобове або бокові скла", "від 600 ₴", "30–60 хв"),
  ("Віск на кузов", "блиск і легка гідрофобність", "від 1 500 ₴", "2–3 год"),
  ("Кварцеве / керамічне покриття", "залежить від покриття та авто", "від 6 000 ₴", "1–2 дні"),
 ]),
]

def prices_table(groups):
    out = ""
    for g, rows in groups:
        out += f'<h3 class="pg">{g}</h3><div class="ptable">'
        for n, d, p, t in rows:
            out += f'<div class="prow"><div><b>{n}</b><span>{d}</span></div><div class="pt">{t}</div><div class="pp">{p}</div></div>'
        out += '</div>'
    return out

# ---------- Матеріали (з detailing-paint-shop.com; не продаємо) ----------
MATERIALS = [
 ("Лаки та ґрунти", "Акрилові лаки, швидкосохнучі ґрунти, адгезійні ґрунти для пластику і металу.", "Visman, Mipa, Carbo"),
 ("Полірування", "Полірувальні пасти, пади різної жорсткості, засоби для очищення поверхні.", "RUPES, LeadMax, Work Stuff, Visman"),
 ("Захисні покриття", "Віск, кварцові та нанокерамічні покриття, антидощ для скла.", "Nasiol, Soft99, K2, CoatPlus"),
 ("Нанесення фарби", "Професійні фарбопульти й обладнання для рівного нанесення.", "Anest Iwata"),
 ("Підготовка та маскування", "Знежирювачі, розчинники, маскувальні матеріали, шпаклівки.", "Різні виробники"),
 ("Герметики та клеї", "Шовні герметики й клеї для відновлення швів та кузовних робіт.", "Teroson та ін."),
]

# ====== ГОЛОВНА ======
def home():
    latest = sorted(ARTICLES, key=lambda a:a["date"], reverse=True)[:3]
    cards = "".join(f'<a class="card" href="blog/{a["slug"]}.html"><small>{a["tag"]} · {fdate(a["date"])}</small><h3>{a["title"]}</h3><p>{a["desc"]}</p></a>' for a in latest)
    srv = [("Сколи","Заповнюємо кратер, захищаємо метал, повертаємо вигляд.","uslugy.html#skoly"),
           ("Подряпини","Полірування або локальне фарбування — залежно від глибини.","uslugy.html#podryapyny"),
           ("Локальне фарбування","Відновлюємо лише пошкоджену зону, без перефарбування всієї деталі.","uslugy.html#farbuvannya"),
           ("Бампери","Потертості, задири й тріщини пластику.","uslugy.html#bampery"),
           ("Полірування","Прибираємо «павутинку», повертаємо глибокий блиск.","uslugy.html#polirovanya"),
           ("Захист кузова","Віск, кварц, кераміка, антидощ.","uslugy.html#zakhyst")]
    scards = "".join(f'<a class="svc" href="{h}"><h3>{t}</h3><p>{d}</p><span>Детальніше →</span></a>' for t,d,h in srv)
    body = f'''
<section class="hero"><div class="wrap hero-in">
<div><p class="eyebrow">{CITY} · локальний ремонт ЛКП</p>
<h1>Ремонт фарби кузова <em>день&nbsp;у&nbsp;день</em></h1>
<p class="lead">Сколи, подряпини, потертості, локальне фарбування. Підбираємо колір за кодом і перевіряємо при денному світлі. Привезли вранці — забрали ввечері.</p>
<div class="btns"><a class="btn" href="kontakty.html">Дізнатися ціну за фото</a><a class="btn ghost" href="tsiny.html">Дивитись ціни</a></div>
<ul class="ticks"><li>Огляд безкоштовний</li><li>Ціна «від» і точна — після огляду</li><li>Без прихованих доплат</li></ul></div>
<div class="art" aria-hidden="true"><svg viewBox="0 0 440 360"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2b3d36"/><stop offset="1" stop-color="#14201c"/></linearGradient></defs>
<rect x="10" y="30" width="420" height="300" rx="36" fill="url(#g)"/>
<path d="M40 120 Q220 60 400 120" stroke="#ffffff22" stroke-width="3" fill="none"/>
<path d="M60 250 L190 190" stroke="#e8542a" stroke-width="3" stroke-linecap="round"/>
<circle cx="300" cy="150" r="5" fill="#e8542a"/><circle cx="318" cy="168" r="3" fill="#e8542a"/><circle cx="285" cy="175" r="3" fill="#e8542a"/>
<circle cx="300" cy="150" r="58" fill="none" stroke="#f4f1ea" stroke-width="5"/><line x1="342" y1="192" x2="388" y2="238" stroke="#f4f1ea" stroke-width="9" stroke-linecap="round"/>
</svg>
<div class="chips"><i style="background:#e8542a"></i><i style="background:#0f5c4a"></i><i style="background:#c9b8a0"></i><i style="background:#14201c"></i><i style="background:#8fa9b8"></i></div></div>
</div></section>

<section class="sec"><div class="wrap"><h2>Що ремонтуємо</h2><div class="grid3">{scards}</div></div></section>

<section class="sec alt"><div class="wrap"><h2>Чому «день у день» — це реально</h2>
<div class="grid3">
<div class="pt1"><b>01</b><h3>Малий обсяг</h3><p>Ремонтуємо тільки пошкоджену зону, а не всю деталь. Це швидше і економніше.</p></div>
<div class="pt1"><b>02</b><h3>Швидкосохнучі матеріали</h3><p>Сучасні ґрунти й лаки та інфрачервоне сушіння скорочують час без втрати якості.</p></div>
<div class="pt1"><b>03</b><h3>Чесні терміни</h3><p>Складні випадки (ціла деталь, перламутр) можуть потребувати 1–2 днів. Скажемо заздалегідь.</p></div>
</div></div></section>

<section class="sec"><div class="wrap"><div class="split"><div><h2>Колір, який збігається</h2>
<p>Підбір кольору — головне в локальному ремонті. Ми визначаємо код фарби, готуємо зразок, порівнюємо його з кузовом при денному світлі й коригуємо. Для складних кольорів плавно розтушовуємо перехід, щоб межу ремонту не було видно.</p>
<p><a class="lnk" href="blog/kod-farby-pidbir-koljoru.html">Читати: код фарби і підбір кольору →</a></p></div>
<div><h2>Матеріали без компромісів</h2><p>Працюємо з перевіреними лаками, ґрунтами та полірувальними системами відомих виробників. Ми їх застосовуємо в роботі, а не продаємо.</p>
<p><a class="lnk" href="materialy.html">Які матеріали використовуємо →</a></p></div></div></div></section>

<section class="sec alt"><div class="wrap"><div class="rowh"><h2>З блогу</h2><a class="lnk" href="blog/index.html">Усі статті →</a></div><div class="grid3">{cards}</div></div></section>
'''
    ld = {"@context":"https://schema.org","@type":"AutoBodyShop","name":BRAND,"description":TAGLINE,
          "address":{"@type":"PostalAddress","addressLocality":CITY,"addressCountry":"UA","streetAddress":ADDRESS},
          "telephone":PHONE_TEL,"url":DOMAIN,"openingHours":"Mo-Sa 09:00-19:00","areaServed":CITY}
    extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
    page("index.html", f"{BRAND} — ремонт ЛКП день у день у {CITY}", f"Локальний ремонт ЛКП у Кривому Розі: сколи, подряпини, фарбування, полірування. Підбір кольору за кодом. Ціни та терміни.", body, "index.html", extra)

def uslugy():
    blocks = [
     ("skoly","Усунення сколів","Скол — це вхід для вологи й корозії. Очищаємо, за потреби обробляємо метал, заповнюємо кратер ґрунтом, базою в колір та лаком, потім вирівнюємо й полірюємо.","від 1 000 ₴","blog/skol-na-kapoti-koroziya.html","Чому не варто чекати"),
     ("podryapyny","Усунення подряпин","Поверхневі подряпини прибираємо поліруванням, глибокі — локальним фарбуванням. Оцінюємо глибину на огляді й чесно кажемо, що підходить саме вам.","від 1 500 ₴","blog/podryapina-polirovka-chy-farbuvannya.html","Полірування чи фарбування"),
     ("farbuvannya","Локальне фарбування","Відновлюємо лише пошкоджену зону з плавним переходом кольору. Підходить для невеликих і середніх пошкоджень.","від 3 500 ₴","blog/lokalne-farbuvannya-yak-pratsyuye.html","Як це працює"),
     ("element","Фарбування елемента кузова","Якщо пошкодження велике, фарбуємо деталь повністю. Матеріали включені у вартість.","від 9 000 ₴","blog/skilky-koshtuye-remont-lkp.html","З чого складається ціна"),
     ("bampery","Ремонт бамперів","Потертості, задири, невеликі тріщини. Використовуємо адгезійні ґрунти для пластику.","від 4 500 ₴","blog/remont-bampera-plastyk.html","Ремонт чи заміна"),
     ("polirovanya","Полірування кузова","Освіжаюче й відновлювальне полірування, окремі елементи. Вимірюємо товщину покриття, щоб не зняти зайвого.","від 700 ₴","blog/vidnovlyuvalne-poliruvannya.html","Що вміє полірування"),
     ("zakhyst","Захист кузова і скла","Віск, кварцове й керамічне покриття, антидощ. Рекомендуємо після ремонту.","від 600 ₴","blog/zakhyst-pislya-remontu.html","Віск, кварц, кераміка"),
    ]
    items = "".join(f'<article class="svcrow" id="{i}"><div><h2>{t}</h2><p>{d}</p><a class="lnk" href="{{{{root}}}}{l}">{ln} →</a></div><div class="price">{p}</div></article>' for i,t,d,p,l,ln in blocks)
    body = f'<section class="sec"><div class="wrap narrow"><h1 class="h1s">Послуги</h1><p class="lead">Усе для відновлення лакофарбового покриття в {CITY}. Ціни орієнтовні — точну вартість називаємо після огляду.</p>{items}</div></section>'
    page("uslugy.html", f"Послуги з ремонту ЛКП — {BRAND}, {CITY}", f"Усунення сколів і подряпин, локальне фарбування, ремонт бамперів, полірування й захист кузова в {CITY}.", body)

def tsiny():
    body = f'''<section class="sec"><div class="wrap narrow"><h1 class="h1s">Ціни</h1>
<p class="lead">Мінімальна вартість роботи. Остаточна ціна залежить від розміру, глибини пошкодження, кольору й матеріалу деталі.</p>{prices_table(PRICES)}
<div class="note"><b>Як отримати точну ціну.</b> Надішліть 2–3 фото і напишіть марку, модель та колір авто. Огляд на місці безкоштовний. Ми зупиняємося й узгоджуємо з вами будь-які зміни обсягу робіт.</div>
<p class="mut small">Терміни — типові для невеликих пошкоджень. Складні випадки (ціла деталь, перламутрові кольори) можуть потребувати 1–2 днів.</p></div></section>'''
    page("tsiny.html", f"Ціни на ремонт ЛКП — {BRAND}, {CITY}", f"Прайс на усунення сколів, подряпин, локальне фарбування, полірування та захист кузова в {CITY}.", body)

def process():
    steps = [("Огляд","Оцінюємо глибину пошкодження, матеріал деталі, колір. Називаємо ціну і час."),
             ("Підготовка","Мийка, знежирення, маскування. Шліфуємо зону ремонту з плавними краями."),
             ("Ґрунт і вирівнювання","Захищаємо метал, за потреби шпаклюємо й вирівнюємо поверхню."),
             ("Колір","Готуємо фарбу за кодом, перевіряємо зразок при денному світлі, коригуємо."),
             ("Фарба й лак","Наносимо базу, розтушовуємо перехід, закриваємо лаком."),
             ("Сушіння й полірування","Сушимо, вирівнюємо поверхню, повертаємо блиск."),
             ("Видача","Показуємо результат при денному світлі, пояснюємо догляд у перші тижні.")]
    li = "".join(f'<li><b>{i+1}</b><div><h3>{t}</h3><p>{d}</p></div></li>' for i,(t,d) in enumerate(steps))
    body = f'<section class="sec"><div class="wrap narrow"><h1 class="h1s">Як ми працюємо</h1><p class="lead">Сім кроків від огляду до видачі авто. У більшості випадків — за один день.</p><ol class="steps">{li}</ol><p><a class="lnk" href="blog/lokalne-farbuvannya-yak-pratsyuye.html">Детальніше про технологію локального ремонту →</a></p></div></section>'
    page("yak-ce-pratsyuye.html", f"Як ми працюємо — {BRAND}, {CITY}", "Етапи локального ремонту ЛКП: огляд, підготовка, колір, фарбування, полірування, видача.", body)

def materials():
    cards = "".join(f'<div class="card flat"><h3>{t}</h3><p>{d}</p><small>{b}</small></div>' for t,d,b in MATERIALS)
    body = f'''<section class="sec"><div class="wrap"><h1 class="h1s">Матеріали, з якими ми працюємо</h1>
<p class="lead narrow">Результат ремонту залежить від матеріалів не менше, ніж від майстра. Ми використовуємо перевірені системи для підготовки, фарбування, полірування й захисту. Це наш робочий інструмент: ми не продаємо матеріали, а застосовуємо їх у ремонті.</p>
<div class="grid3">{cards}</div>
<div class="note narrow"><b>Чому це важливо для вас.</b> Якісні ґрунти й лаки дають кращу адгезію та довговічність, а правильні полірувальні системи — рівну поверхню без голограм.</div></div></section>'''
    page("materialy.html", f"Матеріали для ремонту ЛКП — {BRAND}, {CITY}", "Лаки, ґрунти, полірувальні системи й захисні покриття, які ми використовуємо в роботі.", body)

def about():
    body = f'''<section class="sec"><div class="wrap narrow"><h1 class="h1s">Про нас</h1>
<p class="lead">{BRAND} — майстерня локального ремонту лакофарбового покриття в {CITY}. Ми працюємо з невеликими пошкодженнями і робимо їх швидко.</p>
<h2>Наші принципи</h2>
<ul class="ticks big"><li><b>Чесна оцінка.</b> Якщо вистачить полірування — не пропонуємо фарбування.</li>
<li><b>Мінімальне втручання.</b> Ремонтуємо тільки пошкоджену зону.</li>
<li><b>Прозорі ціни.</b> Називаємо вартість до початку робіт.</li>
<li><b>Колір при денному світлі.</b> Перевіряємо збіг до нанесення.</li></ul>
<h2>Що ми не робимо</h2>
<p>Ми не беремося за кузовні роботи зі зварюванням і відновленням геометрії після серйозних ДТП. Якщо ваш випадок потребує цього, підкажемо, до кого звернутися.</p></div></section>'''
    page("pro-nas.html", f"Про нас — {BRAND}, {CITY}", f"{BRAND}: локальний ремонт ЛКП у {CITY}. Наші принципи й підхід до роботи.", body)

def contacts():
    body = f'''<section class="sec"><div class="wrap narrow"><h1 class="h1s">Контакти</h1>
<div class="split"><div><p><b>Телефон</b><br><a class="lnk" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
<p><b>Telegram / Viber</b><br><a class="lnk" href="{TELEGRAM}">Telegram</a> · <a class="lnk" href="{VIBER}">Viber</a></p>
<p><b>Email</b><br><a class="lnk" href="mailto:{EMAIL}">{EMAIL}</a></p>
<p><b>Адреса</b><br>{ADDRESS}</p><p><b>Графік</b><br>{HOURS}</p></div>
<form class="form" onsubmit="return sendForm(this)"><h2>Оцінка за фото</h2>
<label>Ім'я<input name="name" required></label>
<label>Телефон<input name="phone" type="tel" required></label>
<label>Авто (марка, модель, рік, колір)<input name="car" required></label>
<label>Що сталося<textarea name="msg" rows="4" placeholder="Наприклад: скол на капоті, подряпина на дверях"></textarea></label>
<button class="btn" type="submit">Надіслати</button>
<p class="mut small">Після надсилання відкриється ваша пошта. Фото додайте у листі, або напишіть нам у Telegram чи Viber.</p></form></div></div></section>
<script>window.__EMAIL="{EMAIL}";</script>'''
    page("kontakty.html", f"Контакти — {BRAND}, {CITY}", f"Телефон, адреса та форма для оцінки ремонту ЛКП за фото в {CITY}.", body)

def blog():
    arts = sorted(ARTICLES, key=lambda a:a["date"], reverse=True)
    cards = "".join(f'<a class="card" href="{a["slug"]}.html"><small>{a["tag"]} · {fdate(a["date"])} · {a["min"]} хв</small><h3>{a["title"]}</h3><p>{a["desc"]}</p></a>' for a in arts)
    body = f'<section class="sec"><div class="wrap"><h1 class="h1s">Блог</h1><p class="lead narrow">Практичні поради про сколи, подряпини, колір і догляд за покриттям. Приклади — типові ситуації з нашої практики.</p><div class="grid3">{cards}</div></div></section>'
    page("blog/index.html", f"Блог про ремонт ЛКП — {BRAND}, {CITY}", "Статті про ремонт сколів, подряпин, підбір кольору, полірування й захист кузова.", body, "blog/index.html")
    for a in ARTICLES:
        others = [x for x in arts if x["slug"] != a["slug"]][:3]
        rel = "".join(f'<a class="card" href="{x["slug"]}.html"><small>{x["tag"]} · {fdate(x["date"])}</small><h3>{x["title"]}</h3></a>' for x in others)
        ld = {"@context":"https://schema.org","@type":"Article","headline":a["title"],"description":a["desc"],
              "datePublished":a["date"],"dateModified":a["date"],"inLanguage":"uk",
              "author":{"@type":"Organization","name":BRAND},"publisher":{"@type":"Organization","name":BRAND},
              "mainEntityOfPage":f"{DOMAIN}/blog/{a['slug']}.html"}
        extra = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>'
        body = f'''<article class="sec"><div class="wrap narrow art-page"><p class="crumbs"><a href="index.html">Блог</a> / {a["tag"]}</p>
<h1 class="h1s">{a["title"]}</h1><p class="meta"><time datetime="{a["date"]}">{fdate(a["date"])}</time> · {a["min"]} хв читання</p>
<div class="prose">{a["body"]}</div></div></article>
<section class="sec alt"><div class="wrap"><h2>Читайте також</h2><div class="grid3">{rel}</div></div></section>'''
        page(f"blog/{a['slug']}.html", f'{a["title"]} — {BRAND}', a["desc"], body, "blog/index.html", extra)

def notfound():
    page("404.html", f"Сторінку не знайдено — {BRAND}", "Сторінку не знайдено.",
         '<section class="sec"><div class="wrap narrow"><h1 class="h1s">404</h1><p class="lead">Такої сторінки немає. Перейдіть на <a class="lnk" href="{{root}}index.html">головну</a>.</p></div></section>')

CSS = r'''
:root{--bg:#f4f1ea;--ink:#14201c;--mut:#5c6b65;--line:#d9d3c5;--card:#fbf9f4;--acc:#e8542a;--grn:#0f5c4a;--r:18px}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.65 Onest,system-ui,sans-serif}
h1,h2,h3,h4{font-family:Unbounded,Onest,sans-serif;line-height:1.2;margin:0 0 .6em;font-weight:700}
h1{font-size:clamp(30px,5vw,56px)}h2{font-size:clamp(22px,3vw,32px)}h3{font-size:18px}
a{color:inherit}.wrap{max-width:1160px;margin:0 auto;padding:0 20px}.narrow{max-width:820px}
.mut{color:var(--mut)}.small{font-size:14px}
.top{position:sticky;top:0;z-index:20;background:#f4f1eaee;backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
.bar{display:flex;align-items:center;gap:24px;height:68px}
.brand{display:flex;gap:10px;align-items:center;text-decoration:none}.brand span{display:flex;flex-direction:column;line-height:1.1}
.brand b{font-family:Unbounded;font-size:15px;text-transform:uppercase;letter-spacing:.02em}.brand small{font-size:12px;color:var(--mut)}
.logo-mark{width:38px;height:38px}
nav{display:flex;gap:18px;margin-left:auto;font-size:15px}nav a{text-decoration:none;padding:6px 2px;border-bottom:2px solid transparent}
nav a:hover,nav a.on{border-color:var(--acc)}
.tel{font-weight:600;text-decoration:none;white-space:nowrap}
.burger{display:none;background:none;border:0;padding:8px}.burger span{display:block;width:24px;height:2px;background:var(--ink);margin:5px 0}
.btn{display:inline-block;background:var(--acc);color:#fff;padding:14px 24px;border-radius:999px;text-decoration:none;font-weight:600;border:2px solid var(--acc);cursor:pointer;font:inherit;font-weight:600}
.btn:hover{filter:brightness(.93)}.btn.ghost{background:transparent;color:var(--ink);border-color:var(--ink)}
.btns{display:flex;gap:12px;flex-wrap:wrap;margin:22px 0}
.hero{padding:54px 0 40px}.hero-in{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center}
.hero em{font-style:normal;color:var(--acc)}.eyebrow{color:var(--grn);font-weight:600;text-transform:uppercase;letter-spacing:.08em;font-size:13px}
.lead{font-size:19px;color:#34443e}
.ticks{list-style:none;padding:0;margin:0;display:flex;gap:8px 22px;flex-wrap:wrap;color:var(--mut);font-size:15px}
.ticks li:before{content:"✓ ";color:var(--grn);font-weight:700}.ticks.big{flex-direction:column;font-size:17px;color:var(--ink)}
.art{position:relative}.art svg{width:100%;height:auto}.chips{display:flex;gap:8px;justify-content:center;margin-top:-14px}
.chips i{width:34px;height:34px;border-radius:50%;border:3px solid var(--bg);box-shadow:0 0 0 1px var(--line)}
.sec{padding:56px 0}.sec.alt{background:#ebe6da}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.grid4{display:grid;grid-template-columns:1.4fr 1fr 1fr 1.2fr;gap:28px}
.card,.svc,.pt1{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:22px;text-decoration:none;display:block}
.card:hover,.svc:hover{border-color:var(--ink);transform:translateY(-2px);transition:.15s}
.card small{color:var(--grn);font-weight:600}.card p,.svc p,.pt1 p{color:var(--mut);margin:.4em 0 0;font-size:15.5px}
.svc span{color:var(--acc);font-weight:600;font-size:14px;display:inline-block;margin-top:10px}.pt1 b{font-family:Unbounded;color:var(--acc)}
.card.flat:hover{transform:none;border-color:var(--line)}
.split{display:grid;grid-template-columns:1fr 1fr;gap:40px}.rowh{display:flex;justify-content:space-between;align-items:baseline}
.lnk{color:var(--grn);font-weight:600;text-decoration:underline;text-underline-offset:3px}
.cta{background:var(--ink);color:#f4f1ea;padding:48px 0}.cta-in{display:flex;gap:30px;align-items:center;justify-content:space-between;flex-wrap:wrap}
.cta h2{margin-bottom:.3em}.cta p{margin:0;color:#c9d3ce}.cta .btn.ghost{color:#f4f1ea;border-color:#f4f1ea}
.foot{background:#0e1613;color:#c9d3ce;padding:44px 0 20px;font-size:15px}.foot a{display:block;text-decoration:none;padding:3px 0}.foot a:hover{color:#fff}
.foot h4{font-size:14px;color:#fff}.foot .brand{display:flex}.foot .brand b{color:#fff}.foot .mut{color:#8fa09a;display:block}
.legal{margin-top:28px;padding-top:16px;border-top:1px solid #243029;color:#8fa09a;font-size:13px}
.h1s{font-size:clamp(28px,4vw,44px)}
.svcrow{display:flex;justify-content:space-between;gap:24px;padding:26px 0;border-top:1px solid var(--line)}.svcrow h2{font-size:22px}
.price{font-family:Unbounded;font-weight:700;white-space:nowrap;color:var(--acc)}
.pg{margin-top:36px}.ptable{border:1px solid var(--line);border-radius:var(--r);background:var(--card);overflow:hidden}
.prow{display:grid;grid-template-columns:1fr 110px 130px;gap:14px;padding:16px 20px;border-top:1px solid var(--line);align-items:center}.prow:first-child{border-top:0}
.prow span{display:block;color:var(--mut);font-size:14px}.pt{color:var(--mut);font-size:14px}.pp{font-family:Unbounded;font-weight:700;text-align:right}
.note{background:#fff3ec;border:1px solid #f1c7b4;border-radius:var(--r);padding:18px 22px;margin:26px 0}
.steps{list-style:none;padding:0;counter-reset:s}.steps li{display:flex;gap:18px;padding:18px 0;border-top:1px solid var(--line)}
.steps b{font-family:Unbounded;color:#fff;background:var(--ink);width:38px;height:38px;border-radius:50%;display:grid;place-items:center;flex:none}
.steps h3{margin-bottom:.2em}.steps p{margin:0;color:var(--mut)}
.form{background:var(--card);border:1px solid var(--line);border-radius:var(--r);padding:24px}
.form label{display:block;margin-bottom:14px;font-size:14px;font-weight:600}
.form input,.form textarea{display:block;width:100%;margin-top:6px;padding:12px 14px;border:1px solid var(--line);border-radius:12px;font:inherit;background:#fff}
.crumbs{font-size:14px;color:var(--mut)}.meta{color:var(--mut)}
.prose h2{font-size:24px;margin-top:1.6em}.prose p,.prose li{font-size:18px}.prose ul,.prose ol{padding-left:1.2em}.prose li{margin:.4em 0}
.example{background:#eaf2ee;border-left:4px solid var(--grn);padding:16px 20px;border-radius:0 14px 14px 0;margin:28px 0;font-size:17px}
.cmp{width:100%;border-collapse:collapse;margin:18px 0;font-size:16px}.cmp th,.cmp td{border:1px solid var(--line);padding:10px 12px;text-align:left;background:var(--card)}.cmp th{background:#ebe6da}
@media(max-width:900px){
 .hero-in,.split,.grid3,.grid4{grid-template-columns:1fr}.tel{display:none}
 .burger{display:block;margin-left:auto}nav{display:none;position:absolute;top:68px;left:0;right:0;background:var(--bg);flex-direction:column;padding:12px 20px 20px;border-bottom:1px solid var(--line);gap:6px}
 body.menu nav{display:flex}.prow{grid-template-columns:1fr auto}.pt{display:none}.svcrow{flex-direction:column}
}
'''
JS = r'''
function sendForm(f){
  var d=new FormData(f);
  var body="Ім'я: "+d.get("name")+"\nТелефон: "+d.get("phone")+"\nАвто: "+d.get("car")+"\n\n"+(d.get("msg")||"");
  location.href="mailto:"+(window.__EMAIL||"")+"?subject="+encodeURIComponent("Оцінка ремонту ЛКП")+"&body="+encodeURIComponent(body);
  return false;
}
document.querySelectorAll("nav a").forEach(function(a){a.addEventListener("click",function(){document.body.classList.remove("menu")})});
'''

def static():
    os.makedirs(os.path.join(OUT,"assets"), exist_ok=True)
    open(os.path.join(OUT,"assets/style.css"),"w",encoding="utf-8").write(CSS)
    open(os.path.join(OUT,"assets/main.js"),"w",encoding="utf-8").write(JS)
    pages = ["index.html","uslugy.html","tsiny.html","yak-ce-pratsyuye.html","materialy.html","pro-nas.html","kontakty.html","blog/index.html"]
    urls = [(f"{DOMAIN}/{p}", "2026-10-23") for p in pages] + [(f"{DOMAIN}/blog/{a['slug']}.html", a["date"]) for a in ARTICLES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{u}</loc><lastmod>{d}</lastmod></url>\n" for u,d in urls) + "</urlset>\n"
    open(os.path.join(OUT,"sitemap.xml"),"w",encoding="utf-8").write(sm)
    open(os.path.join(OUT,"robots.txt"),"w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")

if __name__ == "__main__":
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    static(); home(); uslugy(); tsiny(); process(); materials(); about(); contacts(); blog(); notfound()
    print("OK", len(ARTICLES), "articles")
