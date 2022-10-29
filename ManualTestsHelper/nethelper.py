import requests
import sys
import json
import pyperclip
import random

def startSession():
    session = requests.session()
    session.auth = ('admin', 'psw')
    return session

def genToken(session: requests.Session, cashboxId):
    session.headers['Content-Type'] = "application/json"
    url = f"https://market.testkontur.ru:443/cashboxApi/backend/v1/cashbox/{cashboxId}/resetPassword"
    for i in range(5):
        token = str(random.randrange(11111111, 99999999))
        pyperclip.copy(f"{token}")
        data = json.dumps({"Token" : token})
        result = session.post(url, data = data)
        if result.ok: break

def getCashoxSettingsJson (session: requests.Session, cashboxId):
    response = session.get(f'https://market.testkontur.ru:443/cashboxApi/backend/v1/cashbox/{cashboxId}/settings')
    return json.loads(response.text)

def getSavedCashboxName(session: requests.Session, cashboxId):
    backendSettings = getCashoxSettingsJson(session, cashboxId)['settings']['backendSettings']
    return f"shop: {backendSettings['shopName']}, cashbox: {backendSettings['cashboxName']}"