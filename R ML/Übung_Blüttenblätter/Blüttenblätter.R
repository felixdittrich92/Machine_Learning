# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(data.table)
library(ggplot2)
library(caret)

# Aufgabe: Um was f�r eine Pflanzenart handelt es sich?
# Sage dazu die Spalte `Species` vorher. Teile die Daten dazu zuerst 
# in Trainings- und Testdaten auf. Vergleiche dann folgende Modelle:
# 
# - Logistische Regression (multinom über das nnet-Modul)
# - KNN (mit verschiedenen Werten für k, z.B. k = 1, k = 3, k = 5)
#
# Beachte, dass du die Daten für das KNN-Modell skalieren musst. 
#
# Welches Modell hat die beste Accuracy auf den Testdaten?
#
# Hinweis: 
#  - Die Spalte Id wird für das Modell nicht benoetigt, diese Spalte
#    sollte also auf keinen Fall in die Berechnung vom Modell mit
#    einfliessen.
#  - Du moechtest hier die Spalte `Species` vorhersagen. Diese enthaelt
#    drei verschiedene Werte - du moechtest sie daher vor der Berechnung
#    in einen Factor umwandeln: iris$Species <- as.factor(iris$Species) 

iris <- fread("iris.csv")
iris$Species <- as.factor(iris$Species)
print(iris)

train.index <- createDataPartition(iris$Species, p = 0.75, list = FALSE)
train <- iris[train.index, ]
test <- iris[-train.index, ]

library(nnet)
model <- multinom(Species ~ SepalLengthCm + SepalWidthCm + PetalLengthCm + PetalWidthCm,
                  data = train)
pred <- predict(model, test)
print(confusionMatrix(pred, test$Species)$overall["Accuracy"])

######

model.knn <- knn3(Species ~ scale(SepalLengthCm) + scale(SepalWidthCm) + scale(PetalLengthCm) + scale(PetalWidthCm),
                  k = 15, 
                  data = train)
pred.knn <- predict(model.knn, test, type = "class")
print(confusionMatrix(pred.knn, test$Species)$overall["Accuracy"])

