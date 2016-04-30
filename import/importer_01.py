import urllib
import json

service_url='https://api.um.warszawa.pl/api/action/datastore_search?resource_id=0a131e16-ec7f-4502-9b62-8f8af58d8cfd&'
checkout='https://api.um.warszawa.pl/api/action/datastore_search?resource_id=0a131e16-ec7f-4502-9b62-8f8af58d8cfd&filters={"Nr RSPO":"1"}'

while True:
    rspo=input('Enter RSPO of the school: ')
    if len(str(rspo))<1:
        print "Wrong RSPO number"
        break

    rspo_value=""" "Nr RSPO : " """+str(rspo) 
    print rspo_value

    #url=service_url+urllib.urlencode({"limit": 5, 'filters': str({"Nr RSPO": rspo})})
    #print url
    #content=urllib.urlopen(url)
    #print content
