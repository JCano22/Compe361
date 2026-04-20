#1. Write an application that prompts the user to enter a sequence of integer numbers. If the user enters a number that has already been entered before, the application should print all the numbers entered previously and terminate.

s = set()

while True:
    a = int(input("Enter a number: "))
    if a in s:
        print("Here are previously entered numbers: ", s)
        break
    else:
        s.add(a)
