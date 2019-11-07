import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from helper import plot_classifier

df = pd.read_csv("classification.csv")

y = df["success"].values
X = df[["age", "interest"]].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = SVC(kernel="linear", C=0.1) # Parameter C ignoriert einzelne Punkte um die Trennline "besser" zu ziehen
                                    # großes C - beachte jeden Punkt (jeder Punkt ist wichtig) / Entscheidungsgrenze passt sich stark den Punkten an
                                    # niedriges C - gewichtet Punkte nicht so stark / Entscheidungsgrenze passt sich den allgemeinen Trends an
model.fit(X_train, y_train)

print(model.score(X_test, y_test))

# Trainings-Daten plotten
plot_classifier(model, X_train, y_train, proba = False, xlabel = "Alter", ylabel = "Interesse")

# Testdaten plotten
plot_classifier(model, X_test, y_test, proba = False, xlabel = "Alter", ylabel = "Interesse")