#NoEnv  
#Warn  
SendMode Input  
SetWorkingDir %A_ScriptDir% 

 
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
Run, deleteCashBox.py
MsgBox, "You have deleted KMK"
return


!1::
Run, setFirstStaging.py
MsgBox, "You have switched to staging-1"
return

!2::
Run, setSecondStaging.py
MsgBox, "You have switched to staging-2"
return

!c:: 
Run, C:\ProgramData\SKBKontur\Cashbox\UIRunner\bin\1.0.1641.147\SKBKontur.Cashbox.UIRunner.exe 
return 
 
