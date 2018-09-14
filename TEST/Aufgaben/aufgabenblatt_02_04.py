# -*- coding: utf-8 -*-
import re

muster = r"^[A,E,I,O,U]{2}-[1-9]\d[2-7,X]-[A-E]$" #bisschen schwieriger
text = "EI-782-B"
 
ergebnis = re.search(muster, text)
if ergebnis:
    print ergebnis.group(0)
else:
    print "kein Treffer"
