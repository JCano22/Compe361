import socket, threading



srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
srv.bind(('0.0.0.0', 8000))
srv.listen(50) # listens for incoming connections, 50 is the maximum number of queued connections

while True:
    client, remote = srv.accept()
    print("Connection from: " + str(remote))

    buf =client.recv(1000) # waits for a message from the client, returns the message in bytes
    txt = buf.decode() # decodes the message from bytes to string
    print(txt)
    
    resp = "<html><body><b>Hello</b><i> World</i></body></html>" # creates a response message
    bytes_resp = resp.encode() # converts the response message to bytes
    n = len(bytes_resp)

    client.send("HTTP/1.1 200 OK\r\n".encode()) # sends the status line to the client, message must be in bytes
    client.send("content-type: text/html; charset = utf-8\r\n".encode())
    client.send("content-length: ".encode() + str(n).encode() + "\r\n".encode())
    client.send("\r\n".encode())
    client.send(bytes_resp) # sends the response message to the client, message must be in bytes
    client.close()
