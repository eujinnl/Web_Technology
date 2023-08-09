#THIS IS THE SERVER
import socket
import sys
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    host = "127.0.0.1"
    port = 5001
    s.bind((host, port))
    print("Listening...")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            data = data.upper()
            if not data:
                break
            print(f"Received {len(data)} bytes")
            conn.sendall(data)