import random

trials = 100000        
students = 50         
shared_count = 0      

for _ in range(trials):
    birthdays = []

    # generate birthdays
    for _ in range(students):
        day = random.randint(1, 365)
        birthdays.append(day)

    # check if there is at least one match
    if len(birthdays) != len(set(birthdays)):
        shared_count += 1

# estimated probability
probability = shared_count / trials
print("Estimated probability:", probability)
