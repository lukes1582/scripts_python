import csv
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="laPassword",
    database="all_db"
)

with open("mappa-dei-monumenti-in-Italia.csv", newline="", encoding="ISO-8859-1") as filecsv:
    lett = csv.reader(filecsv, delimiter=";")
    all_values = []
    for rows in lett:
        values = (rows[0], rows[1], rows[2], rows[3], rows[4], rows[5], rows[6], rows[7], rows[8], rows[9] )
        all_values.append(values)

query = "insert into tab_monumenti(Comune,Provincia,Regione,Nome,Tipo,Anno inserimento,Data e ora inserimento,Identificatore in OpenStreetMap,Longitudine,Latitudine) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

mycursor = mydb.cursor()

mycursor.executemany(query, values)

mydb.commit()
