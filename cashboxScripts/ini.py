import os
import json

def findDir(path, dir):
    for root, dirs, files in os.walk(path):
        if (dir in dirs):
            return os.path.join(root, dir)
        break # ищем только по первому уровню вложенности
    return "" 

def getPossibleKonturPaths():
    paths = []
    for diskDrive in "C:\\", "D:\\", "F:\\":
        paths.append(os.path.join(diskDrive, "Program Files"))
        paths.append(os.path.join(diskDrive, "Program Files (x86)"))
    return paths

def findCashboxDirPath():
    for path in getPossibleKonturPaths():
        dir = findDir(path, "SKBKontur")
        if dir != "":
            return os.path.join(path, "SKBKontur", "Cashbox")
    return "" 
    # надо выбросить ошибку, мы не нашли вообще папку SKBKontur. Возможно, надо добавить в метод свой диск

def writeToJson(key, value):
    with open("data.json", "r+") as file:
        rawJson = file.read()
        data = json.loads(rawJson)
        data[key] = value
        newJson = json.dumps(data, indent=4)
        file.seek(0)
        file.write(newJson)
        file.truncate()
def readJson(key):
    with open("data.json", "r") as file:
        rawJson = file.read()
        data = json.loads(rawJson)
        return data[key]
    #ошибка

cashboxDirPath = findCashboxDirPath()
writeToJson("cashboxDirPath", cashboxDirPath)

cashbox = readJson("cashboxDirPath")
bin = os.path.join(cashbox, "bin")
js = ""
for root, dirs, files in os.walk(bin):
    js = os.path.join(root, dirs[0], "cashboxService.config.json")
    break
writeToJson("configPath", js)
print(js)






    



        #  result.append(os.path.join(root, filename))

# import os, fnmatch


# def findCashboxFolder(name, path):
#     result = []
#     for root, dirs, files in os.walk(path):
#         if name in files:
#             result.append(os.path.join(root, name))
#     return result

# files = findCashboxFolder("cashboxService.config.json", 'C:')
# print(files[0])


