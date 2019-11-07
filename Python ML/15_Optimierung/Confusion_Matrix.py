import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from helper import plot_classifier

df = pd.read_csv("classification.csv")

y = df["success"].values
X = df[["age", "interest"]].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(solver = "lbfgs")
model.fit(X_train, y_train)

print(model.score(X_test, y_test))

y_test_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_test_pred)) 
# https://de.wikipedia.org/wiki/Beurteilung_eines_bin%C3%A4ren_Klassifikators#Wahrheitsmatrix:_Richtige_und_falsche_Klassifikationen