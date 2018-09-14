# -*- coding: utf-8 -*-
import csv
import json


neue_liste = []

with open('uk-500.csv', 'rU') as data_file:
    reader = csv.reader(data_file, delimiter=',')
    for ding in reader:
        neue_liste.append(ding)


namendaten_dicts = []
for element in neue_liste:
    neue_json= {"first name":element[0], "last name":element[1], "company name":element[2], "address":element[3], "city":element[4], "country":element[5], "postal":element[6], "phone1":element[7], "phone2":element[8], "email":element[9], "web":element[10]}
    namendaten_dicts.append(neue_json)


print namendaten_dicts
with open("neue_namendaten.json", "w") as json_output:
		json.dump(namendaten_dicts, json_output)



    


# aus dem Seminar
"""
for element in liste:
    neue_json = {"Vorname":element[0], "Nachname":element[1], "Land":element[2], "Tore":element[3], "davon Elfmeter":element[4]}
    neue_liste.append(neue_json)
    print neue_json
"""

"""    
with open("neue_spielerdaten2.json", "w") as json_output:
        json.dump(neue_json_spielerdaten, json_output)
"""        
        

