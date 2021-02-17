from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
import numpy as np
import pickle

"""
Here is a simple regression model (Gradient boosted tree) that can predict house price.

"""

data = load_boston()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

# Prediction with gradient boosted tree
clf = GradientBoostingRegressor()
clf.fit(X_train, y_train)

predicted = clf.predict(X_test)
expected = y_test

# Print the error rate
print("RMS: %r " % np.sqrt(np.mean((predicted - expected) ** 2)))

# To save model to file
with open("clf.pkl", "wb") as f:
    pickle.dump(clf, f)