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
    Faccio la chiamata per la pagina web
"""
response = urllib.request.urlopen(url)
webContent = response.read()
"""
    Nel dubbio salvo la pagina web caso mai mi servisse offline senza CSS 
"""
f = open('page.html', 'wb')
f.write(webContent)
f.close
"""
    Richiamo l'URL per leggere la pagina
"""
soup = BeautifulSoup(urllib2.urlopen(url).read())
"""
    Stampo a terminale il testo della pagina web
"""
print(soup.get_text())

#---------------------------------------------------------------------------
# oppure
#---------------------------------------------------------------------------

f_page = open("page.html") # qui puoi mettere direttamente l'URL e saltare tutto prima
soup_page = f_page.read()
bs = BeautifulSoup(soup_page,"html.parser")
"""
    Salvo il testo della pagina web
"""
fWeb = open('page.txt', 'w')
fWeb.write(bs.get_text())
fWeb.close
