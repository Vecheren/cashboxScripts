from subprocess import check_output
import fileshelper

check_output("net stop SKBKontur.Cashbox", shell=True)
cashboxPath = fileshelper.findCashboxPath()
fileshelper.deleteFolder(cashboxPath)
fileshelper.writeJsonValue("configPath", "")