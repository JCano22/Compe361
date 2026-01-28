num = int(input('Please input a number: '))

if num == 0:
    num = int(input('Please input a non-zero number: '))

print('positive' if (num > 0) else 'negative')
