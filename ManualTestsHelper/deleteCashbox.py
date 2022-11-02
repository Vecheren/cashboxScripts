from helpers import fileshelper
import subprocess

fileshelper.stopCashbox()
cashboxPath = fileshelper.findCashboxPath()
fileshelper.deleteFolder(cashboxPath)
fileshelper.writeJsonValue("configPath", "")