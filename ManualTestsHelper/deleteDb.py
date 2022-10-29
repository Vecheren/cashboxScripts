import os
import fileshelper
from subprocess import check_output

check_output("net stop SKBKontur.Cashbox", shell=True)
cashboxPath = fileshelper.findCashboxPath()
dbPath = os.path.join(cashboxPath, "db")
fileshelper.deleteFolder(dbPath)