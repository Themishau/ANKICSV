# -*- coding: utf-8 -*-

import math

class Pizza(object):

    def __init__(self, durchmesser):
        self.durchmesser = float(durchmesser)
        self.beschreibung = "Basispizza (rund)"
        self.basispreis = 4.00
        self.preis_zutat = 0.8
        self.zutaten = []

    def umfang_berechnen(self):
        umfang = 2 * math.pi * (self.durchmesser/2.0)
        return umfang

    def zutat_hinzufuegen(self, zutat):
        self.zutaten.append(str(zutat))

    def preis_berechnen(self):
        zutatenpreis = len(self.zutaten) * self.preis_zutat
        gesamtpreis = self.basispreis + zutatenpreis
        return gesamtpreis

    def pizzabeschreibung(self):
        beschreibung = "Basispizza"
        if self.zutaten:
            zutatenzusatz = ", ".join(sorted(self.zutaten))
            beschreibung += " mit folgenden Zutaten:\n   " + zutatenzusatz
        return beschreibung

if __name__ == '__main__':
    pizza_mit_extra_viel_cheese = Pizza(15)
    print pizza_mit_extra_viel_cheese.umfang_berechnen()
    print pizza_mit_extra_viel_cheese.zutat_hinzufuegen("cheese")
    print pizza_mit_extra_viel_cheese.zutat_hinzufuegen("cheese")
    print pizza_mit_extra_viel_cheese.zutat_hinzufuegen("cheese")
    print pizza_mit_extra_viel_cheese.preis_berechnen()
    print pizza_mit_extra_viel_cheese.pizzabeschreibung()
       


class Blechpizza(Pizza):
    
    def __init__(self, durchmesser, durchmesser_2):
        Pizza.__init__(self, durchmesser)
        self.seite_a = durchmesser
        self.seite_b = durchmesser_2
        self.beschreibung = "Basispizza (quadratisch)"
    
    def umfang_berechnen(self):
        umfang = 2* self.seite_a + 2* self.seite_b
        return umfang
        


if __name__ == '__main__':  
    pizza_mit_extra_viel_cheese1 = Blechpizza(10, 15)
    print pizza_mit_extra_viel_cheese1.umfang_berechnen()
    print pizza_mit_extra_viel_cheese1.zutat_hinzufuegen("cheese")
    print pizza_mit_extra_viel_cheese1.zutat_hinzufuegen("cheese")
    print pizza_mit_extra_viel_cheese1.zutat_hinzufuegen("cheese")
    print pizza_mit_extra_viel_cheese1.zutat_hinzufuegen("schinken")
    print pizza_mit_extra_viel_cheese1.preis_berechnen()
    print pizza_mit_extra_viel_cheese1.pizzabeschreibung()

