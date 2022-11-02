ManualTestsHelper - скрипты, которые автоматизируют рутинные действия при проверках на виндовой кассе.

Сами скрипты написаны на питоне, а запускаются горячими клавишами благодаря AutoHotKey.

## Как запустить

1. Установите питон третьей версии. Обязательно поставьте галочку в "Добавить в Path". https://www.python.org/downloads/
2. Запустите libinstaller.bat. Он установит две библиотеки, которые нам понадобятся
3. В файле data.json: убедитесь, что перечислен ваш жесткий диск, на котором лежит Касса. И добавьте id текущей кассы.
4. Запустите CashboxHotkeys.ahk от администратора (так все скрипты тоже будут запускаться от администратора)

## Как пользоваться

После запуска файла .ahk можно нажимать на горячие клавиши.

:white_check_mark: Остановка службы SKBKontur.Cashbox - ALT + стрелка вниз

:white_check_mark: Запуск службы SKBKontur.Cashbox - ALT + стрелка вверх

:white_check_mark: Удаление базы данных кассы - ALT + D

:white_check_mark: Удаление кассы - ALT + C

:white_check_mark: Генерация нового токена - ALT + T

:white_check_mark: Переключение на стейджинг-1 - ALT + 1

:white_check_mark: Переключение на стейджинг-2 - ALT + 2

:white_check_mark: Изменение настройки переноса остатков - ALT + O

Также работает автозамена строк. Просто напишите ключ где угодно, например, в строке браузера - подставится значение:

:white_check_mark: adm1 - https://market.testkontur.ru/AdminTools

:white_check_mark: adm2 - https://market-dev.testkontur.ru/AdminTools

:white_check_mark: cashdoc - https://cashdoc.kontur/webdav/cashbox/

:white_check_mark: csadm - https://market.kontur.ru/cashboxApi/admin/web/cashbox/


Расширяйте набор скриптов и горячих клавиш по аналогии и подстраивайте их под себя. 

