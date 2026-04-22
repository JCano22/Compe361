# 4. Write an application that reads each byte from a text file (ASCII encoding). If a byte contains a semicolon symbol, it should be replaced (in the same file) with a comma symbol.

f = open("/Users/jorgecano/Desktop/test.txt", "r+b")

b = f.read(1)

while b != b'':
    if b == b',':
        f.seek(-1, 1)
        f.write(b'!')
    b =f.read(1)

f.close()