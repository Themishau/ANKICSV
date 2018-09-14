# -*- coding: utf-8 -*-

class Auto(object):
    # Klassenvariable zur Vergabe einer aufsteigenden Id
    _auto_id = 0

    def __init__(self, verbrauch, benzinstand, kilometerstand):
        print 'Ein neues Auto rollt aus der Fabrik...'
        self._verbrauch = float(verbrauch)
        self._benzinstand = float(benzinstand)
        self._kilometerstand = float(kilometerstand)
        Auto._auto_id += 1
        self._id = Auto._auto_id
    
    def tanken(self, liter):
        """ Methode, um die Fuellmenge eines Autotanks zu veraendern.
        Erwartet wird ein Parameter als integer, der die Benzinmenge
        angibt.
        Noch zu pruefen waere, ob der Tank nicht ueberlaeuft und ob der
        uebergebene Wert evtl. negativ ist. Wie soll das Programm
        sich in dem Fall verhalten? """
        self._benzinstand += liter
        print 'Benzinstand nach dem Tanken:', self._benzinstand, 'Liter'

    def fahren(self, kilometer):
        """ Methode, die das Fahren eines Autos realisiert. Als
        Parameter wird die Anzahl der Kilometer als integer erwartet. """
        print 'Das Auto soll', kilometer, 'Kilometer fahren'
        verbrauch_fahrt = (kilometer/100) * self._verbrauch
        if self._benzinstand < verbrauch_fahrt:
            print 'So weit kann ich nicht fahren.'
            print 'Benzinstand:', self._benzinstand, ' Verbrauch fuer Fahrt: ', verbrauch_fahrt
        else:
            self._benzinstand -= verbrauch_fahrt
            self._kilometerstand += kilometer
            print 'Ich bin', kilometer, 'Kilometer gefahren'
            print 'Neuer Tachostand:', self._kilometerstand
            print 'Neuer Benzinstand:', self._benzinstand

if __name__ == '__main__':
    auto = Auto(5, 0, 0)
    auto.tanken(20)
    auto.fahren(1000)
    auto.tanken(40)
    auto.fahren(1000)
    print auto._auto_id
    auto2 = Auto(6,0,0)
    print auto2._auto_id
