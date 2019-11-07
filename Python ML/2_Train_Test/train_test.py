import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_excel("wohnungspreise.xlsx")
print(df.head)

X = df[["Quadratmeter"]].values
Y = df[["Verkaufspreis"]].values

#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0, test_size=0.25)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

plt.scatter(X_train, Y_train)
plt.scatter(X_test, Y_test, color="RED")
plt.show()

model = LinearRegression()
model.fit(X_train, Y_train)

print("Intercept: " + str(model.intercept_)) #Konstante
print("Coef: " + str(model.coef_)) #Koeffizient

predicted = model.predict(X_test)
plt.scatter(X_test, Y_test, color="RED")
plt.plot(X_test, predicted)
plt.show()