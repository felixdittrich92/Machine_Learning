import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv("fields.csv")

Y = df[["profit"]].values
X = df[["width", "length"]].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25)

model_pf = PolynomialFeatures(include_bias = False)
model_pf.fit(X_train)

X_train_transformed = model_pf.transform(X_train)[:, [0, 2]]
X_test_transformed = model_pf.transform(X_test)[:, [0, 2]]
print(model_pf.powers_)
#width ^ 1 * length ^ 0     ^0 = 1
#....

model_lr = LinearRegression()
model_lr.fit(X_train_transformed, Y_train)

print(model_lr.score(X_test_transformed, Y_test))
