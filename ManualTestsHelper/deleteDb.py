import os
from helpers import fileshelper
import subprocess

fileshelper.stopCashbox()
cashboxPath = fileshelper.findCashboxPath()
dbPath = os.path.join(cashboxPath, "db")
fileshelper.deleteFolder(dbPath)