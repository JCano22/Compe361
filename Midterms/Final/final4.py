#4.    Write an application that opens an existing text file (with UTF-16 encoding) and replaces all bytes containing the symbol '!' with bytes containing the symbol '#' and vice versa. You are allowed to open the file only once, and you are permitted to read only two bytes from the file at a time.

f = open("//Users//jorgecano//Desktop//untitled.txt", "r+b")

ch = f.read(2)
while ch != b'':
    if ch == b'!\0':
        f.seek(-2, 1)
        print(ch)
        f.write(b'#\0')
    elif ch == b'#\0':
        f.seek(-2, 1)
        print(ch)
        f.write(b'!\0')
    ch = f.read(2)

f.close()