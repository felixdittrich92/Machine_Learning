# metrische Daten : sind Daten deren Abstand sinnvoll interpretiert werden kann z.B.: 1-3
# ordinale Daten : haben Rangordnung wie: morgens mittags abends
# nominale Daten : ohne Ordnung z.B.: Geschlecht m/w


import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("hotels.csv")
#OneHot Encoding
df = pd.get_dummies(df, columns = ["Stadt"])
print(df)

Y = df[["Preis in Mio"]].values
X = df[["Gewinn", "Quadratmeter", "Stadt_Berlin", "Stadt_Köln"]].values

#Spalten ignorieren
#df.drop(labels = ["Preis in Mio", "Stadt München"], axis = 1).values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25)

model = LinearRegression()
model.fit(X_train, Y_train)

print(model.score(X_test, Y_test))
#Vorhersage aus Daten Gewinn, Quadratmeter, Berlin, Köln    .... München wenn Berlin und Köln 0 sind
print(model.predict([[10000, 300, 0, 0], [5000, 200, 1, 0], [30000, 500, 0, 0], [100000, 100, 0, 1]]))


