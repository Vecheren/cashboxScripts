#NoEnv  
#Warn  
SendMode Input  
SetWorkingDir %A_ScriptDir% 


!1::
Run, setFirstStaging.py
MsgBox, "You have switched to staging-1"
return

!2::
Run, setSecondStaging.py
MsgBox, "You have switched to staging-2"
return

!s:: 
Run, stop.py
MsgBox, "SKBKontur.Cashbox stopped"
return

!r:: 
Run, start.py
MsgBox, "SKBKontur.Cashbox started"
return

!k::
Run, deleteDb.py
MsgBox, "You have deleted db"
return

#k::
Run, deleteCashbox.py
MsgBox, "You have deleted KMK"
return



