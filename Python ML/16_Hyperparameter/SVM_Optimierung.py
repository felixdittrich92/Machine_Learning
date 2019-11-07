import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from helper import plot_classifier

df = pd.read_csv("classification.csv")

y = df["success"].values
X = df[["age", "interest"]].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("svm", SVC())
])


clf = GridSearchCV(pipeline, param_grid = {
    "svm__C": [0.001, 0.01, 0.1, 1, 10],
    "svm__gamma": [0.001, 0.01, 0.1, 1, 10]
})

clf.fit(X_train, y_train)
print(clf.best_params_)
print(clf.score(X_test, y_test))
#print(clf.best_estimator_)
print(clf.best_score_)