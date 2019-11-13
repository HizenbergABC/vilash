import time
from random import randint
timer = 0

while True :
    timer += 1
    try:
        name_file = randint(1,500)
        time.sleep(1)
        fh = open("I:%i"% name_file, 'a')
        fh.write("Foobar 2")
        fh.close()
    except:
        pass
    print('time of ruinig >>',timer)
