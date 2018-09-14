# -*- coding: utf-8 -*-

def spiraleausseninnen():
	kommando = input("Gib Zahl fuer die nxn-Matrix ein: \n  ")
	matrixzahl = int(kommando)*int(kommando)
	print ("Die Matrix wird", matrixzahl, "gross sein.")
	print ("-------------------")
	print ("-------------------")
	print ("-------------------\n\n\n")

	#null löschen und letzte Zahl hinzufügen
#-----------!!!WENN VON INNEN ANFAGEN DANN REIHENFOLGE HIER AENDERN!!!-----------------------
	zahlen_von_matrix = list(range(matrixzahl + 1)) 
# -----------!!!WENN VON INNEN ANFAGEN DANN REIHENFOLGE HIER AENDERN!!!----------------------- 
# oder abfrage

	del zahlen_von_matrix[0] # oder del zahlen_von_matrix[letzte Zahl bei anders herum]

	n = int(kommando)
	hochzaehlen1, hochzaehlen2 = 1,0				# Starting zaehlen
	x,y = 0,0										# startpunkt links oben
	#ERSTELLUNG DER LISTEN; ALSO DES GRIDS
	zahlenreihe = [[None]* n for j in range(n)] 								# n mal listen in denen n mal elemente sind, die "none" sind (kein value)
	print ("maximale Listenanzahl:", n, "maximale Positionen in Liste",n)
	print ("ACHTUNG! ES WIRD BEI 0 ANGEFANGEN ZU ZAEHLEN")
	print ("\n-------------------\n")
	# POSITION DER ZAHL IN DER LISTE MIT X UND Y WOBEI X DIE LISTE IST UND Y DIE POSITION IN DER LISTE ETWA WIE BEI EINER 2 dimenionalen ebene
	for zahl in zahlen_von_matrix:												# für jedes i in ganze zahlenreihe, also jede zahl 
			zahlenreihe[x][y] = zahl											# setze zahl auf position x y also listenummer und position in liste x 
			print ("Zahl", zahlenreihe[x][y], " wurde an Position: \n","listenummer:", x, "element:",y)
			print (zahlenreihe)
			nx,ny = x+hochzaehlen1, y+hochzaehlen2
			print ("neue Position...")
			if 0<=nx<n and 0<=ny<n and zahlenreihe[nx][ny] == None:				# wenn neue Listennummer x x größer als oder gleich 0 und 
				print ("-------------------")
				print ("Bedingung trifft zu.")
				print ("neue POSITION: \n listenummer:", nx, "position in liste:",ny)
				x,y = nx,ny														# nx und ny geben wieder zurück zu x, y. Bedingung stimmt. nicht verschieben
				print ("hochzaehlen1=", hochzaehlen1, "hochzaehlen2=", hochzaehlen2)
				print ("x=", x,"y=", y)
				print ("-------------------")
				print ("-------------------\n")
			else:
				print ("-------------------")
				print ("BEDINGUNG TRIFFT NICHT ZU.\n EINE ZAHL SCHON AUF POSITION.\n POSITION WIRD GEAENDERT")
				print ("hochzaehlen1=", hochzaehlen1, "hochzaehlen2=", hochzaehlen2)
				hochzaehlen1, hochzaehlen2 = -hochzaehlen2, hochzaehlen1		# wenn nicht bedingung erfüllt, dann tausche zahlen aus und - 1 bei hochzähler
				print ("hochzaehlen1=", hochzaehlen1, "hochzaehlen2=", hochzaehlen2)
				print ("tausche hochzaehlen 1 und 2 und vor hochzaehlen2 ein minus-zeichen gestellt")
				x,y = x + hochzaehlen1, y + hochzaehlen2						# addiere zu position in listen xy
				print ("neue x:", x, "neue y:",y)
				print ("-------------------")
				print ("-------------------\n")

#Ausgabearten
####################################################
	print ("AUSGABE VON ZAHLENSPIRALE")
	print ("\n")
	for reihe in zahlenreihe:
		print (*reihe)
	print()
	print ("erste Spirale")
	print ("\n")
	

	n = range(len(zahlenreihe))
	for y in n:
		for x in n:
			print ("{:2}".format(zahlenreihe[x][y]), end=" ") #methode 1 bei einzelnden digits
		print() # print enter oder so

    
	n = range(len(zahlenreihe))
	for y in n:
		print("zeilenumbruch")#wenn keine leerzeichen, dann geht alles in eine zeile
		for x in n:
			print ("%2i" % zahlenreihe[x][y], end=" ") #methode 1 bei einzelnden digits




####################################################
	print ("\n-------------------\n")
	print ("\n-------------------\n")
	print ("\n-------------------\n")


	print (" in Listenform")
	print ("\n")
	for reihe in zahlenreihe: 
		print (reihe)
	print ("\n-------------------\n")
#umgekehrt ausgeben
	print ("umgekehrt ausgegeben")
	print ("\n")
	neueliste = []	
	for liste in zahlenreihe:
		neue_liste = liste[::-1]
		neueliste.append(neue_liste)
	for reihe in neueliste:
		print (reihe)
	print ("\n-------------------\n")
	
	return zahlenreihe






#------------------------------------
#versuche und ideen ab hier
#------------------------------------
"""

position = (0,0)
position = position(+1,0)
position = (+1,0)

print (positionx, positiony)

bewegungen = matrixzahl
n = 1


#definiere Bewegungen
def rechts():
    position = position(+1,0)
    return position

def unten():
    position = position(0,-1)

def links():
    position = position(-1,0) 

def oben():
    position = position(0,+1) 
 
rechts()
rechts()
  
    
#erstelle grid gilt nur, wenn (0,0) = 1 weil nach geraden und ungeraden zahlen gefragt wird.

def gitter(self):

	grid_in_dictform = {"Zahl": , "Koordinaten":}
	zaehlen = 1	
	for zahl in zahlen_von_matrix:
		print (zahl)
		if zahl % 2: #wenn ungerade zahl, dann rechts 
			rechts()
			for zahl in zaehlen:
				unten()
				
			for zahl in zaehlen: 
				links()	
			zaehlen += 1	 
		else: # wenn gerade dann gehe links 
			links()
			for zahl in zaehlen:
				oben()
			for zahl in zaehlen: 
				rechts()
			zaehlen += 1		
	


	for listenreihe in zahlenreihe:
		listenreihe = str(listenreihe)
		listenreihe = listenreihe.replace(","," ")
		listenreihe = listenreihe.replace("[","")
		listenreihe = listenreihe.replace("]","")
		print (listenreihe)



#ausgtabe von spirale
def printe_matrix(bewegung):
	for zahl in zahlen_von_matrix:
		
	
		bewegen_r(x,y)
		bewegen_u(x,y) 
		bewegen_l(x,y)
		bewegen_o(x,y)
"""


if __name__ == '__main__':
    starte = spiraleausseninnen()
