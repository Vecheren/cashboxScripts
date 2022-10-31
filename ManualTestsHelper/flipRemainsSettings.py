import nethelper
import fileshelper
import json

cashboxId = fileshelper.readJsonValue("cashboxId")
session = nethelper.startSession()
settings = nethelper.getCashoxSettingsJson(session, cashboxId)
moveRemainsToNextShift = settings["settings"]["backendSettings"]["moveRemainsToNextShift"]
settings["settings"]["backendSettings"]["moveRemainsToNextShift"] = False if moveRemainsToNextShift == True else True
result = {}
result["Settings"] = settings["settings"]["backendSettings"]
result["PreviousVersion"] = settings["versions"]["backendVersion"]
nethelper.postCashboxSettings(session, cashboxId, json.dumps(result))

