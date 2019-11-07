# 3D

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("train.csv.bz2")

X = df.drop("subject", axis = 1).drop("Activity", axis = 1)
y = df["Activity"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

pca = PCA(n_components=3)
pca.fit(X)

X_transformed = pca.transform(X) 

fig = plt.figure(figsize = (15, 10)) #Breite , Höhe
ax = fig.add_subplot(111, projection="3d")

for activity in y.unique():
    X_transformed_filtered = X_transformed[y == activity, :]
    ax.scatter(
        X_transformed_filtered[:, 0], 
        X_transformed_filtered[:, 1], 
        X_transformed_filtered[:, 2], 
        label = activity, 
        s=4
    ) 

plt.legend()
plt.show()
