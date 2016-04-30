#coding: utf8
import json
import sqlite3

in_conn = sqlite3.connect( "../import/school_internet.sqlite" )
in_cur = in_conn.cursor()

conn = sqlite3.connect( "test_database.sqlite" )
cur = conn.cursor()
cur.execute( '''DROP TABLE IF EXISTS Try_database''' )
cur.execute( '''CREATE TABLE IF NOT EXISTS Try_database (name TEXT)''')

data = dict()                                                                   #part3 parsowanie
in_cur.execute('''SELECT rspo, imported FROM Schools''')                        #tworzy podreczna baze danych zeby parsowac
for school in in_cur:
    data[ school[0] ] = school[1]

in_cur.close()

for key in data:
    text = json.loads( data[key] )
    try: school_name = text['result']['records'][0][u'Nazwa szkoły/placówki']
    except: continue
    print school_name

    cur.execute('''INSERT INTO Try_database VALUES (?)''', (school_name,) )
    conn.commit()

cur.close()
