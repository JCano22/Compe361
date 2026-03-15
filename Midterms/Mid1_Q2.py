# 2.    Create a Python function that takes three numbers as arguments and returns their product. If any of these numbers is zero or None, it should be excluded from the multiplication. Provide an example of calling this function.

def prod(a, b, c):
    p = 1
    for n in (a,b,c):
        if n not in (0, None):
            p *= n
    
    return p

print(prod(1,2,10))
