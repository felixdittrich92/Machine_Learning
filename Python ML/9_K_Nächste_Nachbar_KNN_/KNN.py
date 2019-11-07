# K-Nearest-Neighbor dient zur Klassifizierung (Algorithmus)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from helper import plot_classifier

df = pd.read_csv("classification.csv")

# Welche Spalten sollen zur Vorhersage verwendet werden
y = df["success"].values
X = df[["age", "interest"]].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = KNeighborsClassifier(n_neighbors = 10) # n_neighbors default ist 5
model.fit(X_train, y_train)

print(model.score(X_test, y_test))

# Trainings-Daten plotten
plot_classifier(model, X_train, y_train, proba = False, xlabel = "Alter", ylabel = "Interesse")

# Testdaten plotten
plot_classifier(model, X_test, y_test, proba = False, xlabel = "Alter", ylabel = "Interesse")

plot_classifier(model, X_train, y_train, proba = True, xlabel = "Alter", ylabel = "Interesse")
# weiß unsicher
# rot / blau sicher