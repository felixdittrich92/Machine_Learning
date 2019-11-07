import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from helper import plot_classifier

# Daten anzeigen
df = pd.read_csv("classification.csv")

Y = df["success"].values
X = df[["age", "interest"]].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25)
# Daten skalieren
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Daten vorhersagen
model = LogisticRegression()
model.fit(X_train, Y_train)
print(model.score(X_test, Y_test))
Y_predicted = model.predict(X_test)

plt.scatter(X_test[:, 0], X_test[:, 1], c=Y_predicted)  # Alter Interesse Farbe
yellow_patch = mpatches.Patch(color='yellow', label='buyed')
purple_patch = mpatches.Patch(color="purple", label = "not buyed")
plt.legend(handles=[purple_patch, yellow_patch],  loc='upper right')
plt.xlabel("Alter")
plt.ylabel("Interesse")
plt.show()

# Entscheidungsgrenze visualisieren
plot_classifier(model, X_train, Y_train, proba=False, xlabel="Alter", ylabel="Interesse")
plot_classifier(model, X_test, Y_test, proba=False, xlabel="Alter", ylabel="Interesse")

# Entscheidungsgrenze visualisieren mit Übergang
plot_classifier(model, X_train, Y_train, proba=True, xlabel="Alter", ylabel="Interesse")