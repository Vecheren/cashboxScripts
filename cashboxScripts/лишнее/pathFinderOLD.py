import os 
import json

def findDir(path, dir):
    for root, dirs, files in os.walk(path):
        if dir in dirs:
            return os.path.join(root, dir)
        break
    return ""
 
def findCashboxDir():
    ProgramFiles = findDir("C:\\", 'Program Files')
    ProgramFilesx86 = findDir("C:\\", 'Program Files (x86)')
    for path in ProgramFiles, ProgramFilesx86:
        if (path != ""):
             konturDir = findDir(path, "SKBKontur")
             if (konturDir != ""): 
                 return os.path.join(konturDir, "Cashbox")
    return ""
    
def addKonturDirToDataJson():
        cashboxPath = findCashboxDir()
        with open("data.json", "r+") as file:
            rawJson = file.read()
            data = json.loads(rawJson)
            data["cashboxPath"] = cashboxPath
            newJson = json.dumps(data, indent=4)
            file.seek(0)
            file.write(newJson)
            file.truncate()

addKonturDirToDataJson()