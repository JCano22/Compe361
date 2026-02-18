h = 7
b = h > 0 or 1 / h + h/(h-7) > 1   
print(b) #prints True

p = '123'
q = '25'
r = p + q
print(r)
#prints 12325

n = int(input())
sum = 0
while(n != 0):
    sum += (n % 10)
    n //= 10

print(sum)