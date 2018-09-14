# -*- coding: utf-8 -*-

string = "Hardware nennt man die Teile eines Computers die man treten kann"
print string

stueckchen = string.split(" ")

print stueckchen
liste = stueckchen

print liste[0]


"""
ngramm = liste[0].split(" ")

print ngramm
"""

li = []
for buchstabe in liste[0]:
    print buchstabe
    li.append(buchstabe)
print li

print li[0::]
print "Das Wort", liste[0], "hat", len(li), "n-gramme"

"""
Das Wort wort hat die n-Gramme ['n-Gramm1', 'n-Gramm2', ...]
"""
