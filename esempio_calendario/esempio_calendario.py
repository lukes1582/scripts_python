'''
Created on 05/03/2021
@author: lukes158@gmail.com l0m1s
'''

from tkinter import *
import calendar

root = Tk()

root.title("Il mio calendario")
anno = 2021

mioCalendario = calendar.calendar(anno)

calendarioAnno= Label(root,text=mioCalendario,font="Calibri 16 bold")
calendarioAnno.pack()

root.mainloop()