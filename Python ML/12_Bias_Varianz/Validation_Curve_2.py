import pandas as pd
import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt 

df = pd.read_csv("classification.csv")

y = df["success"].values
X = df[["age", "interest"]].values

param_range = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # setzen der maximalen Tiefe

train_scores, test_scores = validation_curve(DecisionTreeClassifier(), 
                                X, 
                                y, 
                                param_name = "max_depth", 
                                param_range = param_range , 
                                cv = 3) # cv - wie oft Daten gesplittet werden default ist 5mal

plt.plot(param_range, np.mean(train_scores, axis = 1)) # axis - nimm nur 1 Zeile
plt.plot(param_range, np.mean(test_scores, axis = 1))

plt.show()