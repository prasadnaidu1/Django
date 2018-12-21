from threading import *
from time import *

def fun1(self):
    for i in range(1,10):
        print(i)
        sleep(2)
def fun2(self):
    while True:
        print("hello")
        sleep(2)
#callinng block

t3=Thread(target=fun1)
t4=Thread(target=fun2)
t3.start()
t4.daemon=True
t4.start()
t4.join()

