import os
import shutil
from subprocess import check_output

try:
    check_output("net stop SKBKontur.Cashbox", shell=True)
except Exception: 
    pass







