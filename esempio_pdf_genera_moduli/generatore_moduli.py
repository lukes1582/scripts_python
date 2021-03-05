'''
Created on 04/03/2021
@author: lukes158@gmail.com l0m1s
'''
import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk
from tkinter import messagebox
from os import path
import time

from report_pdf import report_pdf


#definizione dei campi da inserire nel QR
fields = "Anno impianto pratica","Protocollo ABRACADABRA in a.c.","Data Impianto","Dipartimento Richiedente","Rif. Let. Nr ","Data Richiesta","Descrizione Dispositivo","Esito controllo"

# pulisci campi
def clearForm(entries):
    for entry in entries:
        field = entry[0]
        text  = entry[1].delete(0, 'end')

# metordo per il controllo dell'anno inserito
def checker (val_x,zStr):
    val_y = str(val_x)
    if(len(val_x)== 0):
        messagebox.showerror ("Generatore Modulo Recupero Dati", "Errore: Non hai inserito valore nel campo "+zStr+". Errore E000")
    else:
         return val_y
    
# metodo per la determinazione del codice QR
def fetch(entries):
    #----------------------------------------------
    strTime = time.strftime("%Y-%m-%d_%H.%M.%S")
    #---------------------------------------------

    strParametri = ""
    indexF = 0
    for entry in entries:
        field = entry[0]
        text  = entry[1].get()
        if(field == fields[indexF]):
            strParametri +=checker(text,fields[indexF])+","
            indexF +=1

    rapp = report_pdf(strParametri,strTime)
    rapp.generateReport()
    messagebox.showinfo("Generatore Modulo Dati", "Modulo creato correttamente")

def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=30, text=field, anchor='w', font=helv20)
        ent = tk.Entry(row, width=50,font=helv20)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Generatore Moduli Dati Vers. 0.1 ")
    # definizione del font per la GUI
    helv20 = tkFont.Font(family='Helvetica', size=20)
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = tk.Button(root, text='Genera Modulo',
                  command=(lambda e=ents: fetch(e)), font=helv20)
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    
    b2 = tk.Button(root, text='Chiudi', command=root.quit, font=helv20)
    b2.pack(side=tk.RIGHT, padx=5, pady=5)

    b3 = tk.Button(root, text='Pulisci campi',
                  command=(lambda e=ents: clearForm(e)), font=helv20)
    b3.pack(side=tk.RIGHT, padx=5, pady=5)
   
    
  
    
    root.mainloop()
