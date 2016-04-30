#coding: utf8
import sqlite3
import json

conn = sqlite3.connect( '../import/school_internet.sqlite' )
cur = conn.cursor()

data = dict()
cur.execute('''SELECT rspo, imported FROM Schools''')
for school in cur:
    data[school[0]] = school[1]

i = 0
for key in data:
    #s = json.dumps( data[key], ensure_ascii=False ).encode('utf8')
    school_data = json.loads( data[key] )
    print school_data['result']['records'][0][u'łącze TV - do 1 Mbit']
    i += 1
    if i == 1: break
