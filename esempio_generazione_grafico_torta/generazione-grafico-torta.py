'''
Created on 13/02/2021
@author: lukes158@gmail.com l0m1s
'''

from matplotlib import pyplot as plt

persone = 'Luca','Matteo','Marco','Giovanni','Ciccio'
valore = [27, 25, 10, 15, 23]
varie = (0.1, 0, 0, 0, 0)

fig, ax = plt.subplots()

ax.pie(valore, explode=varie, labels = persone, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')

plt.show()