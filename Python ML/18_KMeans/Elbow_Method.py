import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("autos_prepared.csv")

X = df[["yearOfRegistration", "price"]]

scaler = StandardScaler()
X_transformed = scaler.fit_transform(X)

scores = []
for n in range(2, 10):
    model = KMeans(n_clusters = n)
    model.fit(X_transformed)
    scores.append(model.inertia_) # Summe der quadrierten Abstände (Fehlerterm)

plt.plot(range(2, 10), scores)
plt.show()