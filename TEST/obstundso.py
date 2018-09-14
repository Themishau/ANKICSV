# -*- coding: utf-8 -*-

obstliste = {}



while 1==1:
 obst = raw_input("Bitte Obstsorte eingeben: ")
 anzahl = int(raw_input("Bitte Anzahl eingeben: "))
 obstliste[obst] = anzahl

 if raw_input("Noch eine Eingabe? Wenn nicht, dann geben Sie nein ein:   ") == "nein":
     
     break
print "Eingabe beendet."


print  "Inventur", obstliste.items() 


#Laufe nach der Eingabe aller Daten mit einer Schleife über dieses Dictionary und gib jeweils die Obstsorte und die Anzahl der vorhandenen Einheiten aus. 
#Bin mir nicht sicher, ob das gemeint ist.

