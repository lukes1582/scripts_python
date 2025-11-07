# -*- coding: utf-8 -*-
#
# ============================================================
#  Nome Script : QR_inviti.py
#  Autore      : [Luca Vidoni]
#  Alias       : l0m1s
#  Versione    : 0.0.1.A
#  Email       : lukes1582@gmail.com    
#  Data        : 07/11/2025
#  Descrizione : Lo script permette di Contare quanti byte sono a 0x00 in un file video all'interno di una cartella
#  Licenza     : © [2025] [Luca Vidoni] - Tutti i diritti riservati
# ============================================================
#  © 2025 [Luca Vidoni lukes1582@gmail.com]
#  Tutti i diritti riservati. Uso riservato ai fini istituzionali.
#  È vietata la riproduzione, modifica o distribuzione non autorizzata.
# ============================================================

import os
import sys
import logging

def analizza_file_video(cartella_input, file_log, blocco=1024*1024):
    """
    Analizza tutti i file in una cartella e scrive un log con:
      - dimensione del file in MB/GB
      - quanti byte sono a 0x00
    """
    
    # Imposta il logging
    logging.basicConfig(
        filename=file_log,
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    logging.info(f"=== INIZIO ANALISI CARTELLA: {cartella_input} ===")

    # Controlla che la cartella esista
    if not os.path.isdir(cartella_input):
        print(f"Errore: la cartella '{cartella_input}' non esiste.")
        sys.exit(1)

    # Scansiona tutti i file nella cartella
    for root, _, files in os.walk(cartella_input):
        for nome_file in files:
            percorso = os.path.join(root, nome_file)
            try:
                dimensione = os.path.getsize(percorso)
                byte_zero = 0

                with open(percorso, 'rb') as f:
                    while blocco_bytes := f.read(blocco):
                        byte_zero += blocco_bytes.count(0)

                mb_zero = byte_zero / (1024*1024)
                mb_tot = dimensione / (1024*1024)
                gb_tot = dimensione / (1024*1024*1024)
                percentuale = (byte_zero / dimensione) * 100 if dimensione > 0 else 0

                messaggio = (
                    f"{nome_file} pesa {gb_tot:.2f} GB, contiene {mb_zero:.2f} MB "
                    f"di byte a 0x00 ({percentuale:.1f}%)"
                )

                print(messaggio)
                logging.info(messaggio)

            except Exception as e:
                logging.error(f"Errore analizzando {percorso}: {e}")

    logging.info("=== FINE ANALISI ===")


if __name__ == "__main__":
    # Esempio di uso:
    # python analizza_video.py /percorso/cartella /percorso/log.txt
    if len(sys.argv) != 3:
        print("Uso: python analizza_video.py <cartella_input> <file_log>")
        sys.exit(1)

    cartella = sys.argv[1]
    file_log = sys.argv[2]
    analizza_file_video(cartella, file_log)
