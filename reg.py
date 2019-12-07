import os
import winreg as reg
import time

pth = os.path.dirname(os.path.realpath(__file__)) 
# name of the python file with extension 
s_name="reg.py"

# joins the file name to end of path address 
address=os.path.join(pth,s_name) 
      
# key we want to change is HKEY_CURRENT_USER  
# key value is Software\Microsoft\Windows\CurrentVersion\Run 
key = reg.HKEY_CURRENT_USER
key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
      
# open the key to make changes to 
open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS) 
      
# modifiy the opened key 
reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address) 
      
# now close the opened key 
reg.CloseKey(open)
timer = 0
while True :
    time.sleep(10)
    timer += 1
    print ('hello  ...>>',timer)
