import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from helper import plot_classifier

df = pd.read_csv("classification.csv")

y= df["success"].values
X = df[["age", "interest"]].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.25)

model = GaussianNB()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))

plot_classifier(model, X_train, y_train, proba=False, xlabel="Alter", ylabel="Interesse")

plot_classifier(model, X_test, y_test, proba=False, xlabel="Alter", ylabel="Interesse")

plot_classifier(model, X_train, y_train, proba=True, xlabel="Alter", ylabel="Interesse")
