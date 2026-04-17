#1. Write an application that prompts the user to enter a sequence of integer numbers. If the user enters a number that has already been entered before, the application should print all the numbers entered previously and terminate.

a = set()
num = int(input("enter and integer: "))

while True:
    if num in a:
        print(f"You have entered {a} before")
        break
    else:
        a.add(num)
        num = int(input("enter and integer: "))
    
