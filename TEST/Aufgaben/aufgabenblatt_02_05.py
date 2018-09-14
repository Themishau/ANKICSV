# -*- coding: utf-8 -*-
import re

muster = r'^<([A-Z]+_[A-Z]+)>(?!break)[",a-z,0-9]+</\1>$' 
text = "<PUSH_FORWARD>element20</PUSH_FORWARD>"
 
ergebnis = re.search(muster, text)
if ergebnis:
    print ergebnis.group(0)
else:
    print "kein Treffer"



