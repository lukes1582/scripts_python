'''
Created on 13/02/2021
@author: lukes158@gmail.com l0m1s
'''

import random

class generatore_password:
    
    def __init__ (self):
        self.vMin = "abcdefghilmnopqrstuvzxywjk"
        self.vMai = "ABCDEFGHILMNOPQRSTUVZXYWJK"
        self.vNum = "1234567890"
        self.vAll = self.vMin+self.vMai+self.vNum

    def get_password(self,int_lenght):
        self.password = "".join(random.sample(self.vAll,int_lenght))
        return self.password
