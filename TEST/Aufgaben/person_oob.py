# -*- coding: utf-8 -*-

class Person(object):
	def __init__(self, name):
		self._name = name
	
	def sag_deinen_namen(self):
		return self._name
	
	def neuer_name(self, name_neu):
		self._name = name_neu

      
if __name__ == '__main__':
	eine_person = Person("Katharina")
    
	print eine_person.sag_deinen_namen()
	eine_person.neuer_name("Berta")
    
