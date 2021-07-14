#!/usr/bin/env python3

"""
l0m1s
lukes1582@gmail.com
"""

from GoogleNews import GoogleNews

gn = GoogleNews()
gn.set_lang('it')
gn.set_period('7d')
gn.setencode('utf-8')
gn.search('ITALIA')

risultati = gn.result()

for varX in risultati:
    print("*"*50)
    print("Titolo --", varX['title'])
    print("Data --", varX['date'])
    print("Descrizione --", varX['desc'])
    print("Link --", varX['link'])
