# Entropie - Gegenteil von Ordnung
# 0: kein Informationsgehalt (nicht wichtig) 1: Informationsgehalt (wichtig)

import pandas as pd
import graphviz
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from helper import plot_classifier

df = pd.read_csv("classification.csv")

y = df["success"].values
# Welche Spalten sollen zur Vorhersage verwendet werden
X = df[["age", "interest"]].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)

model = DecisionTreeClassifier(criterion = 'entropy', max_depth = 6) # Kriterium und Baumtiefe siehe Doku  
                                                                     # min_samples_leaf = 3 - gibt nur Verzweigungen mit mind. 3 Blättern an
model.fit(X_train, y_train)

print(model.score(X_test, y_test)) #Testdaten schätzen

# Trainings-Daten plotten
plot_classifier(model, X_train, y_train, proba = False, xlabel = "Alter", ylabel = "Interesse")

# beschreibt die einzelnen Bereiche aus dem Plot wo gekauft und wo nicht anhand der Attribute
tree = export_graphviz(model, None, 
                        feature_names= ["age", "interest"], 
                        class_names= ["nicht gekauft", "gekauft"],
                        rounded = True,
                        filled = True)

src = graphviz.Source(tree, format = "png")
src.render("datei")  # Datei als PNG abspeichern

# entropy 0.0 - genau gleich in dem Bereich / samples - Anzahl Datenpunkte
