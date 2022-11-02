from subprocess import check_output
import fileshelper

try:
    check_output("net stop SKBKontur.Cashbox", shell=True)
except:
    pass
cashboxPath = fileshelper.findCashboxPath()
fileshelper.deleteFolder(cashboxPath)
fileshelper.writeJsonValue("configPath", "")