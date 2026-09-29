Как импортировать в Google Ads Editor
1. Editor → Аккаунт → Импорт → Из файла (или вставить из буфера). Выбрать файл.
2. Editor покажет предпросмотр: столбцы уже названы как в Editor (Campaign, Ad Group, Keyword, Criterion Type, Final URL, Status).
3. Проверить, что ошибок нет, нажать «Завершить», затем «Опубликовать».

Порядок:
  01_minus_slova_editor.csv        — минус-слова P0 и P1 во все кампании (строки «решение» из CSV 01 сюда не входят).
  03_pauza_editor.csv              — поставить на паузу фразовые ключи из CSV 03.
  03_dobavit_tochnye_editor.csv    — добавить точные версии вместо фразовых (только те, которых в группе ещё нет).
  02_klyuchi_editor.csv            — новые точные ключи из запросов с конверсиями (без brand-кампании — её создать вручную по CSV 02).

Перед импортом 02: в CHICAGO Lux ключ [sub zero authorized repair] заработает только после удаления минусов «authorized», «authorized repair», «authorized service» (см. CSV 08).
