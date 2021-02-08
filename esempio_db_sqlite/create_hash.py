'''
Created on 08/02/2021
@author: lukes158@gmail.com l0m1s
'''

import hashlib


class create_hash:

    def __init__(self,strN):
        self.strN = strN
        
    def createKeyMD5(self):
        strX = str(self.strN).encode('utf-8')
        hs = hashlib.md5()
        hs.update(strX)
        return hs.hexdigest()

    def createKey1(self):
        strX = str(self.strN).encode('utf-8')
        hs = hashlib.sha1()
        hs.update(strX)
        return hs.hexdigest()

    def createKey224(self):
        strX = str(self.strN).encode('utf-8')
        hs = hashlib.sha224()
        hs.update(strX)
        return hs.hexdigest()

    def createKey256(self):
        strX = str(self.strN).encode('utf-8')
        hs = hashlib.sha256()
        hs.update(strX)
        return hs.hexdigest()

    def createKey384(self):
        strX = str(self.strN).encode('utf-8')
        hs = hashlib.sha3_384()
        hs.update(strX)
        return hs.hexdigest()

    def createKey512(self):
        strX = str(self.strN).encode('utf-8')
        hs = hashlib.sha512()
        hs.update(strX)
        return hs.hexdigest()
