#22.08.2019

import socket
import time
print("Server is running...")

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 8082       # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode("utf-8")
            print(data)
