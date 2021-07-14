#!/usr/bin/env python3

"""
l0m1s
lukes1582@gmail.com
"""

import datetime

oggi = datetime.date.today().strftime('%Y-%m-%d')
oggi_lst = oggi.split("-")

compleanno_data = input("Inserisci la data di compleanno nel formato yyyy-mm-dd: ")

nome = input("Come ti chiami? ")

compleanno_data = compleanno_data.split("-")

eta =(int(oggi_lst[0])  - int(compleanno_data[0]))

print(f"{nome} adesso hai {eta} anni")
