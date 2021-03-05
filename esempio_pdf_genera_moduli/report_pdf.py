'''
Created on 04/03/2021
@author: lukes158@gmail.com l0m1s
'''

from fpdf import FPDF

class report_pdf:

    def __init__(self,strValues,strTime):
        self.strValues = strValues
        self.strTime = str(strTime)
          
    
    def generateReport(self):

        listParametri = self.strValues.split(",")
        """
        listParametri contiene i dati da inserire nel PDF sono cosi' formati
            : 0 anno pratica
            : 1 protocollo ABRACADABRA
            : 2 data impianto
            : 3 dipartimento richiedente
            : 4 riferimento lettera nr 
            : 5 data richiesta
            : 6 dispositivo
            : 7 esito controllo
        """
        pdf = FPDF()
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.set_left_margin(15)
        pdf.set_right_margin(15)
        pdf.set_top_margin(15)
        """
        Prima pagina di intestazione
        """
        pdf.add_page()
        # titolo del pdf
        pdf.set_title("Modulo_Dati")
        # font 
        pdf.set_font("Arial",'B', size=40)
        # spessore linea tabella
        pdf.set_line_width(0.8)       
        # prima dicitura
        pdf.cell(pdf.font_size_pt,pdf.font_size_pt,txt=listParametri[1], border=1,align='C')
        col_width = pdf.w * 0.7
        pdf.set_font("Arial",'B', size=20)
        pdf.cell(col_width, pdf.font_size_pt,txt="SUPPORTO TECNICO AI DIPARTIMENTI", border="LTR",align='C')
        pdf.ln(pdf.font_size_pt)

        pdf.set_font("Arial", size=40)
        pdf.cell(pdf.font_size_pt)

        pdf.set_font("Arial",'B', size=20)
        pdf.cell(col_width, pdf.font_size_pt,txt= "Anno "+listParametri[0], border="LRB",align='C')
        pdf.ln(35)
        #----------------------------------------------------------------------------------------------------------------------------------
        pdf.set_font("Arial", size=40)
        wVal = pdf.font_size_pt
        pdf.image('logo.png',16,75,38)

        pdf.cell(40,48,txt='',border=1)

        pdf.set_font("Arial", size=12)
        col_width = pdf.w * 0.7    
        pdf.cell(col_width, pdf.font_size_pt,txt= "RICHIEDENTE: "+listParametri[3], border="LTR")
        pdf.ln(pdf.font_size_pt)
        pdf.cell(wVal)
        pdf.cell(col_width, pdf.font_size_pt,txt= "RIFERIMENTO LET. NR.: "+listParametri[4], border="LR")
        pdf.ln(pdf.font_size_pt)
        pdf.cell(wVal)
        pdf.cell(col_width, pdf.font_size_pt,txt= "DATA RICHIESTA: "+listParametri[5], border="LR")
        pdf.ln(pdf.font_size_pt)
        pdf.cell(wVal)
        pdf.cell(col_width, pdf.font_size_pt,txt= "DISPOSITIVO: "+listParametri[6], border="LRB")
        pdf.ln(25)


        #-----------------------------------------------------------------------------------------------------------------------
        pdf.set_font("Arial", size=12)
        col_width = pdf.w * 0.89
        pdf.cell(col_width, pdf.font_size_pt,txt= "DATA IMPIANTO PRATICA: "+listParametri[2], border="LTR")
        pdf.ln(pdf.font_size_pt)
        pdf.cell(col_width, pdf.font_size_pt,txt= "LABORATORI INTERESSATO: ELETTRONICA", border="LR")
        pdf.ln(pdf.font_size_pt)
        pdf.cell(col_width, pdf.font_size_pt,txt= "DATA ASSEGNAZIONE: __________________________________________", border="LR")
        pdf.ln(pdf.font_size_pt)
        pdf.cell(col_width, pdf.font_size_pt,txt= "TECNICO ASSEGNATARIO: ________________________________________", border="LR")
        pdf.ln(pdf.font_size_pt)
        pdf.cell(col_width, pdf.font_size_pt,txt= "DATA EVASIONE PRATICA: ________________________________________", border="LRB")
        
        """
        Seconda pagina 
        """
        pdf.add_page()
        pdf.image('logo.png',19,16,33)
        pdf.set_font("Arial",'B', size=14)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="SUPPORTO TECNICO AI DIPARTIMENTI ",border="LTR",align='C')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="ANNO "+listParametri[0],border="LR",align='C')
        pdf.ln(pdf.font_size_pt/2)
        pdf.set_font("Arial", size=14)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="PROT.LLO ABRACADABRA: "+listParametri[1]+"   ",border="LR",align='R')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="DATA IMPIANTO: "+listParametri[2]+"   ",border="LRB",align='R')
        pdf.ln(pdf.font_size_pt)
        
        pdf.set_font("Arial", size=12)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="- DIPARTIMENTO RICHIEDENTE:\t"+listParametri[3],border="LTR",align='L')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="- RIFERIMENTO LET. NR. :\t"+listParametri[4],border="LR",align='L')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="- DATA RICHIESTA:\t"+listParametri[5],border="LR",align='L')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="- DISPOSITIVO:\t"+listParametri[6],border="LR",align='L')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="- ESITO CONTROLLO RICEVIMENTO:\t"+listParametri[7],border="LR",align='L')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="- COLLOCAZIONE DISPOSITIVO: Laboratorio Elettronica",border="LR",align='L')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="firma per ricevuta ________________________ ",border="LRB",align='R')
        pdf.ln(pdf.font_size_pt)

        pdf.set_font("Arial",'B', size=14)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="LABORATORIO INTERESSATO",border="LTR",align='C')
        pdf.ln(pdf.font_size_pt/2)
        pdf.set_font("Arial", size=14)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="SEZIONE ELETTRONICA",border="LRB",align='C')
        pdf.ln(pdf.font_size_pt)

        pdf.set_font("Arial",'B', size=14)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="DISPOSIZIONI DIRIGENTE DEL DIPARTIMENTO",border="LTR",align='C')
        pdf.ln(pdf.font_size_pt/2)
        pdf.set_font("Arial", size=12)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="___________________________________________________________________________",border="LR",align='C')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="___________________________________________________________________________",border="LR",align='C')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="___________________________________________________________________________",border="LR",align='C')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="[]Ordinaria          []Urgente          []Prioritaria                              _______________________ ",border="LR",align='R')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="(Firma del Dirigente)  ",border="LRB",align='R')
        pdf.ln(pdf.font_size_pt)

        pdf.set_font("Arial",'B', size=14)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="DISPOSIZIONI DIRIGENTE DI SEZIONE",border="LTR",align='C')
        pdf.ln(pdf.font_size_pt/2)
        pdf.set_font("Arial", size=12)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="PRATICA ASSEGNATA A _____________________ IN DATA _________________________",border="LR",align='L')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="NOTE TECNICHE:_____________________________________________________________",border="LR",align='L')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="____________________________________________________________________________",border="LR",align='L')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="____________________________________________________________________________",border="LR",align='L')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="____________________________________________________________________________",border="LR",align='L')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="Roma, _______________",border="LR",align='L')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="_____________________________________",border="LR",align='R')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="(Firma del Dirigente della Sezione) ",border="LRB",align='R')
        pdf.ln(pdf.font_size_pt)                                                                

        pdf.set_font("Arial",'B', size=14)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="CONCLUSIONI",border="LTR",align='C')
        pdf.ln(pdf.font_size_pt/2)
        pdf.set_font("Arial", size=12)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="- ESITO DELLE ATTIVITA  DI SUPPORTO TECNICO: ______________",border="LR",align='L')
        pdf.ln(pdf.font_size_pt/2)
        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="- DISPOSITIVO: ",border="LR",align='L')
        pdf.ln(pdf.font_size_pt/2)

        valW = pdf.font_size_pt
        pdf.cell(pdf.font_size_pt,pdf.font_size_pt,txt="[]",border="L",align='R')
        pdf.cell(valW)
        pdf.cell((pdf.w-valW-0.5)*0.7899,pdf.font_size_pt,txt="RESTITUITO AL DIPARTIMENTO RICHIEDENTE DATA RESTITUZIONE _______  ",border="R",align='L')
        pdf.ln(pdf.font_size_pt/2)

        pdf.cell(pdf.font_size_pt,pdf.font_size_pt,txt="[]",border="L",align='R')
        pdf.cell(valW)
        pdf.cell((pdf.w-valW-0.5)*0.7899,pdf.font_size_pt,txt="TRATTENUTO DAL LABORATORIO COLLOCAZIONE ____________________________  ",border="R",align='L')
        pdf.ln(pdf.font_size_pt/2)

        pdf.cell(pdf.w*0.857,pdf.font_size_pt,txt="- DATA ARCHIVIAZIONE PRATICA: _____________________________",border="LRB",align='L')
        pdf.ln(pdf.font_size_pt) 

        """
        Terza pagina 
            : ok perfetta cosi com e
        """
        pdf.set_font("Arial",'B', size=16)
        pdf.add_page()
        col_width = pdf.w * 0.666
        pdf.cell(40,40,txt='',border=1)
        pdf.image('logo.png',19,19,33)
        pdf.cell(col_width,40,txt="  ANNOTAZIONI, APPUNTI, PROMEMORIA, VARIE..", border=1)
    

        pdf.output("Modulo_Recupero_Dati_"+self.strTime+".pdf")
