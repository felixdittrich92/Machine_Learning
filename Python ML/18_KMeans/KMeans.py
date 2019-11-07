import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("autos_prepared.csv")

X = df[["yearOfRegistration", "price"]]

scaler = StandardScaler()
X_transformed = scaler.fit_transform(X)

model = KMeans(n_clusters = 3) # 3 Cluster
model.fit(X_transformed)

labels = model.labels_    # zu welchem Label welcher Pukt gehört
centers = model.cluster_centers_ # Zentrum jedes Clusters (insgesamt 3)
centers_transformed = scaler.inverse_transform(centers) # normalisieren der centers

plt.scatter(df["yearOfRegistration"], df["price"], c = labels, alpha=0.6)
plt.scatter(centers_transformed[:, 0], centers_transformed[:, 1], color="red", marker="X")
plt.show()