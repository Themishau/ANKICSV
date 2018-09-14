# -*- coding: utf-8 -*-
import csv

# Oeffnen der Datei im Lesemodus
with open('torschuetzen_fifa_wm_2014.txt', 'r') as input_file:
    # zeilenweise einlesen, jedes Listenelement ist ein Datensatz
    torschuetzen = input_file.readlines()

spielerdaten = []

for spieler in torschuetzen:
    # Auftrennen der Datenzeile am Leerzeichen, erzeugt neue Liste
    # Entfernen von Whitespace-Zeichen durch strip() hier nicht notwendig
    # da durch das Splitten nur Werte übrigbleiben, die auch Inhalt
    # besitzen, d.h. nicht nur aus Whitespace-Zeichen bestehen
    # sofern noetig, so zu realisieren: daten_spieler = [datum.strip() for datum in daten_spieler]
    daten_spieler = spieler.split()
    # Entfernen der Klammern um den letzten Eintrag
    daten_spieler[-1] = daten_spieler[-1][1:-1]
    # Eintrag der Spielerdaten als Liste in Liste fuer alle Spielerdaten
    spielerdaten.append(daten_spieler)

# Oeffnen der Datei im Schreibmodus
# Binaerzusatz, damit nicht nach jeder Datenzeile eine Leerzeile auftritt
with open('torschuetzen_fifa_wm_2014.csv', 'wb') as csv_file:
    # writer-Objekt anlegen, Trennzeichen und Quoting festlegen
    writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
    # komplette Liste auf einmal schreiben
    writer.writerows(spielerdaten)