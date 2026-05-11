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

def g(p):
    return pow(p, 3)

a = 2
b = 14

Echo(a,b,g)
