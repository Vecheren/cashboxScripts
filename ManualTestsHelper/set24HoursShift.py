from helpers import fileshelper
import json


shift = fileshelper.getLastShiftFromSQL()
shiftJson = json.loads(shift)
shiftJson["openInfo"]["openDateTime"] = "2022-11-03 22:39:30.5000103"
result = json.dumps(shiftJson)
fileshelper.editShiftInDB(result)
fileshelper.startCashbox()