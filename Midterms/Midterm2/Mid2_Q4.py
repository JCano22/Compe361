# 4. Write an application that reads each byte from a text file (ASCII encoding). If a byte contains a semicolon symbol, it should be replaced (in the same file) with a comma symbol.

f = open("/Users/jorgecano/Desktop/test.txt", "r+b")

byte = f.read(1)

while byte != b'':
    if byte == b';':
        f.seek(-1, 1)
        f.write(b',')
    byte = f.read(1)

f.close()


