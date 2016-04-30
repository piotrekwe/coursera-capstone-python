import urllib
import json

service_url='https://api.um.warszawa.pl/api/action/datastore_search?resource_id=0a131e16-ec7f-4502-9b62-8f8af58d8cfd&'
warsaw="https://api.um.warszawa.pl/api/action/datastore_search?resource_id=0a131e16-ec7f-4502-9b62-8f8af58d8cfd&limit=5"
test1="""https://api.um.warszawa.pl/api/action/datastore_search?resource_id=0a131e16-ec7f-4502-9b62-8f8af58d8cfd&filters={"\ufeffNr RSPO":"70686"}"""
test2="""https://api.um.warszawa.pl/api/action/datastore_search?resource_id=0a131e16-ec7f-4502-9b62-8f8af58d8cfd&q=gimnazjum"""
while True:
    rspo=70686

    rspo_value='''{"\ufeffNr RSPO":"'''+str(rspo)+'''"}'''
    print rspo_value

    url=service_url+"&filters="+rspo_value
    for lines in urllib.urlopen(url) :
        print lines
    print url

    url=service_url+urllib.urlencode({'filters': rspo_value })
    for lines in urllib.urlopen(url) :
        print lines

    break
