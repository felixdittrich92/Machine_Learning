# K-Nearest-Neighbor dient zur Klassifizierung (Algorithmus)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("iris.csv")

# Welche Spalten sollen zur Vorhersage verwendet werden
y = df["Species"].values
X = df.drop(["Id", "Species"], axis = 1).values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

scaler = StandardScaler()
scaler.fit(X_train)

X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(multi_class='auto', solver='lbfgs')
model.fit(X_train, y_train)

print(model.score(X_test, y_test))

model = KNeighborsClassifier(n_neighbors = 5) # n_neighbors default ist 5
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
