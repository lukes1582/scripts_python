#!/usr/bin/env python3

"""
l0m1s
lukes1582@gmail.com
"""

import socket

HOST = '127.0.0.1'  # (localhost)
PORT = 65432        # Porte 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connesso ', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)