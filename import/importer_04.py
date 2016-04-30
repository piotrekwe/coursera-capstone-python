import urllib
import time
import sqlite3

def rpso_generator(file_name) :  # create list with rspo numbers of warsaw schools
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

conn = sqlite3.connect('school_internet.sqlite') #accessing database
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Schools (rspo INTEGER, imported TEXT)''') # checking if databases structure is already set

for item in rpso_data : #itering by rspo numbers
    current_rspo=item
    i=i+1
    cur.execute("SELECT imported FROM Schools WHERE rspo= ?", (current_rspo, )) #checking if record for this rspos already exists

    try:
        h = cur.fetchone()[0] #if there is an element with rspo_current value, we skip to next iteration
        if len(h)>1:
            print "Found in databes1: ", current_rspo
            continue
        print "Found in database2: ", current_rspo
        continue
    except:
        pass

    rspo_value='''{"\ufeffNr RSPO":"'''+str(current_rspo)+'''"}''' # potrojne ciapki spowodowane obecnoscia ciapkow w srodku
    url=service_url+urllib.urlencode({'filters': rspo_value }) # create url adress for get method
    print "Retrieving information about school with RSPO: ", current_rspo
    data=urllib.urlopen(url).read() #opening webapge and writing it to string
#ToDo: create some validation of downloaded content
    cur.execute('''INSERT INTO Schools (rspo, imported)
            VALUES ( ?, ? )''', ( current_rspo, data ) ) # now we are sure thare are no duplicates

                                 #adding downloaded information to database
    conn.commit()

print "Importing completed"
print len(rpso_data)
