import pandas as pd
import numpy as np
from sklearn.model_selection import learning_curve
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.linear_model import LogisticRegression
#from sklearn.utils import shuffle
import matplotlib.pyplot as plt 

df = pd.read_csv("classification.csv")

y = df["success"].values
X = df[["age", "interest"]].values

#X, y = shuffle(X, y)

train_sizes_abs, train_scores, test_scores = learning_curve(KNeighborsClassifier(), X, y)
#train_sizes_abs, train_scores, test_scores = learning_curve(LogisticRegression(), X, y)

plt.plot(train_sizes_abs, np.mean(train_scores, axis = 1))
plt.plot(train_sizes_abs, np.mean(test_scores, axis = 1))
plt.show()