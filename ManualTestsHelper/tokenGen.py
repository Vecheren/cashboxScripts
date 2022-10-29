import nethelper
import helper

cashboxId = helper.readJsonValue("cashboxId")
session = nethelper.startSession()
nethelper.genToken(session, cashboxId)
