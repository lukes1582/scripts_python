'''
Created on 11/02/2021
@author: lukes158@gmail.com l0m1s
'''

from prettytable import PrettyTable
import random as rm

Tabella = PrettyTable(["Nome","Val_1","Val_2","Val_3"])

xNome = ["Luca","Giovanni","Marco","Matteo","Pietro","Giuseppe","Simone","Ciccio"]

for i in range(1,15):
    xRiga = []
    xRiga.append(xNome[rm.randint(0,len(xNome)-1)])
    xRiga.append(rm.randint(0,9))
    xRiga.append(rm.randint(10,99))
    xRiga.append(rm.randint(100,200))
    Tabella.add_row(xRiga)

print(Tabella)
    