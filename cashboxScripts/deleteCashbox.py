import os
import shutil
from subprocess import check_output
import json

def writeToJson(key, value):
    with open("data.json", "r+") as file:
        rawJson = file.read()
        data = json.loads(rawJson)
        data[key] = value
        newJson = json.dumps(data, indent=4)
        file.seek(0)
        file.write(newJson)
        file.truncate()

def DeleteFolder(filePath):
    if os.path.isdir(filePath):
        shutil.rmtree(filePath)
        print("dir has been deleted")
    else: 
        print("dir not found")

try:
    check_output("net stop SKBKontur.Cashbox", shell=True)
except Exception: 
    pass


DeleteFolder(r"C:\Program Files (x86)\SKBKontur\Cashbox")
DeleteFolder(r"C:\Users\mnoskov\AppData\Roaming\SkbKontur")
writeToJson("configPath", "")




    



