import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA

train = pd.read_csv("train.csv.bz2")
test = pd.read_csv("test.csv.bz2")

X_train = train.drop("subject", axis = 1).drop("Activity", axis = 1)
y_train = train["Activity"]

X_test = test.drop("subject", axis = 1).drop("Activity", axis = 1)
y_test = test["Activity"]

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

pca = PCA(n_components = 150) #komprimieren

X_train_transformed = pca.fit_transform(X_train)
X_test_transformed = pca.transform(X_test)

clf = LogisticRegression()
clf.fit(X_train_transformed, y_train)

print(clf.score(X_test_transformed, y_test))

print(np.sum(pca.explained_variance_ratio_[:100])) # gibt Varianz (Streuung) an / mit Numpy: wieviel Streuung abgedeckt wird