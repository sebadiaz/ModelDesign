'''
Created on 24 mai 2017

@author: buissondiaz
'''
from numpy import genfromtxt
import numpy as np
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
clf = LogisticRegression(C=0.03, class_weight='auto')
print X_scaled
clf.fit(np.nan_to_num(X), y)
print(clf)
