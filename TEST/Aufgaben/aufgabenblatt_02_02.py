# -*- coding: utf-8 -*-
import re

muster = r"(DE)\d{20}" 
text = "DE21301204000000015228"
 
ergebnis = re.search(muster, text)
if ergebnis:
    print ergebnis.group(0)
else:
    print "kein Treffer"

# War hier nicht viel zu ändern.
