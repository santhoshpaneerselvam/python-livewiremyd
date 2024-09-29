
"""import threading
import time

def print_numbers():
    for i in range(1,6):
        print(i)
        time.sleep(1)

thread1 = threading.Thread(target=print_numbers) 
thread2 = threading.Thread(target=print_numbers)
thread2.start()
thread1.start()
thread1.join()
thread2.join()   
""" 

"""import threading
import time
def numbers():
    for a in range(1,7):
        print(a)
        time.sleep(1)
def letters():
    for char in ['a','b','c','d','e','f']:
        print(char)
        time.sleep(1)
thread1=threading.Thread(target=numbers) 
thread2=threading.Thread(target=letters) 

thread1.start()
thread2.start()

thread2.join()
thread1.join()
print("both thread have finished")""" 



import threading
import time

def numbers():
    for i in range(1,7):
        print(i)
        time.sleep(1)

def letters():
    for char in ['a','b','c','d','e','f']:
        print(char) 
        time.sleep(1)

thread1=threading.Thread(target=numbers)

thread2=threading.Thread(target=letters)

thread1.start()

thread2.start()

thread2.join()

thread1.join()

print("both thread are finished")

