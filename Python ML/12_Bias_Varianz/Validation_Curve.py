"""
Bias: Die Unfähigkeit eines Verfahrens zur Erfassung der Wahrheitsbeziehung wird als Bias bezeichnet. 
Also sagt der Bias aus, dass bzw. wie genau ein Modell die realen Datensätze beschreibt. 
Umso niedriger, desto genauer ist das Modell.

Overfitting: Overfitting bedeutet, dass ein Modell so stark an die Trainingsdaten angepasst ist, 
dass es nicht mehr für reale Werte sinnvolle Ergebnisse gibt. 
Beudeutet: Wenn du einen sehr geringen Bias hast, dann ist die Wahrscheinlichkeit höher, 
dass du dein Modell overfittet hast.

Underfitting: ist das Gegenteil von Overfitting. 
Also dass ein Modell besser angepasst werden kann.

Varianz: Die Varianz sagt aus, wie gut ein Modell die Testdaten schätzt. 
Der Bias bezieht sich auf die Trainingsdaten und die Varianz auf die Testdaten. 
Wobei die Varianz zum Beispiel über den Mean Square Error berechnet werden kann.
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import validation_curve
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt 

df = pd.read_csv("classification.csv")

y = df["success"].values
X = df[["age", "interest"]].values

param_range = np.array([40, 30, 20, 15, 10, 8, 6, 5, 4, 3, 2, 1])  # setzen der zu betrachtenden Nachbarn

train_scores, test_scores = validation_curve(KNeighborsClassifier(), 
                                X, 
                                y, 
                                param_name = "n_neighbors", 
                                param_range = param_range , 
                                cv = 50) # cv - wie oft Daten gesplittet werden default ist 5mal

plt.plot(param_range, np.mean(train_scores, axis = 1)) # axis - nimm nur 1 Zeile
plt.plot(param_range, np.mean(test_scores, axis = 1))

# drehen der X-Achse, dass sie von 40 bis 1 geht
plt.xlim(np.max(param_range), 0)
plt.show()

# 40 - ca. 35 Underfitting
# 10 - 0 Overfitting
# 15 wäre optimal

