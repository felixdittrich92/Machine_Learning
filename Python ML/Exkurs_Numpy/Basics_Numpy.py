import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("fields.csv")
print(df.head())
print(df.values)

# Numpy Arrays
numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(numbers * 2)
print(numbers[0])
e = [0, 3]
print(numbers[e])
print(numbers[[6, 8]])

One = np.ones(5) # 5 x die 1 in Array
print(One)
Zero = np.zeros(5) # 5 x die 0 in Array
print(Zero)
print(Zero + 2)
print(np.repeat(2, 5)) # 5 x die 2 im Array
print(np.arange(1, 10)) # von bis 
print(np.arange(1, 10, 2)) # von bis abstand
print(np.linspace(0, 2018, 10)) # 10 Werte aus Bereich mit gleichem Abstand

x = np.arange(0, 20, 1)
plt.plot(x, x ** 2) # ** 2 = Quadrat
plt.show()
print(x ** 2)

x = np.arange(0, 20, 5)
plt.plot(x, x ** 2) # ** 2 = Quadrat
plt.show()

print("----------------------------------")

# Numpy Matrizen
m = np.array([[1, 2, 3], [4, 5, 6]])
print(m)
print(m.shape)
print(np.ones((2, 3)))
print(np.arange(1, 7).reshape(2, 3)) # erstellt Matrix von bis / Zeile Spalte
print(m.reshape(6))
print(np.arange(1, 10).reshape(3, -1)) # -1 mach den Rest(Spalten) automatisch
print(np.arange(0, 10).reshape(-1, 5)) # -1 mach den Rest(Zeilen) automatisch
print(m.reshape(-1))

print("----------------------------------")

# np.where()
print(np.where([True, False], [1, 2], [3, 4])) #[1 -True, 2- False] [3 - True, 4-False]
noten = np.array([1, 2, 3, 4, 5, 6])
print(noten <= 4 ) # True False
print(np.where(noten <= 4, "bestanden", "nicht bestanden"))

print("----------------------------------")

df2 = pd.read_csv("diamonds.csv")
print(np.where(df2["color"] == "D")) 
df2["color"] = np.where(df2["color"] == "D", 1, 0)
print(df2.head())
df2["cut"] = np.where(df2["cut"] == "Premium", "Premium++", df2["cut"])
print(df2.head())