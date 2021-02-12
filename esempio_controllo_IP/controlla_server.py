'''
Created on 12/02/2021
@author: lukes158@gmail.com l0m1s
'''

import os
import re
import threading
from datetime import datetime


# dichirazione variabili personalizzabili
# indirizzo email a cui inviare i dati
mail = "lukes1582@gmail.com"
# timer PING in minuti
timePING = 5
# timer per l'invio MAIL in minuti
timeMAIL = 60
# file che contiene gli IP da controllare
wFile = "white_list.txt"
# file che verra' allegato alla mail
bFile = "black_list.txt"

# lista di supporto al programma
IP_address=[]

# metodo per il controllo degli IP
def checkIP(val):
    # espressione regolare per gli IPv4
    pat = re.compile("^([1][0-9][0-9].|^[2][5][0-5].|^[2][0-4][0-9].|^[1][0-9][0-9].|^[0-9][0-9].|^[0-9].)([1][0-9][0-9].|[2][5][0-5].|[2][0-4][0-9].|[1][0-9][0-9].|[0-9][0-9].|[0-9].)([1][0-9][0-9].|[2][5][0-5].|[2][0-4][0-9].|[1][0-9][0-9].|[0-9][0-9].|[0-9].)([1][0-9][0-9]|[2][5][0-5]|[2][0-4][0-9]|[1][0-9][0-9]|[0-9][0-9]|[0-9])$")
    # test di correttezza
    test = pat.match(val)
    if test:
        return val
    else:
        # se esiste un IP non valido viene scritto nella BLACK LIST
        writeBlackList("Errore nell IP  "+val)
        return None

# metodo per la lettura degli IP
def readWhiteList():
    fs = open(wFile,'r') 
    lines = fs.readlines() 
    for line in lines: 
        # inserisce gli IP in una lista di supporto
        IP_address.append(checkIP(line))
    fs.close()  

# metodo per la scrittura del file in allegato
def writeBlackList(val):
    ws = open(bFile,'a')
    ws.write(val)

#metodo per la 
def pingHost(hostname):
    date_time = datetime.now()
    t1 = date_time.strftime("%d-%b-%Y (%H:%M:%S)")
    # Se sei in ambiente "Linux -c"
    response = os.system("ping -n 3 " + hostname)
    if response == 0:
        return str(hostname + " Server on line !\n")
    else:
        writeBlackList(str("\n" + hostname + " Server off line ! \t "+t1+" \n"))
        return str(hostname + " Server off line !")


def callHostPING():
    threading.Timer((60.0*timePING), callHostPING).start()
    readWhiteList()
    for k in IP_address:
        print(pingHost(k))
    IP_address.clear()

def sendMAIL():
    threading.Timer((60.0*timeMAIL), sendMAIL).start()
    b = os.path.getsize("black_list.txt")
    """
    Viene dato per scontato che DEVE essere installato il programma   mail  all'interno della macchina in cui gira lo script
    """
    if(b > 0):
        # crea una mail e allega il file con i server offline
        bash_mail = " echo 'Server Offline' | mail -s subject "+mail+" -a black_list.txt"
        # spedisce la mail 
        os.system(bash_mail) 
        # cancella il file con la lista dei server offline
        os.remove(bFile)

if __name__ == '__main__':
  callHostPING()
  sendMAIL()  






