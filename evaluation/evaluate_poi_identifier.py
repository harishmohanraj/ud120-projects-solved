#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.cross_validation import train_test_split
from sklearn.tree import tree
from sklearn.metrics import accuracy_score, precision_score, recall_score

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.30, random_state=42)

### it's all yours from here forward!  
clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
acc = accuracy_score(labels_test, pred)

print "How many POI's are identified in your test set", pred
print "The length of your test set", len(pred)
print "Actual label", labels_test
print "predicted label", pred

combined_list = zip(labels_test, pred)
true_positive = 0
for i, j in combined_list:
    if i == 1 and j == 1:
        true_positive += 1
print "True positive value", true_positive

precision_value = precision_score(labels_test, pred)
recall_value = recall_score(labels_test, pred)
print "precision_score", precision_value
print "recall_score", recall_value
