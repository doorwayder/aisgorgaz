from pypxlib import *
import pymysql.cursors
import os

HOSTNAME = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = 'root'
DB1 = 'gorgaz'
DB2 = 'gorgaz_sev'

def to_utf8(string: str):
    return string.encode('cp850').decode('cp1251')


connection = pymysql.connect(host=HOSTNAME, port=PORT, user=USER, password=PASSWORD,
                             db=DB1, charset='utf8', cursorclass=pymysql.cursors.DictCursor)

"""CONVERT ULICA"""
table1 = Table('db\\ulica.DB')
print(len(table1))

for row in table1:
    if row['Ulica'] is not None:
        #print(to_utf8(row['Ulica']))
        #print(row['Codg'])

        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO ulica(Codg, Ulica, Codu) VALUES (%s, %s, %s)'
                cursor.execute(sql, (row['Codg'], to_utf8(row['Ulica']), row['Codu']))
                connection.commit()
        except Exception as e:
            print(e)
table1.close()


table2 = Table('db\\gorod.DB')
print(len(table2))

for row in table2:
    if row['Gor'] is not None:
        #print(to_utf8(row['Gor']))
        #print(row['Codg'])

        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO Gorod(Gor, Codg) VALUES (%s, %s)'
                cursor.execute(sql, (to_utf8(row['Gor']), row['Codg']))
                connection.commit()
        except Exception as e:
            print(e)
connection.close()
table2.close()


connection = pymysql.connect(host=HOSTNAME, port=PORT, user=USER, password=PASSWORD,
                             db=DB2, charset='utf8', cursorclass=pymysql.cursors.DictCursor)

"""CONVERT ULICA"""
table3 = Table('db\\sev\\ulica.DB')
print(len(table3))

for row in table3:
    if row['Ulica'] is not None:
        #print(to_utf8(row['Ulica']))
        #print(row['Codg'])

        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO ulica(Codg, Ulica, Codu) VALUES (%s, %s, %s)'
                cursor.execute(sql, (row['Codg'], to_utf8(row['Ulica']), row['Codu']))
                connection.commit()
        except Exception as e:
            print(e)
table3.close()


table4 = Table('db\\sev\\gorod.DB')
print(len(table4))

for row in table4:
    if row['Gor'] is not None:
        #print(to_utf8(row['Gor']))
        #print(row['Codg'])

        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO Gorod(Gor, Codg) VALUES (%s, %s)'
                cursor.execute(sql, (to_utf8(row['Gor']), row['Codg']))
                connection.commit()
        except Exception as e:
            print(e)
connection.close()
table4.close()

