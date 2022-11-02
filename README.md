ManualTestsHelper - скрипты, которые автоматизируют рутинные действия при проверках на виндовой кассе.

Сами скрипты написаны на питоне, а запускаются горячими клавишами благодаря AutoHotKey.

## Как запустить

1. Установите питон третьей версии. Обязательно поставьте галочку в "Добавить в Path". https://www.python.org/downloads/
2. Запустите libinstaller.bat. Он установит две библиотеки, которые нам понадобятся
3. В файле data.json: убедитесь, что перечислен ваш жесткий диск, на котором лежит Касса. И добавьте id текущей кассы.
4. Запустите CashboxHotkeys.ahk от администратора (так все скрипты тоже будут запускаться от администратора)

## Как пользоваться

После запуска файла .ahk можно нажимать на горячие клавиши.

| Горячие клавиши | Действие | Пояснение|
|----:|:----:|:----------|
| ALT + стрелка вниз ↓  | Остановка службы SKBKontur.Cashbox |  |
| ALT + стрелка вверх | Запуск службы SKBKontur.Cashbox |  |
|ALT + D |Удаление базы данных кассы | Служба остановится, папка db будет удалена |
|ALT + C | Удаление кассы | Служба установится, папка Cashbox будет удалена |
|ALT + T| Генерация нового токена| Код активации сгенерируется для кассы, которая указана в файле data.json |
| ALT + 1|Переключение на стейджинг-1 | В конфиге адрес лояльности заменится на: market.testkontur... |
|ALT + 2 |Переключение на стейджинг-2  | В конфиге адрес лояльности заменится на: market-dev.testkontur... |
|ALT + O |Изменение настройки переноса остатков | MoveRemainsToNextShift - заменяем настройку с тру на фолс или с фолс на тру |

Также работает автозамена строк. Просто напишите ключ где угодно, например, в строке браузера - подставится значение:

:white_check_mark: adm1 - https://market.testkontur.ru/AdminTools

:white_check_mark: adm2 - https://market-dev.testkontur.ru/AdminTools

:white_check_mark: cashdoc - https://cashdoc.kontur/webdav/cashbox/

:white_check_mark: csadm - https://market.kontur.ru/cashboxApi/admin/web/cashbox/

____

:cat: *Расширяйте набор скриптов и горячих клавиш по аналогии и подстраивайте их под себя. Или хотя бы расказывайте, чего не хватает :)* 

