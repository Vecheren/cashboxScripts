import os
from subprocess import check_output
import helper

cashboxPath = helper.findCashboxPath()
dbPath = os.path.join(cashboxPath, "db")
check_output("net stop SKBKontur.Cashbox", shell=True)
helper.deleteFolder(dbPath)




