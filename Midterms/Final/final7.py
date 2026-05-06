#7.    Write a server-side application where a socket waits for a client connection. The application should receive text from the connected client, replace lowercase letters with uppercase letters in the text, and then send it back to the client.

import socket

srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(('0.0.0.0', 5000))

srv.listen(5)

while True:
    cnt, remote = srv.accept()

    txt = cnt.recv(1024).decode()
    resp = txt.upper()
    cnt.send(resp.encode())

    cnt.close()