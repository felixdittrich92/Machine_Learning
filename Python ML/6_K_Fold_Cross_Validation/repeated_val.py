import pandas as pd
import numpy as np
from sklearn.model_selection import RepeatedKFold
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

df = pd.read_csv("hotels.csv") 

Y = df[["Preis in Mio"]].values
X = df[["Gewinn", "Quadratmeter"]].values

kf = RepeatedKFold()
print(cross_val_score(LinearRegression(), X, Y, cv = kf))
scores = cross_val_score(LinearRegression(), X, Y, cv = kf)
print(np.mean(scores))