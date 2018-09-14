# -*- coding: utf-8 -*-


from sklearn import tree
# erstellt automatisch klassen und gewichte fuer zukünftige Sachen

"""
features = [[140, "weich"][130, "weich"][150, "hart"][170, "hart"]] # als input
labels = ["apfel", "apfel", "orange", "orange"] # output
"""
#samples fuer machine learning
#decision tree
features = [[140, 1],[130, 1],[150, 0],[170, 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels) # fit steht für find patterns in data. 
print (clf.predict([[160,0]]))
