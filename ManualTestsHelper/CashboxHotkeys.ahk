#NoEnv  
#Warn  
SendMode Input  
SetWorkingDir %A_ScriptDir% 


!Up:: 
Run, start.py
MsgBox, "Служба SKBKontur.Cashbox запущена"
return

!Down:: 
Run, stop.py
MsgBox, "Служба SKBKontur.Cashbox остановлена"
return

!1::
Run, setFirstStaging.py
MsgBox, "Касса готова к работе с первым стейджем"
return

!2::
Run, setSecondStaging.py
MsgBox, "Касса готова к работе со вторым стейджем"
return

!d::
Run, deleteDb.py
MsgBox, "Вы удалили БД кассы"
return

!c::
Run, deleteCashbox.py
MsgBox, "Вы удалили кассу"
return

!t::
Run, tokenGen.py
MsgBox, "Новый токен - в вашем буфере обмена"
return


:*:adm1:: https://market.testkontur.ru/AdminTools

:*:adm2:: https://market-dev.testkontur.ru/AdminTools

:*:cashdoc:: https://cashdoc.kontur/webdav/cashbox/

:*:csadm:: https://market.testkontur.ru/cashboxApi/admin/web/cashbox/
