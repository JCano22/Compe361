##1.    Suppose the following function is given:
#def Echo(a,b,f):
 #   k = a
 #   while k <= b:
  #      z=f(k)
 #       print(z)
 #       k+=1
#write a Python application code in which Echo function will be called.

def Echo(a,b,f):
    k = a
    while k <= b:
        z=f(k)
        print(z)
        k+=1

def g(x):
    return x**2

x = 2
y = 5
Echo(x,y,g)

Echo(1,10, lambda x: x + 1)