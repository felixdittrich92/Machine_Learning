import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("autos_prepared.csv")
print(df.head())
print(df["price"])

plt.scatter(df["kilometer"], df["price"])
plt.show() #zeigt Punkte im Koordinatensystem

model = LinearRegression()
model.fit(df[["kilometer"]], df[["price"]])

print("Intercept: " + str(model.intercept_)) #Konstante
print("Coef: " + str(model.coef_)) #Koeffizient


predicted = model.predict(([[0], [50000]]))
plt.scatter(df["kilometer"], df["price"])
plt.plot([0, 50000], predicted, color="red")
plt.show()

print(" Bei 50000 km : ") 
print(model.predict([[50000]]))