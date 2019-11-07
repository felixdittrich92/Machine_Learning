import pandas as pd
import graphviz
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from helper import plot_classifier

df = pd.read_csv("classification.csv")

y = df["success"].values
X = df[["age", "interest"]].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)

model = RandomForestClassifier(criterion="entropy", n_estimators=100) # Anzahl der Bäume im Wald
model.fit(X_train, y_train)

plot_classifier(model, X_train, y_train, proba = True, xlabel = "Alter", ylabel = "Interesse")

print(model.score(X_test, y_test))