'''
Created on 12/02/2021
@author: lukes158@gmail.com l0m1s
'''

from barcode import *
from barcode.writer import ImageWriter

class create_barcode:
    def __init__(self,val,dirSelect):
        self.val = val
        self.dirSelect = dirSelect

    def createBarcodeEAN13(self):
        my_code = EAN13(self.val, writer=ImageWriter()) # solo numeri
        my_code.save(self.dirSelect+"barcode_EAN13_"+self.val, {"module_width":0.35, "module_height":6, "font_size": 8, "text_distance": 1, "quiet_zone": 3}) # in png _ean13

    def createBarcodeEAN14(self):
        my_code = EAN14(self.val, writer=ImageWriter()) # solo numeri 
        my_code.save(self.dirSelect+"barcode_EAN14_"+self.val, {"module_width":0.35, "module_height":6, "font_size": 8, "text_distance": 1, "quiet_zone": 3})# in png _ean14

    def createBarcodeEAN8(self):
        my_code = EAN8(self.val, writer=ImageWriter()) # solo numeri 
        my_code.save(self.dirSelect+"barcode_EAN8_"+self.val, {"module_width":0.35, "module_height":6, "font_size": 8, "text_distance": 1, "quiet_zone": 3}) #in png _ean8

    def createBarcode128(self):
        my_code = Code128(self.val, writer=ImageWriter()) #alfanumerico
        my_code.save(self.dirSelect+"barcode_Code128_"+self.val, {"module_width":0.05, "module_height":2, "font_size": 8, "text_distance": 1, "quiet_zone": 3}) #in png _128
