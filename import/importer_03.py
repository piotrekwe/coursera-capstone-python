import urllib

service_url='https://api.um.warszawa.pl/api/action/datastore_search?resource_id=0a131e16-ec7f-4502-9b62-8f8af58d8cfd&'
source_name=raw_input('Enter file name of rpso numbers ')
def rpso_generator(file_name) :
    source=open(file_name)
    container=list()
    for item in source:
        try:
            value=int(item)
        except:
            continue
        container.append(value)
    return container

rpso_data=rpso_generator(source_name)

for item in rpso_data :
    rspo=item

    rspo_value='''{"\ufeffNr RSPO":"'''+str(rspo)+'''"}'''

    url=service_url+urllib.urlencode({'filters': rspo_value })
    data=urllib.urlopen(url).read()
    print data
    # for lines in urllib.urlopen(url) :
    #     print lines

    break
