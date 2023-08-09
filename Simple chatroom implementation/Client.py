import socket
import threading
#THIS IS THE CLIENT
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 5001
s.connect((host, port))

def write():
    while True:
        msg = bytes(input (" => "), encoding='UTF-8')
        s.send(msg)

def receive():
    while True:
        try:
            message = s.recv(1024)
            print(message)
        except:
            print("An error occured!")
            s.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()