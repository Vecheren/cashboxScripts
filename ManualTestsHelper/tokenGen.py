from helpers import nethelper
from helpers import fileshelper

cashboxId = fileshelper.readJsonValue("cashboxId")
session = nethelper.startSession()
nethelper.genToken(session, cashboxId)
