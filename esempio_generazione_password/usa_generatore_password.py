'''
Created on 13/02/2021
@author: lukes158@gmail.com l0m1s
'''

from generatore_password import generatore_password

if __name__ == '__main__':
    """
    La classe creata ha al suo interno
    : un metodo costruttore nel quale si passano due parametri
    : 1 parametro = il valore che deve essere convertito in hash
    """
    vPass = generatore_password()

    print("Password a 8 caratteri "+ vPass.get_password(8))
    print("Password a 10 caratteri "+ vPass.get_password(10))
    print("Password a 16 caratteri "+ vPass.get_password(16))
    
    
