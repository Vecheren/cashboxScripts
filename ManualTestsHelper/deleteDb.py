import os
from helpers import fileshelper
import subprocess

try:
    subprocess.call(['sc', 'stop', 'SKBKontur.Cashbox'])
except:
    pass
cashboxPath = fileshelper.findCashboxPath()
dbPath = os.path.join(cashboxPath, "db")
fileshelper.deleteFolder(dbPath)