#Mittelwert : 5 + 8 +8 +9 +5 = 35 / 5 = 7
#Median : 1 2 4 5 -> 3

import numpy as np
import pandas as pd

incomes = [10000, 30000, 5000000]
print(np.median(incomes))
print(np.mean(incomes))

df = pd.read_csv("diamonds.csv")

print(df["carat"].median())
print(df["carat"].mean())

print(df.mean()) #Mittelwert aller Spalten