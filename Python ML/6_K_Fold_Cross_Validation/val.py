import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

df = pd.read_csv("hotels.csv") #[:6] ersten 6 Einträge

Y = df[["Preis in Mio"]].values
X = df[["Gewinn", "Quadratmeter"]].values

kf = KFold(n_splits = 4, shuffle = True) #Anzahl der Datensplits 3(default) -max. 10, shuffle - mischen (für vorsortierte Daten)

for train_index, test_index in kf.split(X):
    print("train : " + str(train_index))
    print("test : " + str(test_index))
    print("------------------")
    X_test = X[test_index]
    X_train = X[train_index]

    Y_test = Y[test_index]
    Y_train = Y[train_index]

    # Lineare Regression 
    model = LinearRegression()
    model.fit(X_train, Y_train)

    print(model.score(X_test, Y_test))

# das ganze in Kurz :
kf = KFold(n_splits=10)
print(cross_val_score(LinearRegression(), X, Y, cv = kf))
scores = cross_val_score(LinearRegression(), X, Y, cv = kf)
print(np.mean(scores))
