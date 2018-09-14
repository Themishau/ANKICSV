# -*- coding: utf-8 -*-
import re

muster = r"^(\d{1,4}),(\d{2})(€)$" #wie die aufgabe davor nur mit ^ und $
text = "35,99€"
 
ergebnis = re.search(muster, text)
if ergebnis:
    print ergebnis.group(0)
else:
    print "kein Treffer"
