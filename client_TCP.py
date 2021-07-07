#!/usr/bin/env python3

"""
l0m1s
lukes1582@gmail.com
"""

import socket

target_host = "www.google.it"
target_port = 80

# creo oggetto socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send(b"GET / HTTP/1.1\r\nHost: google.it\r\n\r\n")

resp = client.recv(4096)

print(resp)