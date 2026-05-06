#client to final7.py

import socket
cnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cnt.connect( ('', 5000))

txt = "I know what you did last summer"

cnt.send(txt.encode())
resp = cnt.recv(1024).decode()

print(resp)

cnt.close()