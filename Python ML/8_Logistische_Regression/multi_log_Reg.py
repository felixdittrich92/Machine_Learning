# multinomiale Logistische Regression / in R wichtig, da es dort keine OneVsAll - Klassifizierung gibt in Python wird diese
# bei der logistischen Regression als default verwendet

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.multiclass import OneVsOneClassifier

df = pd.read_csv("foods.csv")

Y = df["clss"].values
X = df.drop(["brands", "countries", "product_name", "clss"], axis = 1)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# One-vs-all: Sklearn hat automatisch erkannt, wir möchten hier
#             mehrere Klassen vorhersagen - daher wird per default
#             die One-vs-all-Methode (OneVsRestClassifier) verwendet. 

model = LogisticRegression(solver='newton-cg', multi_class='multinomial') #solver/multi_class siehe Doku
model.fit(X_train, Y_train)

print(model.score(X_test, Y_test))
