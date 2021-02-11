'''
Created on 11/02/2021
@author: lukes158@gmail.com l0m1s
'''

from PyPDF2 import PdfFileWriter, PdfFileReader

def proteggi_pdf(file,password):
    pdf_parser = PdfFileWriter()
    pdf_file = PdfFileReader(file)

    for pagine in range(pdf_file.numPages):
        pdf_parser.addPage(pdf_file.getPage(pagine))

    pdf_parser.encrypt(password)

    with open(f"file_protetto_{file}","wb") as f:
        pdf_parser.write(f)
        f.close()
    
    print(f"file_protetto_{file} e' stato creato correttamente")

if __name__ == "__main__":
    file = "prova.pdf"
    password = "lapasswordpiulungadelmondo"
    proteggi_pdf(file,password)