import os
import shutil
from subprocess import check_output

def DeleteFolder(filePath = r"C:\Program Files (x86)\SKBKontur\Cashbox\db"):
    if os.path.isdir(filePath):
        shutil.rmtree(filePath)
        print("db has been deleted")
    else: 
        print("db not found")

try:
    check_output("net stop SKBKontur.Cashbox", shell=True)
except Exception: 
    pass

DeleteFolder(r"C:\Program Files (x86)\SKBKontur\Cashbox\db")
# DeleteFolder(r"C:\Program Files (x86)\SKBKontur\Cashbox\bin")





