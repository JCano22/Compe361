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

def g(r):
    return r*r

print("======= Echo function with g(r) = r^2 =======")
x = 2
y = 3
z = 4

Echo(x, y, g)

Echo(x, z, lambda r: r * r) #lambda funcion is an anonymous function that can be defined in a single line. In this case, it takes an argument r and returns r squared.
