import os
import shutil
from subprocess import check_output

try:
    check_output("net start SKBKontur.Cashbox", shell=True)
except Exception: 
    pass







