# Hyperparameter sind die einzelnen Parameter der verschiedenen Modelle bzw. die optimierten

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from helper import plot_classifier

df = pd.read_csv("classification.csv")

y = df["success"].values
X = df[["age", "interest"]].values

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier(n_neighbors = 5))
])

#pipeline.set_params(knn__n_neighbors = 1) # Parameter nachträglich ändern

X_train, X_test, y_train, y_test = train_test_split(X, y)
pipeline.fit(X_train, y_train)

print(pipeline.score(X_test, y_test))