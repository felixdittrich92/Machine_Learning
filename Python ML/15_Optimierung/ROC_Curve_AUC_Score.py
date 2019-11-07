import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, roc_auc_score
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

y_test_predicted = model.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_test_predicted) # siehe Doku

plt.plot(fpr, tpr)
plt.xlabel("False positiv rate")
plt.ylabel("True positiv rate")
plt.show()

print("Fläche unter der Kurve :")
print(roc_auc_score(y_test, y_test_predicted))