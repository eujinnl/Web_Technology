#THIS IS THE SERVER
import socket
import sys
import threading


def handle_clients(conn, cid):
    while True:
        conn.send(b"Welcome to this chatroom!")
        list_of_clients[cid] = conn
        while True:
            message_2 = conn.recv(1024)
            message = message_2.decode('UTF-8')
            cid_str = cid.decode('UTF-8')
            if message:
                message_to_send = bytes("<" + cid_str + "> " + message ,encoding ='UTF-8')
                broadcast(message_to_send, conn)


def broadcast(msg,cid):
    for clients in list_of_clients:
        if clients != cid:
            list_of_clients[clients].send(msg)


def accept_client_connection():
    while True:
        conn, addr = s.accept()
        with conn:
            conn.send(b"Enter CID")
            cid = conn.recv(1024)
            if cid != None:
                #handle_clients(conn, cid)
                new_thread = threading.Thread(target=handle_clients, args=(conn,cid))
                new_thread.start()
                new_thread.join()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"
port = 5001
s.bind((host, port))
print("Listening...")
list_of_clients={}
while True:
    s.listen(100)
    new_thread = threading.Thread(target=accept_client_connection())
    new_thread.start()
    new_thread.join()
