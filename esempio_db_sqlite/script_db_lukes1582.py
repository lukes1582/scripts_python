'''
Created on 08/02/2021
@author: lukes158@gmail.com l0m1s
'''

import sqlite3
from sqlite3 import Error
import random as rm

from create_hash import create_hash

listNomeDonna = []
listNomeUomo = []
listCognomi = []

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ creare una tabella dall'istruzione create_table_sql
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def readFilesData():
    """ lettura dei dati dai file
    """
    txtUomo = open("z001.txt", 'r')
    lineUomo = txtUomo.readlines()
    for lUomo in lineUomo:
        lUomo = lUomo.replace('\n', '')
        listNomeUomo.append(lUomo)

    txtDonna = open("z002.txt", 'r')
    lineDonna = txtDonna.readlines()
    for lDonna in lineDonna:
        lDonna = lDonna.replace('\n', '')
        listNomeDonna.append(lDonna)

    txtCognomi = open("z003.txt", 'r')
    lineCognomi = txtCognomi.readlines()
    for lCognomi in lineCognomi:
        lCognomi = lCognomi.replace('\n', '')
        listCognomi.append(lCognomi)

def create_anagrafica(conn, anagrafica):
    """ crea una nuova anagrafica nella tabella anagrafica    
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO anagrafica(id_anagrafica,nome,cognome,data_nascita,key_anagrafica)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, anagrafica)
    conn.commit()
    return cur.lastrowid

def main():
    readFilesData()

    database = r"test_anagrafica.db"

    sql_create_anagrafica_table = """ CREATE TABLE IF NOT EXISTS anagrafica (
                                        id_anagrafica integer PRIMARY KEY,
                                        nome text NOT NULL,
                                        cognome text NOT NULL,
                                        data_nascita text,
                                        key_anagrafica text
                                    ); """

    # creo una connessione al db
    conn = create_connection(database)

     # creo la tabella anagrafica
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_anagrafica_table)
    else:
        print("Errore! Non posso creare la tabella.")

    with conn:
        # insrisco i dati casuali in anagrafica
        for i in range (1,41): # 40 righe di anagrafica randomica inserite nel db
            nomeU_Rand = listNomeUomo[rm.randint(0,len(listNomeUomo)-1)]
            nomeD_Rand = listNomeDonna[rm.randint(0,len(listNomeDonna)-1)]
            cognome_Rand = listCognomi[rm.randint(0,len(listCognomi)-1)]

            # id_anagrafica,nome,cognome,data_nascita,key_anagrafica

            if(i%2==0):
                h = create_hash(cognome_Rand+"-"+nomeU_Rand)
                dataU = str(rm.randint(1,31))+"-"+str(rm.randint(1,12))+"-"+str(rm.randint(1940,2012))
                anagrafica = (i,nomeU_Rand,cognome_Rand,dataU,str(h.createKeyMD5()));
                anagrafica_id = create_anagrafica(conn, anagrafica)
            else:
                h = create_hash(cognome_Rand+"-"+nomeD_Rand)
                dataD = str(rm.randint(1,31))+"-"+str(rm.randint(1,12))+"-"+str(rm.randint(1940,2012))
                anagrafica = (i,nomeD_Rand,cognome_Rand,dataD, str(h.createKeyMD5()));
                anagrafica_id = create_anagrafica(conn, anagrafica)
       

if __name__ == '__main__':
    main()