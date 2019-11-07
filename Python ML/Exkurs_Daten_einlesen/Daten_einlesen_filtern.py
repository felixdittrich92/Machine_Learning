import pandas as pd

df = pd.read_csv("classification.csv")
print(df.head())
print(df["age"] > 20) # zeigt True/False
print(df[df["age"] > 20]) #zeigt nur Leute über 20
print((df["age"] > 20 ) & (df["age"] < 30)) # mehreres kombiniert & und | oder  
print(df.drop(1)) # erste Element / Zeile entfernt
print(df.drop([1, 3]))

success = df[df["success"] == 1]
print(success.head())
print(success.index) # zeigt an welche Einträge dieses Kriterium erfüllen

print(df.drop("interest", axis = 1)) # entfernt komplette Spalte