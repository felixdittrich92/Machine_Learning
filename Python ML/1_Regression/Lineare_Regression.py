import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_excel("wohnungspreise.xlsx")
print(df.head())
print(df["Verkaufspreis"])

plt.scatter(df["Quadratmeter"], df["Verkaufspreis"])
plt.show() #zeigt Punkte im Koordinatensystem

model = LinearRegression()
model.fit(df[["Quadratmeter"]], df[["Verkaufspreis"]])

print("Intercept: " + str(model.intercept_)) #Konstante
print("Coef: " + str(model.coef_)) #Koeffizient

# Verkaufspreis = 3143.28481869 + 5071.35242619 * Quadratmeter
# y = 3143.28481869 + 5071.35242619 * x

print(3143.28481869 + 5071.35242619 * 60)

print(model.predict([[60], [80]]))#schon fertige Methode aus LinearRegression()
min_x =  min(df["Quadratmeter"])
max_x = max(df["Quadratmeter"])

predicted = model.predict(([[min_x], [max_x]]))
plt.scatter(df["Quadratmeter"], df["Verkaufspreis"])
plt.plot([min_x, max_x], predicted, color="red")
plt.show()
