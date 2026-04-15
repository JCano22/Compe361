#1. Write an application that prompts the user to enter a sequence of integer numbers. If the user enters a number that has already been entered before, the application should print all the numbers entered previously and terminate.

q = set()

u = int(input("Type a number: "))

while u not in q:
    q.add(u)
    u = int(input("Type a number: "))

for x in q:
    print(x)
