# -*- coding: utf-8 -*-

class BrummBrumm(object):
	
	def __init__(self, verbrauch_pro_km, max_fuellmenge, aktuelle_fuellmenge, kilometerstand):
		self.verbrauch_pro_km = float(verbrauch_pro_km)
		self.max_fuellmenge = max_fuellmenge
		self.aktuelle_fuellmenge = aktuelle_fuellmenge
		self.kilometerstand = kilometerstand 
	def fahren(self, weg):
		gesamtverbrauch = weg * self.verbrauch_pro_km
		if  self.aktuelle_fuellmenge < gesamtverbrauch:
			noch_tanken = gesamtverbrauch - self.aktuelle_fuellmenge
			print u"Tank wird leer gehen. Bitte {} Liter nachtanken!".format(noch_tanken)
		else:
			rest_benzin = self.aktuelle_fuellmenge - gesamtverbrauch
			rest_km = rest_benzin / self.verbrauch_pro_km
			kilometerstandnachfahrt = self.kilometerstand + weg
			print u"Noch {} Liter Bezin. Kannst noch {} Km fahren. Kilometerstand {}".format(rest_benzin, rest_km, kilometerstandnachfahrt)
			 
		
	def tanken(self, benzinmenge):
		if self.aktuelle_fuellmenge + float(benzinmenge) > self.max_fuellmenge:
			print u"max. Fuellmenge überschritten."
		else:
			self.aktuelle_fuellmenge += benzinmenge
			print u"Es werden {} nachgefüllt.".format(float(benzinmenge), self.aktuelle_fuellmenge)

mein_auto = BrummBrumm(0.149, 70.0, 15.0, 10000)
mein_auto.tanken(55)
mein_auto.fahren(390.0)
