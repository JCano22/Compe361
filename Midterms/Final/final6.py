#6.    Write a Python program that concurrently calls two functions in separate threads. Each function should increment a shared global variable by a specified amount in a loop. Use a Lock object to prevent simultaneous access to the shared variable during updates.from threading import Thread
import threading, time

def add_three():
    global n
    lck.acquire()
    n += 3
    lck.release()

def add_two():
    global n 
    lck.acquire()
    n += 2
    lck.release()

n = 100

thrd1 = threading.Thread(target = add_three)
thrd2 = threading.Thread(target = add_two)

lck = threading.Lock()

thrd1.start()
thrd2.start()

thrd1.join()
thrd2.join()

print(n)
