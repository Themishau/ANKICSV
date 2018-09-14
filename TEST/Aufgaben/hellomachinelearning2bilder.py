# -*- coding: utf-8 -*-
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
fuer_test = [0, 50, 100] # nimm nur ein teil der daten; 3 Datensets
print (fuer_test)

#---------------------------------
#print (iris.feature_names)
#print (iris.target_names)
#print (iris.data[0])
#print (iris)
#---------------------------------

# daten training; lösche die drei einträge aus trainingsdaten
trainier_ziel = np.delete(iris.target, fuer_test)
print ("Ergebnis:", trainier_ziel)
trainier_daten = np.delete(iris.data, fuer_test, axis=0)
print ("Traiingsdaten:",trainier_daten)


# daten zum testen
test_ziel = iris.target[fuer_test]
test_daten = iris.data[fuer_test]
print ("Testziel:",test_ziel)
print ("Testdaten:",test_daten)


clf = tree.DecisionTreeClassifier() 
clf = clf.fit(trainier_daten, trainier_ziel) # fit steht für find patterns in data. 
			  #Eigenschaften  #Kennzeichnung/Label

#---------------------------------

#Test
print ("schon Ergebnis:",test_ziel)			  
print ("Test von Learning: ", clf.predict(test_daten))
