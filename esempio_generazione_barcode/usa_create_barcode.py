'''
Created on 12/02/2021
@author: lukes158@gmail.com l0m1s
'''

from create_barcode import create_barcode

if __name__ == '__main__':
    """
    La classe creata ha al suo interno
    : un metodo costruttore nel quale si passano due parametri
    : 1 parametro = il valore che deve essere convertito in barcode
    : 2 parametro = il percorso in cui dovrà essere salvato il barcode
    
    DEVI SAPERE che:
        EAN13 (esatti 12 caratteri)
        EAN14
        EAN8
        accettano solo valori numerici per poi essere convertiti in barcode
    MENTRE
        Code128
        accetta valori alfanumerici
    """
    b_code = create_barcode("1234657891011","")
    b_code.createBarcodeEAN13()
    b_code.createBarcodeEAN14()
    b_code.createBarcodeEAN8()

    b2_code = create_barcode("abcde12388","")
    b2_code.createBarcode128()