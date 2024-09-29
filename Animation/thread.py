
""" import threading
import time

def type_numbers():
    for k in range(1,10):
        print(k)
        time.sleep(1)

def print_numbers():
    for cell in ['3','1','4','2','1','3','2','4','3']:
        print(cell)
        time.sleep(1)

thread1=threading.Thread(target=type_numbers)
thread2=threading.Thread(target=print_numbers)

thread1.start()
thread2.start()

thread1.join()
thread2.join() """


""" import threading
import time

def numbers():
    for t in range(1,16):
        print(t)
        time.sleep(1)

def letters():
    for word in ['a','b','c','d','c','a','d','b','a','d','b','c','a','d','c']:
        print(word)
        time.sleep(1)

thread1=threading.Thread(target=numbers)

thread2=threading.Thread(target=letters)

thread1.start()

thread2.start()

thread2.join()

thread1.join()

print("both thread have finished")
 """


import threading
import time

def first_name():
    for firstname in ("santhosh","anbu","kabilan"):
        print(firstname)
        time.sleep(1)

def last_name():
    for nickname in ["sandy","praveen","arun"]:
        print(nickname)
        time.sleep(1)

thread1=threading.Thread(target=first_name)
thread2=threading.Thread(target=last_name)

thread1.start()
thread2.start()

thread2.join()
thread1.join()
        
