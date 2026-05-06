#6.    Write a Python program that concurrently calls two functions in separate threads. Each function should increment a shared global variable by a specified amount in a loop. Use a Lock object to prevent simultaneous access to the shared variable during updates.from threading import Thread
from threading import Thread


