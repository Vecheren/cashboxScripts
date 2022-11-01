import nethelper
import fileshelper
import json

cashboxId = fileshelper.readJsonValue("cashboxId")
session = nethelper.startSession()
settings = nethelper.getCashoxSettingsJson(session, cashboxId)
settings = json.loads(settings)
moveRemainsToNextShift = settings["settings"]["backendSettings"]["moveRemainsToNextShift"]
settings["settings"]["backendSettings"]["moveRemainsToNextShift"] = False if moveRemainsToNextShift == True else True
result = {}
result["settings"] = settings["settings"]["backendSettings"]
result["previousVersion"] = settings["versions"]["backendVersion"]
nethelper.postCashboxSettings(session, cashboxId, result)