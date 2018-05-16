# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:47:23 2017

@author: singh
"""

from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size= .5)

##from sklearn import tree
##clf = tree.DecisionTreeClassifier()

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()



clf.fit(X_train, y_train)

predictions = clf.predict(X_test)
print (predictions)

from sklearn.metrics import accuracy_score
print (accuracy_score(y_test, predictions))