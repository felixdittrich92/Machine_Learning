import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from helper import plot_classifier

df = pd.read_csv("classification.csv")

y = df["success"].values
X = df[["age", "interest"]].values

X_train, X_test, y_train, y_test = train_test_split(X, y)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier())
])


clf = GridSearchCV(pipeline, param_grid = {
    "knn__n_neighbors": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
})

clf.fit(X_train, y_train)
print(clf.best_params_)
print(clf.score(X_test, y_test))
print(clf.best_estimator_)
print(clf.best_score_)