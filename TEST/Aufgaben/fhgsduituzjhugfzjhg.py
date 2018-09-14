import re

muster = r"<(\w+)>.*</\1>" # Backreference auf Gruppe 1
#(\w+) Definition </\1> auf erste Gruppe hier (\w+)
text = "<div>bla...</div>"

ergebnis = re.search(muster, text)
if ergebnis:
	print ergebnis.group(0)
else:
	print "kein Treffer"



import re

muster = r"(?P<stunden>\d{2}):(?P<minuten>\d{2})" # Name vergeben
#r für raw string keine Zeilenumbruch und so seite 38

text = "22:41"

ergebnis = re.search(muster, text)

if ergebnis:
	print "Minuten: ", ergebnis.group('minuten') # Aufruf über Name
	print "Stunden: ", ergebnis.group('stunden') # Aufruf über Name
else:
	print "kein Treffer"
	
	
(?!00)/d oder so tw1tter
(?P<tagname>\w+)
(<tagname attr_a="\w+")(attr_b="\w+">"\w+"</tagname>)

^<([A-Za-z0-9]+)( [A-Za-z_]+=".*")*>(.*)</\1>$
