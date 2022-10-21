import json
import os

# прикольно было бы с параметром запускать этот скрипт: 1 или 2
def readJson(key):
    with open("data.json", "r") as file:
        rawJson = file.read()
        data = json.loads(rawJson)
        return data[key]

def writeToJson(key, value):
    with open("data.json", "r+") as file:
        rawJson = file.read()
        data = json.loads(rawJson)
        data[key] = value
        newJson = json.dumps(data, indent=4)
        file.seek(0)
        file.write(newJson)
        file.truncate()


def setStagingConfig():
    configPath = readJson("configPath") 
    if configPath == "":
        cashboxPath = readJson("cashboxDirPath")
        bin = os.path.join(cashboxPath, "bin")
        for root, dirs, files in os.walk(bin):
            configPath = os.path.join(root, dirs[0], "cashboxService.config.json")
            break
        writeToJson("configPath", configPath)


    with open(configPath, "r+") as file:
        rawJson = file.read()
        data = json.loads(rawJson)
        data["settings"][0]["loyaltyCashboxClientUrl"] = "https://market.testkontur.ru/loyaltyCashboxApi"
        newJson = json.dumps(data, indent=4)
        file.seek(0)
        file.write(newJson)
        file.truncate()

setStagingConfig()

