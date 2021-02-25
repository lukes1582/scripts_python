'''
Created on 24/02/2021
@author: lukes158@gmail.com l0m1s
'''

from bs4 import BeautifulSoup
import urllib.request as urllib2
import urllib.request, urllib.error, urllib.parse

"""
    Definisco l' URL 
"""
url = 'https://www.ansa.it/sito/notizie/cronaca/2021/02/24/uber-procuratore-di-milano-aperta-unindagine-fiscale_fd98d931-55c4-4410-9ac2-35abaf5f503e.html'

"""
    Richiamo l'URL per leggere la pagina
"""
soup_page = BeautifulSoup(urllib2.urlopen(url).read(),"html.parser")
"""
    Salvo il testo della pagina web
"""
fWeb = open('pagina.txt', 'w')
fWeb.write(soup_page.get_text())
fWeb.close
