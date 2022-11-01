from helpers import fileshelper
import subprocess

subprocess.call(['sc', 'stop', 'SKBKontur.Cashbox'])
cashboxPath = fileshelper.findCashboxPath()
fileshelper.deleteFolder(cashboxPath)
fileshelper.writeJsonValue("configPath", "")