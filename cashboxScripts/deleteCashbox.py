import helper
from subprocess import check_output

check_output("net stop SKBKontur.Cashbox", shell=True)
cashboxPath = helper.findCashboxPath()
helper.deleteFolder(cashboxPath)
helper.writeJsonValue("configPath", "")

    



