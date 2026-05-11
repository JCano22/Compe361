#3.    Write a Python application which will ask the user to enter numbers until user enters negative number. After this application should print the three greatest numbers entered by user. Do not hold in memory all numbers entered by user simultaneously.
#For example, if the user enters:
#5, 8, 7, 2, 3, 8, 4, 5, 7, 2, 9, 0 
#then the following numbers should be printed:
#9, 8, 7 (printed numbers to not need to be sorted)

num = int(input("Enter number: "))
a = []

while num >= 0:
    if len(a) < 3:
        a.append(num)
    else:
        a.append(num)
        a.sort()
        a.pop(0)
    num = int(input("Enter number: "))

print(a)


        
