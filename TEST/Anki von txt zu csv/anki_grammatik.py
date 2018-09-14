# -*- coding: utf-8 -*-
import csv
import itertools
with open('grammatik_liste.txt', 'r', encoding="utf8") as input_file:
    # zeilenweise einlesen, jedes Listenelement ist ein Datensatz
    liste = input_file.readlines()

with open('grammatik_saetze.txt', 'r', encoding="utf8") as input_file:
    # zeilenweise einlesen, jedes Listenelement ist ein Datensatz
    beispielsaetze = input_file.readlines()

"""
to do: Liste ändern, dass für jede grammatik ein satz oder sowas.
"""

neue_liste = []
neue_beispielsaetze = []
kompakt_liste = []
zeilen1 = 0
zeilen2 = 0
for grammatik in liste:
    #print (grammatik)
    #zeilen1 += 1
    #grammatik_split = grammatik.split("Tobi")
    #print (grammatik_split)
    #print (len(grammatik_split))
    neue_liste.append(grammatik) #bei kombi mit +";"
 
#speichern nur grammatikliste    
with open('anki_grammatik_liste.csv', 'w', encoding="utf8") as csv_file1:
    # writer-Objekt anlegen, Trennzeichen und Quoting festlegen
    #writer = csv.writer(csv_file,delimiter=';') #, delimiter=';'
    # komplette Liste auf einmal schreiben
    #writer.writerows(kompakt_liste)
    for eintrag in neue_liste:
        eintrag = eintrag.replace("\n", "")
        eintrag = eintrag.replace("\t", " ")
        csv_file1.write(eintrag + "\n")  
        
for satz in beispielsaetze:
    #print (satz)
    #zeilen2 += 1
    grammatik_satz_split = satz.split("\t")
    print (grammatik_satz_split)
    #print (len(grammatik_satz_split))
    neue_beispielsaetze.append(grammatik_satz_split)

#speichern nur saetzeliste
with open('anki_grammatik_saetze.csv', 'w', encoding="utf8") as csv_file2:
    # writer-Objekt anlegen, Trennzeichen und Quoting festlegen
    writer = csv.writer(csv_file2, delimiter=';') #, delimiter=';' # "Anführungszeichen entfernen!
    # komplette Liste auf einmal schreiben
    writer.writerows(neue_beispielsaetze)
    
#for element in neue_liste:
#    print (element)
#print (neue_liste[0]) #jedes element eine liste
#print (neue_liste[1])


for l1,l2 in zip(neue_liste, str(neue_beispielsaetze)):
    kompakt_liste.append(l1+l2)
    

#kompakte_liste = [response for ab in zip_longest(neue_liste, neue_beispielsaetze, fillvalue='-')for response in ab]

for element in kompakt_liste:
    print (element)

with open('anki_grammatik.csv', 'w', encoding="utf8") as csv_file:
    # writer-Objekt anlegen, Trennzeichen und Quoting festlegen
    #writer = csv.writer(csv_file,delimiter=';') #, delimiter=';'
    # komplette Liste auf einmal schreiben
    #writer.writerows(kompakt_liste)
    for eintrag in kompakt_liste:
        eintrag = eintrag.replace("\n", "")
        eintrag = eintrag.replace("\t", " ")
        csv_file.write(eintrag + "\n")




    
    """
    for eintrag in neue_beispielsaetze:
        eintrag = eintrag.replace("\n", "")
        eintrag = eintrag.replace("\t", " ")
        csv_file2.write(eintrag + "\n")  
    """

"""
for grammatikliste in neue_liste: 
    #print (grammatikliste) # jede liste in der großen Liste
    #print (len(grammatik_split))
   
   # for wort in grammatikliste:
   #     print (wort)
   #     print (len(wort))
"""
