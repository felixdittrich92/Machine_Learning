import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("autos.csv", encoding="iso8859-1")

#print(df.info())
#print(df.describe())  // PyGeoLab für Postleitzahlen 

# Daten aufbereiten
# unwichtige Daten für das Modell entfernen
df = df.drop(["dateCrawled", "abtest", "dateCreated", "nrOfPictures", "lastSeen", "seller", "offerType", "postalCode", "model"], axis = 1)

# Jahr berechnen als Kommazahl
df["monthOfRegistration"] = np.where(df["monthOfRegistration"] == 0, 6, df["monthOfRegistration"]) #wenn Wert 0 dann setze 6 also Mitte des Jahres
df["registration"] = df["yearOfRegistration"] + (df["monthOfRegistration"] - 1) / 12
df = df.drop(["yearOfRegistration", "monthOfRegistration"], axis = 1 )

# Werte die auf 0 sind entfernen
df = df.drop(df[df["price"] == 0].index)
df = df.drop(df[df["powerPS"] == 0].index)

# NaN Werte entfernen
df["notRepairedDamage"] = np.where(df["notRepairedDamage"] == "ja", 1, df["notRepairedDamage"])
df["notRepairedDamage"] = np.where(df["notRepairedDamage"] == "nein", 0, df["notRepairedDamage"])
df = df[df["notRepairedDamage"].notnull()]

# Daten visualisieren
#g = sns.pairplot(df) // "notRepairedDamage" <- Fehler 
#plt.show()
#df = df[(df["price"] < 500000) & (df["powerPS"] < 500) & (df["registration"] <= 2018)]
#g = sns.pairplot(df.sample(250), hue = "vehicleType")  # Fahrzeugtypen als Diagramm anzeigen
#plt.show()

# Strings umwandeln / unterteilen
df = pd.get_dummies(df, columns=["vehicleType", "gearbox", "fuelType", "brand"]) 

# Modell tranineren
df = df[(df["price"] > 500) & (df["price"] < 20000)]
y = df["price"]
X = df.drop(["name", "price"], axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LinearRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))

print(model.score(X_train, y_train))



