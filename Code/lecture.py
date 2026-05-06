

numbers = [45, 12, 78, 34, 91, 56, 23, 67, 89, 11,
    72, 38, 55, 19, 84, 61, 47, 30, 93, 66,
    14, 52, 77, 41, 28, 85, 63, 96, 7, 39,
    50, 182, 17, 73, 44, 99, 26, 58, 35, 80,
    9, 164, 21, 88, 53, 37, 76, 199, 42, 15,
    69, 31, 95, 48, 83, 22, 57, 74, 6, 90,
    33, 70, 46, 13, 87, 60, 25, 79, 43, 98,
    18, 51, 86, 29, 165, 40, 97, 8, 62, 36,
    75, 20, 49, 92, 16, 54, 181, 113, 71, 27,
    59, 94, 10, 68, 32, 5, 88, 24, 41, 73]

maxNum = numbers[0]
secMax = -1

for x in numbers:
    if x > maxNum:
        secMax = maxNum
        maxNum = x
    elif x > secMax and x != maxNum:
        secMax = x

print("The largest number is:", maxNum)
print("The second largest number is:", secMax)
    