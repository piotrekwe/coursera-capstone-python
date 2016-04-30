import urllib
import time
import sqlite3

def rpso_generator(file_name) : # tworzy liste z numerami rspo szkol warszawskich
    source=open(file_name)
    container=list()
    for item in source:
        try:
            value=int(item)
        except:
            continue
        container.append(value)
    return container

service_url='https://api.um.warszawa.pl/api/action/datastore_search?resource_id=0a131e16-ec7f-4502-9b62-8f8af58d8cfd&'
i=1
source_name=raw_input('Enter file name of rspo numbers ')
if len(source_name)<1 :
    source_name="rspo.txt"

rpso_data=rpso_generator(source_name)

conn = sqlite3.connect('school_internet.sqlite') #otwieram baze danych
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Schools (rspo INTEGER, imported TEXT)''') # sprawdzam czy struktura bazy juz jest utworzona

for item in rpso_data : #interujemy po numerach rspo
    current_rspo=item
    i=i+1
    cur.execute("SELECT imported FROM Schools WHERE rspo= ?", (current_rspo, )) #sprawdza czy mamy juz w bazie rekord o danym numerze rspo

    try:
        h = cur.fetchone()[0] #jezeli udalo sie pobrac ten element z bazy danych to przechodzimy do nastepnej iteracji
        if len(h)>1:
            print "Found in databes1: ", current_rspo
            continue
        print "Found in database2: ", current_rspo
        continue
    except:
        pass

    rspo_value='''{"\ufeffNr RSPO":"'''+str(current_rspo)+'''"}''' # potrojne ciapki spowodowane obecnoscia ciapkow w srodku
    url=service_url+urllib.urlencode({'filters': rspo_value }) # tworze adres do metody get
    print "Retrieving information about school with RSPO: ", current_rspo
    data=urllib.urlopen(url).read() #otwieram strone i wpisuja ja do stringa
#powinna tu sie pojawic opcja walidacji pobranego contentu
    cur.execute('''INSERT INTO Schools (rspo, imported)
            VALUES ( ?, ? )''', ( current_rspo, data ) ) # jestesmy w czesci w ktorej mamy pewnosci ze nie mamy duplikatow

                                 #dodajemy pobrany wpis do bazy danych
    conn.commit()

print "Importing completed"
print len(rpso_data)
