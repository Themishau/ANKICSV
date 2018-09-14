import re

muster = r"<(\w+)>.*</\1>"


text = ""

ergebnis = re.search(muster, text)

if ergebnis:
	print "Minuten: ", ergebnis.group('minuten') # Aufruf über Name
	print "Stunden: ", ergebnis.group('stunden') # Aufruf über Name
else:
	print "kein Treffer"
