#7.    Write a server-side application where a socket waits for a client connection. The application should receive text from the connected client, replace lowercase letters with uppercase letters in the text, and then send it back to the client.

import socket

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

srv.bind(('0.0.0.0', 5000))

srv.listen(5)

while True:
    c, a = srv.accept()
    txt = c.recv(1024).decode()
    u = txt.upper()
    c.send(u.encode())
    
srv.close()


