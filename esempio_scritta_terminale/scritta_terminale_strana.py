'''
Created on 13/02/2021
@author: lukes158@gmail.com l0m1s
'''

import os
from pyfiglet import Figlet

terminal_text = Figlet(font="slant")
# se sei in windows è cls se si in Linux è clear
os.system("cls")
# definizione del terminale
os.system("mode con: cols=80 lines=40")
print(terminal_text.renderText("l0m1s"))