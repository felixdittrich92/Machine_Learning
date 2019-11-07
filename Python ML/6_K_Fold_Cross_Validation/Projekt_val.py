import pandas as pd
import numpy as np
from sklearn.model_selection import RepeatedKFold
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

df = pd.read_csv("diamonds.csv")

Y = df[["price"]].values
X = df[["carat"]].values
X1 = df[["x", "y", "z"]]

kf = RepeatedKFold()

scores = cross_val_score(LinearRegression(), X, Y, cv = kf)
scores1 = cross_val_score(LinearRegression(), X1, Y, cv = kf)
print(np.mean(scores))
print(np.mean(scores1))

if (np.mean(scores) - np.mean(scores1)) > 0.025:
    print("ist signifikant (carat bestimmt Preis besser)")
else:
    print("ist nicht signifikant")
