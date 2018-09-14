# -*- coding: utf-8 -*-

import csv

with open("caesar_de_bello_gallico.txt", "r") as datei:
    inhalt = datei.read()

satzzeichen = ".,:;!?"
for zeichen in satzzeichen:
    inhalt = inhalt.replace(zeichen, "")    
    
inhalt = inhalt.lower()   

liste_woerter = inhalt.split()





woerter_haeufigkeit = {}
for wort in liste_woerter:
    if wort not in woerter_haeufigkeit:
        woerter_haeufigkeit[wort] = 1
    else:
        woerter_haeufigkeit[wort] = woerter_haeufigkeit[wort] + 1




with open('haeufigkeit.csv', 'wb') as csv_file:
  

    w = csv.writer(csv_file)
    w.writerow(woerter_haeufigkeit.keys())
    w.writerow(woerter_haeufigkeit.values())



