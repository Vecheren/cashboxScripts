import os
import helper
from subprocess import check_output

check_output("net stop SKBKontur.Cashbox", shell=True)
cashboxPath = helper.findCashboxPath()
dbPath = os.path.join(cashboxPath, "db")
helper.deleteFolder(dbPath)