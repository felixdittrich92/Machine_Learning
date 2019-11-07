import pandas as pd
import numpy as np

df = pd.read_csv("classification.csv")
#print(df.head())

print(df.sort_values("age").head()) # sortieren nach Spalte //inplace = True// ersetzt altes Dataframe
print(df.info()) # Info über Einträge
print(df.describe()) # Mittelwert / Median / Maximum / Minimum ...
