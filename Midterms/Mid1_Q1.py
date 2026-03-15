#1.    Create a Python application which will ask the user to enter integer number between 0 and 100 and which will print the corresponding letter grade according to the following grading scheme:

#Number    Letter Grade
#94-100     A
#90-93      A-
#87-89    B+
#84-86    B
#80-83    B-
#77-79    C+
#74-76    C
#70-73    C-
#0-69    F

while True:
    try:
        grade = int(input("Enter a grade: "))
        if grade >= 0 and grade <= 100:
            break
        else:
            print("Number must be between 0 and 100.")
    except ValueError:
        print("Please enter and integer.")

n = input("what is your name: ")
if grade >= 94:
    print(f"{n} got an A")
elif grade >= 90:
    print(f"{n} got an A-")
elif grade >= 87:
    print(f"{n} got a B+")
elif grade >= 84:
    print(f"{n} got a B")
elif grade >= 80:
    print(f"{n} got a B-")
elif grade >= 77:
    print(f"{n} got a C+")
elif grade >= 74:
    print(f"{n} got a C")
elif grade >= 70:
    print(f"{n} got a C-")
else:
    print(f"{n} got an F")

