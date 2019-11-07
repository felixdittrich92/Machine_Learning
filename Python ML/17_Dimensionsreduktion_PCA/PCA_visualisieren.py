# 2D

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv("train.csv.bz2")

X = df.drop("subject", axis = 1).drop("Activity", axis = 1)
y = df["Activity"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

pca = PCA(n_components=2)
pca.fit(X)

X_transformed = pca.transform(X) 

plt.figure(figsize = (15, 10)) #Breite , Höhe
#Zeile 5 bis Ende 5:,   5 bis 10 5:10, // , alle Spalten //Listcomprahantions
for activity in y.unique():
    X_transformed_filtered = X_transformed[y == activity, :] #['STANDING' 'SITTING' 'LAYING' 
    #'WALKING' 'WALKING_DOWNSTAIRS' 'WALKING_UPSTAIRS']
    plt.scatter(X_transformed_filtered[:, 0], X_transformed_filtered[:, 1], label = activity, s=4) #s = Größe der Punkte

plt.legend()
plt.show()

#print(y.unique()) # zeigt jeden "Zustand" einmal an