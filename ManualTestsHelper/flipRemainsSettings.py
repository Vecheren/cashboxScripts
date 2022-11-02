from helpers import nethelper
from helpers import fileshelper
import json

cashboxId = fileshelper.readJsonValue("cashboxId")
session = nethelper.startSession()
settings = nethelper.getCashoxSettingsJson(session, cashboxId)
flippedSettings = nethelper.prepareFlippedRemainsSettings(settings)
nethelper.postCashboxSettings(session, cashboxId, flippedSettings)