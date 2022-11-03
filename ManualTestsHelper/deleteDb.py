import os
from helpers import fileshelper
import time

fileshelper.stopCashbox()
cashboxPath = fileshelper.findCashboxPath()
dbPath = os.path.join(cashboxPath, "db")
time.sleep(2)
fileshelper.deleteFolder(dbPath)