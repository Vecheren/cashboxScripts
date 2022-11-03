from helpers import fileshelper
import time

fileshelper.stopCashbox()
cashboxPath = fileshelper.findCashboxPath()
time.sleep(2)
fileshelper.deleteFolder(cashboxPath)
