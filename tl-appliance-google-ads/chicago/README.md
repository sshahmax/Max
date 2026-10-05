# TL Appliance Repair — Google Ads, Chicago (новая кампания с нуля)

Домен: https://tappliancerepair.site/chicago/
Собрано: 2026-10-05. Формат — экспорт Google Ads Editor (те же колонки, что в файлах TOL).

## Файлы (порядок импорта важен)

| # | Файл | Что внутри |
|---|------|------------|
| 1 | `TL_CHI_01_MAIN_campaign_adgroups_keywords_ads_assets.csv` | кампания, 37 групп, 2 294 ключа, 74 RSA, 10 сайтлинков, 10 уточнений, звонок |
| 2 | `TL_CHI_02_LOCATIONS.csv` | 277 гео: Chicago, Cook / DuPage / Lake counties + районы и пригороды |
| 3 | `TL_CHI_03_NEGATIVES.csv` | 519 минус-слов уровня кампании |

Импорт: Google Ads Editor → Account → Import → From file. Сначала 01, затем 02, затем 03.
Кампания импортируется со статусом **Paused** — включить после проверки телефона и URL.

## Структура

Одна кампания `TL-CHI | Luxury Appliance Repair` (Search, только поиск Google, без партнёров).

Группы объявлений (каждая ведёт на свою страницу сайта `/chicago/<бренд>/<услуга>/`):

- **Sub-Zero (10):** Fridge Repair · Not Cooling · Freezer · Ice Maker · Wine Storage · Leaks & Frost · Compressor & Sealed System · Installation & Replacement · Series & Models · Brand & Areas
- **Wolf (7):** Range · Wall Oven · Rangetop · Cooktop · Steam Oven · Outdoor Grill · Brand & Areas
- **Viking (7):** Refrigerator · Range · Cooktop & Rangetop · Wall Oven · Wine Cellar · Ice Maker · Brand & Areas
- **Miele (6):** Washer · Dryer · Oven & Steam Oven · Refrigerator · Wine Cooler · Brand & Areas
- **Thermador (6):** Refrigerator · Range · Cooktop · Wall Oven · Wine Column · Brand & Areas
- **Luxury & Built-In > All Brands (1):** «luxury / high end / built in appliance repair» → `/chicago/`

Группы «Brand & Areas» содержат ключи «бренд + район/пригород» (Lincoln Park, Gold Coast, Evanston, Winnetka, Hinsdale, Naperville и ещё ~50) — только точное соответствие.

## Ключевые слова

- Каждый ключ — в Exact и Phrase (гео-комбинации — только Exact).
- Ни один ключ не повторяется в двух группах.
- Ни один ключ не пересекается с минус-словами (проверено скриптом).

## Объявления

- 74 RSA, по 2 в группе (вариант A и B с разными доказательствами/призывами).
- 15 заголовков + 4 описания в каждом. Закреплены только 2 заголовка на позиции 1 (бренд + услуга), описание 1 — на позиции 1. Остальное — свободная ротация.
- Без названия компании, без вставки ключевых слов `{KeyWord}` и без `{LOCATION}`.
- Тексты полностью новые: 0 совпадений и 0 близких совпадений (похожесть ≥ 0.8) с 296 объявлениями TOL.
- Все заявления подтверждаются сайтом: независимая компания, OEM-запчасти, цена согласуется до работы, диагностика идёт в зачёт ремонта, 90 дней гарантии на работу, телефон отвечает 24/7, same/next day в большинстве районов. Нет слов «authorized», «certified», «factory».

## Настройки кампании

| Параметр | Значение | Почему |
|---|---|---|
| Бюджет | $300/день | как у TOL Sub-Zero Chicago; поднять после первых конверсий |
| Стратегия | **Manual CPC**, ставки на уровне групп | у новой кампании нет истории конверсий; tCPA/Max Conv на старте раздувают CPC. Через 15–30 конверсий переключить на Maximize Conversions → tCPA |
| Max CPC | $42–44 Sub-Zero сервисные, $34–36 Wolf/Viking/Thermador сервисные, $30–38 Brand & Areas, $26 Luxury | |
| Гео | Location of presence (только находящиеся) | |
| Языки | All | |
| Final URL suffix | utm_source/medium/campaign/content/term + matchtype, device, network, targetid, loc | другие имена параметров, чем у TOL |
| Расписание | нет (телефон 24/7) | |

## ⚠️ Проверить перед запуском

1. **Телефон.** В звонковом ассете стоит **(847) 834-6513** — взят из `config/company.php` в присланном zip. Если у tappliancerepair.site другой номер — заменить в строке с `Phone number` (одна строка в файле 01) **до** импорта.
2. **URL.** Сайт tappliancerepair.site недоступен из среды, где собирались файлы, поэтому адреса страниц взяты из структуры присланного кода (`/chicago/sub-zero/refrigerator-repair/` и т. д.) и общих страниц `/pricing/`, `/warranty/`, `/contact/`. Перед импортом открыть 3–4 адреса из колонки `Final URL` и убедиться, что они отдают 200.
3. **Отслеживание конверсий** — убедиться, что на сайте стоят метки звонка и формы для нового аккаунта.

## Как пересобрать

Генератор — `build/build.py` + `build/descs.py` (тексты описаний). Требует рядом исходные файлы TOL
(`main.csv`, `loc.csv`, `neg.csv`) для проверки уникальности и списка гео. `python3 build.py` пишет три CSV в `out/`
и печатает отчёт: превышения длины, совпадения со старыми текстами, конфликты ключей с минус-словами.
