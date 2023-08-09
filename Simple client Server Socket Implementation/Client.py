import socket
#THIS IS THE CLIENT
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    host = "127.0.0.1"
    port = 5001
    s.connect((host, port))
    s.send(b"hello world")
    data = s.recv(1024)