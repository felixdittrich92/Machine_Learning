import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("diamonds.csv")

Y = df[["price"]].values
#X = df[["carat"]].values
X = df[["x", "y", "z"]].values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25)

# Lineare Regresion
#model = LinearRegression()
#model.fit(X_train, Y_train)
#print(model.score(X_test, Y_test))

#polynominale Regression Grad 2
model_pf = PolynomialFeatures(degree = 2, include_bias = False)
model_pf.fit(X_train)

X_train_transformed = model_pf.transform(X_train)
X_test_transformed = model_pf.transform(X_test)

model_lr = LinearRegression()
model_lr.fit(X_train_transformed, Y_train)

print(model_lr.score(X_test_transformed, Y_test))