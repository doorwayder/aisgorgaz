import pymysql.cursors
from pypxlib import *
from termcolor import colored
import re
from converter_lib import *

HOSTNAME = 'localhost'
PORT = 3306
USER = 'root'
PASSWORD = 'root'
DB = 'arzgaz_imp'


def to_utf8(string: str):
    return string.encode('cp850').decode('cp1251')


def is_phone_incorrect(phone: str):
    if phone == '':
        return 0
    elif re.search('[а-я]', phone):
        return 1
    elif len(phone) < 10:
        return 2
    elif re.search(',', phone) or re.search(', ', phone) or re.search('; ', phone):
        if not parse_phones(phone):
            return 3
        else:
            return False
    elif len(phone) > 12:
        return 4
    else:
        return False


def get_correct_phone(phone):
    if not parse_phones(phone):
        if len(phone) == 10 and re.search('^9', phone):
            return phone
        elif len(phone) == 11 and re.search('^89', phone):
            return phone[1:]
        elif len(phone) == 12 and re.search('^\+79', phone):
            return phone[2:]
    else:
        for item in parse_phones(phone):
            if len(item) == 10 and re.search('^9', item):
                return item
            elif len(item) == 11 and re.search('^89', item):
                return item[1:]
            elif len(item) == 12 and re.search('^\+79', item):
                return item[2:]


def parse_phones(phone):
    phones1 = phone.split(', ')
    phones2 = phone.split(',')
    phones3 = phone.split('; ')
    if len(phones1) > 1:
        return phones1
    if len(phones2) > 1:
        return phones2
    if len(phones3) > 1:
        return phones3
    return False


def get_id_by_oldid(oldid):
    connection = pymysql.connect(host=HOSTNAME, port=PORT, user=USER, password=PASSWORD,
                                 db=DB, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = f'SELECT id FROM dogovor_dogovor WHERE id_old={oldid}'
            cursor.execute(sql)
    finally:
        connection.close()
        if cursor.rowcount > 0:
            return cursor.fetchone()['id']
        return False


"""CONVERT MAIN BAZA (34586)"""
def convert_baza(table):
    connection = pymysql.connect(host=HOSTNAME, port=PORT, user=USER, password=PASSWORD,
                                 db=DB, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    count = 0
    for row in table:
        if True:
            Tel3 = ''
            if row['Fam'] is not None:
                Fam = to_utf8(row['Fam'])
                # print(Fam)
            else:
                Fam = ''
            if row['Oborud'] is not None:
                Oborud = to_utf8(row['Oborud'])
            else:
                Oborud = ''
            if row['Datdog'] is not None:
                Datdog = row['Datdog']
            else:
                Datdog = ''
            Fl = int(row['Fl'])
            Rab = row['Rab']
            Vibr = row['Vibr']
            if row['Nom'] is not None:
                Nom = to_utf8(row['Nom'])
            else:
                Nom = ''
            if row['Tel'] is not None:
                Tel = to_utf8(row['Tel'])
            else:
                Tel = ''
            Idold = row['Id']
            Codg = row['Codg']
            Codu = row['Codu']
            if row['Dom'] is not None:
                Dom = to_utf8(row['Dom'])
            else:
                Dom = ''
            if row['Kv'] is not None:
                Kv = to_utf8(row['Kv'])
            else:
                Kv = ''
            Sum0 = row['Sum0']
            Skid = row['Skid']
            Sum1 = row['Sum1']
            Sumpr = row['Sumpr']
            if row['Datrab'] is not None:
                Datrab = row['Datrab']
            else:
                Datrab = None
            Period = row['Period']
            if row['Datsrok'] is not None:
                Datsrok = row['Datsrok']
            else:
                Datsrok = None
            if row['Coment'] is not None:
                Coment = to_utf8(row['Coment'])
            else:
                Coment = ''

            try:
                with connection.cursor() as cursor:
                    # print(Tel)
                    if not is_phone_incorrect(Tel):
                        Tel1 = get_correct_phone(Tel)
                        if Tel1:
                            count += 1
                            if parse_phones(Tel):
                                Tel3 = Tel
                            #print(count, Fam)
                        else:
                            Tel1= ''
                    else:
                        Tel3 = Tel
                        Tel1 = ''

                    sql = 'INSERT INTO dogovor_dogovor (name, number, date, end_date, tel1, tel3, fiz, address_city, ' \
                          'address_street, address_house, address_kv, equip, sum, discount, amount, comment, id_old, ' \
                          'active, created_by_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    cursor.execute(sql, (Fam, Nom, Datdog, Datsrok, Tel1, Tel3, Fl, getg(Codg), getu(Codg, Codu), Dom,
                                         Kv, Oborud, Sum0, Skid, Sum1, Coment, Idold, Rab, 3))
                    connection.commit()
            except Exception as e:
                print(e)


"""CONVERT MAIN BAZA (34586)"""
def convert_baza_sev(table):
    connection = pymysql.connect(host=HOSTNAME, port=PORT, user=USER, password=PASSWORD,
                                 db=DB, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    count = 0
    for row in table:
        if True:
            Tel3 = ''
            if row['Fam'] is not None:
                Fam = to_utf8(row['Fam'])
            else:
                Fam = ''
            if row['Oborud'] is not None:
                Oborud = to_utf8(row['Oborud'])
            else:
                Oborud = ''
            if row['Datdog'] is not None:
                Datdog = row['Datdog']
            else:
                Datdog = ''
            Fl = int(row['Fl'])
            Rab = row['Rab']
            Vibr = row['Vibr']
            if row['Nom'] is not None:
                Nom = to_utf8(row['Nom'])
            else:
                Nom = ''
            if row['Tel'] is not None:
                Tel = to_utf8(row['Tel'])
            else:
                Tel = ''
            Idold = row['Id'] + 100000
            Codg = row['Codg']
            Codu = row['Codu']
            if row['Dom'] is not None:
                Dom = to_utf8(row['Dom'])
            else:
                Dom = ''
            if row['Kv'] is not None:
                Kv = to_utf8(row['Kv'])
            else:
                Kv = ''
            Sum0 = row['Sum0']
            Skid = row['Skid']
            Sum1 = row['Sum1']
            Sumpr = row['Sumpr']
            if row['Datrab'] is not None:
                Datrab = row['Datrab']
            else:
                Datrab = None
            Period = row['Period']
            if row['Datsrok'] is not None:
                Datsrok = row['Datsrok']
            else:
                Datsrok = None
            if row['Coment'] is not None:
                Coment = to_utf8(row['Coment'])
            else:
                Coment = ''

            try:
                with connection.cursor() as cursor:
                    # print(Tel)
                    if not is_phone_incorrect(Tel):
                        Tel1 = get_correct_phone(Tel)
                        if Tel1:
                            count += 1
                            if parse_phones(Tel):
                                Tel3 = Tel
                            #print(count, Fam)
                        else:
                            Tel1= ''
                    else:
                        Tel3 = Tel
                        Tel1 = ''

                    sql = 'INSERT INTO dogovor_dogovor (name, number, date, end_date, tel1, tel3, fiz, address_city, ' \
                          'address_street, address_house, address_kv, equip, sum, discount, amount, comment, id_old, ' \
                          'active, created_by_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
                    cursor.execute(sql, (Fam, Nom, Datdog, Datsrok, Tel1, Tel3, Fl, getg(Codg), getu(Codg, Codu), Dom,
                                         Kv, Oborud, Sum0, Skid, Sum1, Coment, Idold, Rab, 4))
                    connection.commit()
            except Exception as e:
                print(e)


def convert_payments(table):
    connection = pymysql.connect(host=HOSTNAME, port=PORT, user=USER, password=PASSWORD,
                                 db=DB, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    count = 0
    errors = 0
    for row in table:
        Idold = row['Id']
        if row['Fio'] is not None:
            Fio = to_utf8(row['Fio'])
            #print(Fio)
        else:
            Fio = ''
        if row['Datrab'] is not None:
            Datrab = row['Datrab']
        else:
            datrab = ''
        if row['Sumo'] is not None:
            Sumo = row['Sumo']
        else:
            Sumo = 0

        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO dogovor_payment (pay_type, date, amount, pay_place, dogovor_id_id, comment, created_by_id) ' \
                      'VALUES (%s, %s, %s, %s, %s, %s, %s)'
                did = get_id_by_oldid(Idold)
                if did:
                    count += 1
                    cursor.execute(sql, (1, Datrab, Sumo, '', did, Fio, 3))
                    connection.commit()
                else:
                    errors += 1
                    print('error: id=', did)

                #print(count, '===', Idold, Fio, Datrab, Sumo)
        except Exception as e:
            print(e)
        print('errors: ', errors)


def convert_payments_sev(table):
    connection = pymysql.connect(host=HOSTNAME, port=PORT, user=USER, password=PASSWORD,
                                 db=DB, charset='utf8', cursorclass=pymysql.cursors.DictCursor)
    count = 0
    errors = 0
    for row in table:
        Idold = row['Id'] + 100000  # 100000 - для Севастопольской
        if row['Fio'] is not None:
            Fio = to_utf8(row['Fio'])
            #print(Fio)
        else:
            Fio = ''
        if row['Datrab'] is not None:
            Datrab = row['Datrab']
        else:
            datrab = ''
        if row['Sumo'] is not None:
            Sumo = row['Sumo']
        else:
            Sumo = 0

        try:
            with connection.cursor() as cursor:
                sql = 'INSERT INTO dogovor_payment (pay_type, date, amount, pay_place, dogovor_id_id, comment, created_by_id) ' \
                      'VALUES (%s, %s, %s, %s, %s, %s, %s)'
                did = get_id_by_oldid(Idold)
                if did:
                    count += 1
                    cursor.execute(sql, (1, Datrab, Sumo, '', did, Fio, 4))
                    connection.commit()
                else:
                    errors += 1
                    print('error: id=', did)

                #print(count, '===', Idold, Fio, Datrab, Sumo)
        except Exception as e:
            print(e)
        print('errors: ', errors)


filename_baza = os.path.join('db', 'baza.db')
filename_baza_sev = os.path.join('db\\sev', 'baza.DB')
filename_pay = os.path.join('db', 'period.DB')
filename_pay_sev = os.path.join('db\\sev', 'period.DB')

print(colored('[Converting started]', 'green'))


convert_baza(Table(filename_baza))
convert_baza_sev(Table(filename_baza_sev))
convert_payments(Table(filename_pay))
convert_payments_sev(Table(filename_pay_sev))

