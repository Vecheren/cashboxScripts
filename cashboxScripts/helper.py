import os
import shutil
import json

def deleteFolder(filePath):
    assert os.path.isdir(filePath)
    shutil.rmtree(filePath)

def getProgramFilesPaths():
    paths = []
    for diskDrive in readJsonValue("diskDrives"):
        paths.append(os.path.join(diskDrive, "Program Files"))
        paths.append(os.path.join(diskDrive, "Program Files (x86)"))
    return paths

def findCashboxPath():
    cashboxPath = readJsonValue("cashboxPath")
    if cashboxPath != "": 
        return cashboxPath
    for path in getProgramFilesPaths():
        dir = findChildDirPath(path, "SKBKontur")
        if dir != "":
            cashboxPath = os.path.join(path, "SKBKontur", "Cashbox")   
    assert cashboxPath != "", "Can't find Cashbox. Try to add your Disk Drive names to data.json" 
    writeJsonValue("cashboxPath", cashboxPath)
    return cashboxPath

def findConfigPath():
    configPath = readJsonValue("configPath")
    if configPath != "":
        return configPath
    cashbox = findCashboxPath()
    bin = os.path.join(cashbox, "bin")
    for root, dirs, files in os.walk(bin):
        configPath = os.path.join(root, dirs[0], "cashboxService.config.json")
        break
    assert configPath != "", "Can't find config path"
    writeJsonValue("configPath", configPath)
    return configPath

def setStaging(stagingNumber):
    configPath = findConfigPath()
    try: 
        changeStagingInConfig(stagingNumber, configPath)
    except FileNotFoundError: # на случай, если удаляли кассу не скриптом
        writeJsonValue("configPath", "")
        configPath = findConfigPath()
        changeStagingInConfig(stagingNumber, configPath)

def changeStagingInConfig(stagingNumber, configPath):
    with open(configPath, "r+") as file:
        rawJson = file.read()
        data = json.loads(rawJson)
        if stagingNumber == 2:
            data["settings"][0]["loyaltyCashboxClientUrl"] = "https://market-dev.testkontur.ru/loyaltyCashboxApi"
        else: 
            data["settings"][0]["loyaltyCashboxClientUrl"] = "https://market.testkontur.ru/loyaltyCashboxApi"
        newJson = json.dumps(data, indent=4)
        file.seek(0)
        file.write(newJson)
        file.truncate()    


def findChildDirPath(path, dir):
    for root, dirs, files in os.walk(path):
        if (dir in dirs):
            return os.path.join(root, dir)
        break 
    return "" 

def writeJsonValue(key, value, path = "data.json"):
    with open(path, "r+") as file:
        rawJson = file.read()
        data = json.loads(rawJson)
        data[key] = value
        newJson = json.dumps(data, indent=4)
        file.seek(0)
        file.write(newJson)
        file.truncate()

def readJsonValue(key, path = "data.json"):
    with open(path, "r") as file:
        rawJson = file.read()
        data = json.loads(rawJson)
        assert key in data, f"Key {key} not in {path}"
        return data[key]
        
# чтобы найти вложенное поле, сюда можно докинуть поиск по графу типа DFS или BFS