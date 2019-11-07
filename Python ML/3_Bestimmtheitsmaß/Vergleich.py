import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df = pd.read_csv("hotels.csv")
print(df.head())

scores = []

for i in range(0, 100):

    X = df[["Quadratmeter"]].values #anhand was geschätzt werden soll
    #X = df[["Gewinn"]].values
    #X = df[["Gewinn", "Quadratmeter"]].values
    y = df[["Preis in Mio"]].values #was geschätzt werden soll

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_test_pred = model.predict(X_test)

    #r2 = r2_score(y_test, y_test_pred)
    #print(r2)

    scores.append(model.score(X_test, y_test))

for score in scores:
    print(score)

print("\nBestimmtheitsmaß : ")
print(sum(scores) / len(scores)) #je näher an 1 umso genauer ist das Model