'''
Created on 12/02/2021
@author: lukes158@gmail.com l0m1s
'''

import threading

def temporizzatore_print():
  threading.Timer(3.0, temporizzatore_print).start() # 3 in secondi
  print("Hello, World!")

if __name__ == "__main__":
  temporizzatore_print() 
  """
  Una volta lanciato il metodo, esso ogni 3 secondi stampa sul terminale 'Hello, World!'
  """
