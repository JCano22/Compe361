#3.    Write a Python application which will ask the user to enter numbers until user enters negative number. After this application should print the three greatest numbers entered by user. Do not hold in memory all numbers entered by user simultaneously.
#For example, if the user enters:
#5, 8, 7, 2, 3, 8, 4, 5, 7, 2, 9, 0 
#then the following numbers should be printed:
#9, 8, 7 (printed numbers to not need to be sorted)


lst = []  # Using a list to store numbers

u = int(input("Enter a number (negative to stop): "))
while u >= 0:
    if len(lst) < 3:
        lst.append(u)
    else:
        lst.append(u)
        lst.sort()  # Sort the list in descending order
        lst.pop(0)  # Remove the smallest number (the first one after sorting)
    u = int(input("Enter a number (negative to stop): "))
for x in lst:
    print(x)

