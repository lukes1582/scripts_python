#!/usr/bin/env python3

"""
l0m1s
lukes1582@gmail.com
"""

import socket
import threading
import sys
import subprocess
import getopt

# variabili globali
target = ""
port = 0
upload_dest = ""
listen = False
upload = False
command = False
excute = ""

# definizione del programma
def usage():
    print()
    print("Netcat in Python -- Solo per LINUX")
    print()
    print("Utilizzo di netcat.py -t target-host -p port")
    print("-l --listen \t\t\t ascolta su [host]:[port] in attesa di connessioni")
    print("-e --execute=file_da_eseguire \t esegui il file appena ricevi una connessione")
    print("-c --command \t\t\t inizializza un comando per la shell")
    print("-u --upload=destinazione \t dopo aver ricevuto una connessione puoi fare\n\t\t\t\t il caricamento del file o scrivi direttamente su [destinazione]")
    print("***************************************************************")
    print("Esempi: ")
    print("netcat.py -t 192.168.10.1 -p 3333 -l -c")
    print("netcat.py -t 192.168.10.10 -p 3333 -l -u=/home/luca/target.sh")
    print("netcat.py -t 192.168.10.100 -p 3333 -l -e=cat /etc/password")
    print("echo '123456' | ./netcat.py -t 192.168.10.15 -p 333")
    print("***************************************************************")
    sys.exit(0)

#***************************************************************
def main():
    global upload_dest
    global listen
    

    if not len(sys.argv[1:]):
        usage()
    
    try:
        opts, args = getopt.getopt(sys.argv[1:],"hle:t:p:cu",["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as errore:
        print(errore)
    
    for op,ar in opts:
        if op in ("-h","--help"):
            usage()
        elif op in ("-l","--listen"):
            listen = True
        elif op in ("-e","--execute"):
            excute = ar
        elif op in ("-c","--command"):
            command = True
        elif op in ("-u","--upload"):
            upload_dest = ar
        elif op in ("-t","--target"):
            target = ar
        elif op in ("-p","--port"):
            port = int(ar)
            print(port)
        else:
            assert False,"Opzioni invalide"

        if ((not listen) and (len(target)) and (port>0)):
            buffer = sys.stdin.read()
            client_sender(buffer)

    if listen:
        server_loop()
main()

#***************************************************************
def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((target,port))
        
        if len(buffer):
            client.send(buffer)
        
        while(True):
            recv_len = 1
            response = ""

            while(recv_len):
                r_data = client.recv(4096)
                recv_len = len(r_data)
                response += r_data

                if(recv_len < 4096):
                    break
            print(response)

            buffer = raw_input("")
            buffer += "\n"

            client.send(buffer)
    except:
        print("Esiste una Eccezione... devi gestirla")
        client.close()
#***************************************************************
def server_loop():
    global target
    global port

    if not len(target):
        target = "0.0.0.0"
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target,port))

    server.listen(12)

    while(True):
        client_socket, addr = server.accept()

        client_thread = threading.Thread(target=client_handler,args=(client_socket,))
        client_thread.start()

#***************************************************************
def run_command(command):
    command = command.rstrip()
    try:
        c_output = subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)
    except:
        c_output = "Comando fallito\n"
    
    return c_output

#***************************************************************
def client_handler(client_socket):
    global upload
    global command
    global excute

    if (len(upload_dest)):

        file_buffer = ""

        while(True):
            c_data = client_socket.recv(1024)
            if not c_data:
                break
            else:
                file_buffer+= c_data

        try:
            file_desc = open(upload_dest,"wb")
            file_desc.write(file_buffer)
            file_desc.close()

            client_socket.send("Risultato salvato nel file")
        except:
            client_socket.send("Risultato NON salvato nel file. ERRORE!!!")
    if(len(excute)):
        c_output = run_command(excute)
        client_socket.send(c_output)

    if (command):
        while(True):
            client_socket.send("<NTC:#> ")
            cmd_buffer = ""
            while("\n" not in cmd_buffer):
                cmd_buffer += client_socket.recv(1024)
            
            response = run_command(cmd_buffer)
            client_socket.send(response)

#***************************************************************

