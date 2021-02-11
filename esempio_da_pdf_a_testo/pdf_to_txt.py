'''
Created on 11/02/2021
@author: lukes158@gmail.com l0m1s
'''

import pdfplumber
from PyPDF2 import PdfFileReader

def converti_pdf(file):
    pdf_file = PdfFileReader(file)

    for nr_pagine in range(pdf_file.numPages):
        with pdfplumber.open(file) as pdf:
            print(pdf.pages[nr_pagine].extract_text())

            with open(f"file_testuale_{file}.txt","ab") as f:
                strX = pdf.pages[nr_pagine].extract_text().encode("utf-8")
                f.write(strX)
                f.close()
            
    print(f"file_protetto_{file} e' stato creato correttamente")

if __name__ == "__main__":
    file = "prova.pdf"
    converti_pdf(file)






