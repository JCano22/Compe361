# 4. Write an application that reads each byte from a text file (ASCII encoding). If a byte contains a semicolon symbol, it should be replaced (in the same file) with a comma symbol.

f = open("/Users/jorgecano/Desktop/test.txt", "r+b")

u = f.read(1)

while u != b'':
    if u == b';':
        f.seek(-1, 1)
        f.write(b',')
    u = f.read(1)

f.close()