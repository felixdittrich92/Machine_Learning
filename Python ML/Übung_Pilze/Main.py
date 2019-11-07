import pandas as pd
import graphviz
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz

df = pd.read_csv("mushrooms.csv")
df = pd.get_dummies(df)  # umwandeln in 0 und 1
df = df.drop("class_e", axis = 1)

y = df["class_p"].values
X = df.drop(["class_p"], axis = 1).values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)

model = DecisionTreeClassifier(criterion = 'entropy', max_depth = 6) # Kriterium und Baumtiefe siehe Doku  
                                                                     # min_samples_leaf = 3 - gibt nur Verzweigungen mit mind. 3 Blättern an
model.fit(X_train, y_train)

print(model.score(X_test, y_test)) #Testdaten schätzen

# beschreibt die einzelnen Bereiche aus dem Plot wo gekauft und wo nicht anhand der Attribute
tree = export_graphviz(model, None, 
                        feature_names = df.drop("class_p", axis = 1).columns.values,
                        class_names= ["essbar", "nicht essbar"],
                        rounded = True,
                        filled = True)

src = graphviz.Source(tree, format = "png")
src.render("datei")  # Datei als PNG abspeichern