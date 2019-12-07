import os
import winreg as reg
import time

pth = os.path.dirname(os.path.realpath(__file__))  
s_name="reg.py" 
address=os.path.join(pth,s_name) 
key = reg.HKEY_CURRENT_USER
key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address) 
reg.CloseKey(open)
timer = 0
while True :
    time.sleep(10)
    timer += 1
    print ('hello  ...>>',timer)
