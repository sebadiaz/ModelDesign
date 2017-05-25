'''
Created on 24 mai 2017

@author: buissondiaz
'''
from numpy import genfromtxt
import numpy as np
import pandas as pd
dataset = genfromtxt('eggs.csv', delimiter=' ')

X = dataset[:,2:11]
y = dataset[:,1]
print type(dataset[1,3])
print type(dataset[1,10])
print type(dataset[1,11])
print np.asanyarray(X)
print np.isfinite(X).all()
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn import metrics
#X, y = dataset.load_train()

raw_scaler = StandardScaler()
raw_scaler.fit(X)
X_scaled = raw_scaler.transform(X)
print np.any(np.isnan(X_scaled))
bad_indices = np.where(np.isinf(X_scaled))
print "np.inf=", np.where(np.isnan(X))
print "is.inf=", np.where(np.isinf(X))
print "np.max=", np.max(abs(X))

print(bad_indices)

print "Logisitic"
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
clf = LogisticRegression(C=0.03, class_weight='auto')
print X_scaled
clf.fit(X_train, y_train)
yscore=clf.predict(X_test)
fpr, tpr, thresholds = metrics.roc_curve(y_test, yscore, pos_label=2)
print fpr
print tpr
print thresholds
print(metrics.classification_report(y_test, yscore))
print(metrics.confusion_matrix(y_test, yscore))
print (clf.predict_proba(X_test))
print(clf)
print(pd.crosstab(y_test, yscore, rownames=['True'], colnames=['Predicted'], margins=True))

print "Discrim"
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

clf = LinearDiscriminantAnalysis()
clf.fit(X_train, y_train)
LinearDiscriminantAnalysis(n_components=None, priors=None, shrinkage=None,
              solver='svd', store_covariance=False, tol=0.0001)
yscore=clf.predict(X_test)
fpr, tpr, thresholds = metrics.roc_curve(y_test, yscore, pos_label=2)
print fpr
print tpr
print thresholds
print(metrics.classification_report(y_test, yscore))
print(metrics.confusion_matrix(y_test, yscore))
print(pd.crosstab(y_test, yscore, rownames=['True'], colnames=['Predicted'], margins=True))

print "Tree"
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
yscore=clf.predict(X_test)
fpr, tpr, thresholds = metrics.roc_curve(y_test, yscore, pos_label=2)
print fpr
print tpr
print thresholds
print(metrics.classification_report(y_test, yscore))
print(metrics.confusion_matrix(y_test, yscore))
print(pd.crosstab(y_test, yscore, rownames=['True'], colnames=['Predicted'], margins=True))

print "Adaboost"
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier()
clf.fit(X_train, y_train)
yscore=clf.predict(X_test)
fpr, tpr, thresholds = metrics.roc_curve(y_test, yscore, pos_label=2)
print fpr
print tpr
print thresholds
print(metrics.classification_report(y_test, yscore))
print(metrics.confusion_matrix(y_test, yscore))
print(pd.crosstab(y_test, yscore, rownames=['True'], colnames=['Predicted'], margins=True))

print "Random Forest"
from sklearn.ensemble import  RandomForestClassifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)
yscore=clf.predict(X_test)
fpr, tpr, thresholds = metrics.roc_curve(y_test, yscore, pos_label=2)
print fpr
print tpr
print thresholds
print(metrics.classification_report(y_test, yscore))
print(metrics.confusion_matrix(y_test, yscore))
print(pd.crosstab(y_test, yscore, rownames=['True'], colnames=['Predicted'], margins=True))

print "KNeighbors"
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
yscore=clf.predict(X_test)
fpr, tpr, thresholds = metrics.roc_curve(y_test, yscore, pos_label=2)
print fpr
print tpr
print thresholds
print(metrics.classification_report(y_test, yscore))
print(metrics.confusion_matrix(y_test, yscore))
print(pd.crosstab(y_test, yscore, rownames=['True'], colnames=['Predicted'], margins=True))

print "SVC"
from sklearn.svm import SVC
clf = SVC()
clf.fit(X_train, y_train)
yscore=clf.predict(X_test)
fpr, tpr, thresholds = metrics.roc_curve(y_test, yscore, pos_label=2)
print fpr
print tpr
print thresholds
print(metrics.classification_report(y_test, yscore))
print(metrics.confusion_matrix(y_test, yscore))
print(pd.crosstab(y_test, yscore, rownames=['True'], colnames=['Predicted'], margins=True))

print "GaussianNB"
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X_train, y_train)
yscore=clf.predict(X_test)
fpr, tpr, thresholds = metrics.roc_curve(y_test, yscore, pos_label=2)
print fpr
print tpr
print thresholds
print(metrics.classification_report(y_test, yscore))
print(metrics.confusion_matrix(y_test, yscore))
print(pd.crosstab(y_test, yscore, rownames=['True'], colnames=['Predicted'], margins=True))

print "MLP"
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier()
clf.fit(X_train, y_train)
yscore=clf.predict(X_test)
fpr, tpr, thresholds = metrics.roc_curve(y_test, yscore, pos_label=2)
print fpr
print tpr
print thresholds
print(metrics.classification_report(y_test, yscore))
print(metrics.confusion_matrix(y_test, yscore))
print(pd.crosstab(y_test, yscore, rownames=['True'], colnames=['Predicted'], margins=True))

print "QuadraticDiscriminantAnalysis"
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
clf = QuadraticDiscriminantAnalysis()
clf.fit(X_train, y_train)
yscore=clf.predict(X_test)
fpr, tpr, thresholds = metrics.roc_curve(y_test, yscore, pos_label=2)
print fpr
print tpr
print thresholds
print(metrics.classification_report(y_test, yscore))
print(metrics.confusion_matrix(y_test, yscore))
print(pd.crosstab(y_test, yscore, rownames=['True'], colnames=['Predicted'], margins=True))
#print "GaussianProcessClassifier"
#from sklearn.gaussian_process import GaussianProcessClassifier
#from sklearn.gaussian_process.kernels import RBF
#clf = GaussianProcessClassifier(1.0 * RBF(1.0), warm_start=True)
#clf.fit(X_train, y_train)
#yscore=clf.predict(X_test)
#fpr, tpr, thresholds = metrics.roc_curve(y_test, yscore, pos_label=2)
#print fpr
#print tpr
#print thresholds
#print(metrics.classification_report(y_test, yscore))
#print(metrics.confusion_matrix(y_test, yscore))
