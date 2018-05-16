from sklearn import tree
features=[[1400,1],[300,0],[150,0],[1700,1]]
labels = [1,0,0,1]
clf  = tree.DecisionTreeClassifier()
clf= clf.fit(features,labels)
print (clf.predict([[1700,0]]))

