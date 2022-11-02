import threading
import time
a = 0
def son():
    for x in range (0,150):
        time.sleep(0.1)
        print(x)
        if a == 50:
           break

def son1():
    for x in range(0,150):
        time.sleep(0.1)
        print(x)
        if a == 100:
           break
def son2():
    for x in range(0,150):
        time.sleep(0.1)
        print(x)
        if a == 150:
            break
t1 = threading.Thread(target=son)
t2 = threading.Thread(target=son1)
t3 = threading.Thread(target=son2)

t1.start()
t2.start()
t3.start()

