#1. Write an application that prompts the user to enter a sequence of integer numbers. If the user enters a number that has already been entered before, the application should print all the numbers entered previously and terminate.

a = set()

while True:
    num = int(input("enter a number: "))
    if num not in a:
        a.add(num)
    else:
        print("Here are the previously entered numbers: ", a)
        break
