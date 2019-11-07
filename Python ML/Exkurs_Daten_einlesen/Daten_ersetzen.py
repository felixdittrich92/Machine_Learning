import pandas as pd
import numpy as np

df = pd.read_csv("classification.csv")
print(df.head())

print(df[df["age"] < 18].head())

#df["age"] = 19  #ersetzt alle Werte in dieser Spalte durch 19
#print(df.head()) 

#df["age"] = np.where(df["age"] < 18, "minderjährig", "volljährig") # ersetzt Zahlenwerte durch Wörter
#print(df)

df["interest"] = df["interest"] * 5 # komplette Spalteninhalte * 5

df["age2"] = np.where(df["age"] < 18, "minderjährig", "volljährig") # Spalte hinzufügen
print(df)