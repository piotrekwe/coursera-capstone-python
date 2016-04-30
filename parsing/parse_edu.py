#coding: utf8
import sqlite3
import json

input_name = raw_input( 'Enter input database: ' )                              #part1 polacz z tabela z raw data
if len( input_name ) < 1:
    input_name = "../import/school_internet.sqlite"
    print "Input:", input_name

try:
    in_conn = sqlite3.connect( input_name )
    in_cur = in_conn.cursor()
except: print "Could not open database"

out_conn = sqlite3.connect( "parsed_edu.sqlite" )                               #part2 stworz nowa tabele dla sparsowanych danych
out_cur = out_conn.cursor()
out_cur.execute('''DROP TABLE IF EXISTS Edu_internet ''')                       #jesli jest taka tabela, to usun
out_cur.execute('''CREATE TABLE IF NOT EXISTS Edu_internet (
    rspo INTEGER, Type TEXT, Name TEXT,
    tel_1 INTEGER, tel_2 INTEGER, tel_10 INTEGER, tel_up INTEGER,
    TV_1 INTEGER, TV_2 INTEGER, TV_10 INTEGER, TV_up INTEGER,
    fiber_1 INTEGER, fiber_2 INTEGER, fiber_10 INTEGER, fiber_up INTEGER,
    SAT_1 INTEGER, SAT_2 INTEGER, SAT_10 INTEGER, SAT_up INTEGER,
    radio_1 INTEGER, radio_2 INTEGER, radio_10 INTEGER, radio_up INTEGER,
    kom_1 INTEGER, kom_2 INTEGER, kom_10 INTEGER, kom_up INTEGER,
    State TEXT, County TEXT, Borough TEXT, Town TEXT, Street TEXT, Street_numer INTEGER,
    House_numer INTEGER, Postal_code TEXT, Post TEXT, Tel INTEGER, Email TEXT,
    Organization TEXT, Publicity TEXT, Students_category TEXT, Specificity TEXT, Kind TEXT)''') #opis po polsku niektorych skrotow jest nizej przy wpisywaniu do tabeli

data = dict()                                                                   #part3 parsowanie
in_cur.execute('''SELECT rspo, imported FROM Schools''')                        #tworzy podreczna baze danych zeby parsowac
for school in in_cur:
    data[ school[0] ] = school[1]
print "Data obtained"

in_cur.close()

n = 0                                                                           #licznik zeby wiedziec ile bylo wpisow
i = 0                                                                           #taki licznik zeby robic commit co 50 wpisow (jak Charles)
for key in data:                                                                #petla do parsowania i uzupelniania sparsowanej bazy danych
    rspo = key
    if len(data[key]) < 1: continue
    school_data = json.loads( data[key] )
    try:                                                                        # probujemy przypisac wartosci bo bez tego wywala problem ktorego nie rozumiem
        s_type = school_data['result']['records'][0][u'Typ szkoły/placówki']
        name = school_data['result']['records'][0][u'Nazwa szkoły/placówki']
        tel_1 = school_data['result']['records'][0][u'Łącze telefoniczne - do 1 Mbit']
        tel_2 = school_data['result']['records'][0][u'Łącze telefoniczne - do 2 Mbit']
        tel_10 = school_data['result']['records'][0][u'Łącze telefoniczne - do 10 Mbit']
        tel_up = school_data['result']['records'][0][u'Łącze telefoniczne - powyżej 10 Mbit']
        TV_1 = school_data['result']['records'][0][u'łącze TV - do 1 Mbit']
        TV_2 = school_data['result']['records'][0][u'łącze TV - do 2 Mbit']
        TV_10 = school_data['result']['records'][0][u'łącze TV - do 10 Mbit']
        TV_up = school_data['result']['records'][0][u'łącze TV - powyżej 10 Mbit']
        fiber_1 = school_data['result']['records'][0][u'Światłowód - do 1 Mbit']
        fiber_2 = school_data['result']['records'][0][u'Światłowód - do 2 Mbit']
        fiber_10 = school_data['result']['records'][0][u'Światłowód - do 10 Mbit']
        fiber_up = school_data['result']['records'][0][u'Światłowód - powyżej 10 Mbit']
        SAT_1 = school_data['result']['records'][0][u'Łącze SAT -do 1 Mbit']
        SAT_2 = school_data['result']['records'][0][u'Łącze SAT - do 2 Mbit']
        SAT_10 = school_data['result']['records'][0][u'Łącze SAT - do 10 Mbit']
        SAT_up = school_data['result']['records'][0][u'Łącze SAT - powyżej 10 Mbit']
        radio_1 = school_data['result']['records'][0][u'Łącze radio - do 1 Mbit']
        radio_2 = school_data['result']['records'][0][u'Łącze radio - do 2 Mbit']
        radio_10 = school_data['result']['records'][0][u'Łącze radio - do 10 Mbit']
        radio_up = school_data['result']['records'][0][u'Łącze radio - powyżej 10 Mbit']
        kom_1 = school_data['result']['records'][0][u'Łącze tel kom - do 1 Mbit']
        kom_2 = school_data['result']['records'][0][u'Łącze tel kom - do 2 Mbit']
        kom_10 = school_data['result']['records'][0][u'Łącze tel kom - do 10 Mbit']
        kom_up = school_data['result']['records'][0][u'Łącze tel kom - powyżej 10 Mbit']
        woj = school_data['result']['records'][0][u'Województwo']
        s_pow = school_data['result']['records'][0][u'Powiat']
        gm = school_data['result']['records'][0][u'Gmina']
        miej = school_data['result']['records'][0][u'Miejscowość']
        ul = school_data['result']['records'][0][u'Ulica']
        nr_d = school_data['result']['records'][0][u'Nr domu']
        nr_m = school_data['result']['records'][0][u'Nr mieszkania']
        kod = school_data['result']['records'][0][u'Kod pocztowy']
        post = school_data['result']['records'][0][u'Poczta']
        nr_tel = school_data['result']['records'][0][u'Telefon']
        mail = school_data['result']['records'][0][u'E-mail']
        org_prow = school_data['result']['records'][0][u'Typ organu prowadzącego']
        pub = school_data['result']['records'][0][u'Publiczność']
        st_cat = school_data['result']['records'][0][u'Kategoria uczniów']
        spec = school_data['result']['records'][0][u'Specyfika szkoły']
        kind = school_data['result']['records'][0][u'Rodzaj placówki']
    except: continue                                                            #jak sie nie uda to przechodzi do kolejnej iteracji i tracimy wpis

    out_cur.execute('''INSERT INTO Edu_internet
            VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )''',
            ( rspo, s_type, name,
                tel_1, tel_2, tel_10, tel_up,
                TV_1, TV_2, TV_10, TV_up,
                fiber_1, fiber_2, fiber_10, fiber_up,
                SAT_1, SAT_2, SAT_10, SAT_up,
                radio_1, radio_2, radio_10, radio_up,
                kom_1, kom_2, kom_10, kom_up,
                woj, s_pow, gm, miej, ul, nr_d, nr_m,
                kod, post, nr_tel, mail, org_prow,
                pub, st_cat, spec, kind ) )                                     #wrzucenie danych do tabeli
    i += 1
    n += 1
    if i == 50:
        out_conn.commit()
        i = 0                                                                   #zapis co 50 wpisów
out_conn.commit()                                                               #jesli danych jest wiecej niz wielokrotnosc 50 to ten zapis gwarantuje ze nie stracimy tej nadwyzki

out_cur.close()                                                                 #zamykamy, jestesmy mili dl komputera
print "Data parsed,", n, "data pieces written"
