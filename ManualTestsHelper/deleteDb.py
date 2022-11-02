import os
import fileshelper
from subprocess import check_output

try:
    check_output("net stop SKBKontur.Cashbox", shell=True)
except:
    pass
cashboxPath = fileshelper.findCashboxPath()
dbPath = os.path.join(cashboxPath, "db")
fileshelper.deleteFolder(dbPath)