'''
Created on 12/02/2021
@author: lukes158@gmail.com l0m1s
'''

from create_hash import create_hash

if __name__ == '__main__':
    """
    La classe creata ha al suo interno
    : un metodo costruttore nel quale si passano due parametri
    : 1 parametro = il valore che deve essere convertito in hash
    """
    vHash = create_hash("123456789lkjpoiuasdvbnc")

    print("MD5 "+vHash.createKeyMD5())
    print("SHA1 "+vHash.createKeySHA1())
    print("SHA224 "+vHash.createKeySHA224())
    print("SHA256 "+vHash.createKeySHA256())
    print("SHA384 "+vHash.createKeySHA384())
    print("SHA512 "+vHash.createKeySHA512())
    

