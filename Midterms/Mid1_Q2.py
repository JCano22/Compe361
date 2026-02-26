# 2.    Create a Python function that takes three numbers as arguments and returns their product. If any of these numbers is zero or None, it should be excluded from the multiplication. Provide an example of calling this function.

def prod(a, b, c):
    p = 1
    for num in (a,b,c):
        if num not in (0, None):
            p *= num
    return p

num = prod(2, 0, 4)
print(num)
