import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("hotels.csv")
print(df.head())

X = df[["Gewinn", "Quadratmeter"]].values
y = df[["Preis in Mio"]].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)

model = LinearRegression()
model.fit(X_train, y_train)

print(model.intercept_)
print(model.coef_)

# 6.48370247 + [Gewinn] * 6.39855984e-06 + [Quadratmeter] * 3.89642288e-03

y_test_pred = model.predict(X_test)
for i in range(0, len(y_test_pred)):
    print(str(y_test_pred[i][0]) + " - " + str(y_test[i][0]))
    