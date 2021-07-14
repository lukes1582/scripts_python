#!/usr/bin/env python3

"""
l0m1s
lukes1582@gmail.com
"""

from win10toast import ToastNotifier

t = ToastNotifier()
t.show_toast("Notifica del piffero","Allerta del piffero", threaded=True,icon_path=None,duration=5) #5 secondi di visualizzazione dell'alert

import time

while t.notification_active():
    time.sleep(0.1)