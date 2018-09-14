# -*- coding: utf-8 -*-

class Wassernkocher(object):
	
	def _init_(self, min_fuellmenge, max_fuellmenge):
		self.min_fuellmenge = min_fuellmenge
		self.max_fuellmenge = max_fuellmenge
		self.eingeschaltet = False
		self.aktuelle_fuellmenge = 0.0
		
	def einschalten(self):
		if self.eingeschaltet:
			print "Der Wasserkocher ist bereits eingeschaltet..."
		else:
			if self.aktuelle_fuellmenge < self.min_fuellmenge:
				pring u"Es ist ein wenig Wasser im Wasserkocher! Erst nachfuelenllen!"
			else:
				self.eingeschaltet = True
				print "Der Wasserkocher ist einsatzbereit."
	def ausschalten(self):
		if not self.eingeschaltet:
			print "DerWasserkocher ist bereit ausgeschaltet."
		else:
			self.eingeschaltet = False
			print "Der aus"
				
			
	def wasser_einfuellen(self, wassermenge):
		if self_aktuelle_fuellemnge + float(wassermenge) > self.max_fuellemenge:
			print u"max fuelmenge überschritten"
		elif self.aktuelle_fuellmenge + float(wassermenge) < self.min_fuellmenge:
			print u"Die minimale ist nicht erreicht"
		else:
			self.aktuelle_fuellemenge += wassermenge
			print u"Es werden {} nachgefüllt"
	def wasser_ausgiessen(self, wassermenge):
		if float(wassermenge) > 
