import pymysql.cursors

DATABASE = 'gorgaz_sev'

def converter():
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db=DATABASE,
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            sql = f'SELECT * FROM baza LIMIT 30000'
            cursor.execute(sql)
    finally:
        connection.close()
        result = cursor.fetchall()

    if result is not None:
        return result
    else:
        return False


def getu(codg, codu):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db=DATABASE,
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = f'SELECT * FROM ulica WHERE Codg={codg} AND Codu={codu}'
            cursor.execute(sql)
    finally:
        connection.close()
        if cursor.rowcount > 0:
            return cursor.fetchone()['Ulica']
        return ''



def getg(codg):
    connection = pymysql.connect(host='localhost', port=3306, user='root', password='root', db=DATABASE,
                                 charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = f'SELECT * FROM gorod WHERE Codg={codg} '
            cursor.execute(sql)
    finally:
        connection.close()
        if cursor.rowcount > 0:
            return cursor.fetchone()['Gor']
        else:
            return ''
