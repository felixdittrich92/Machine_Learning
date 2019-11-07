# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(data.table)
library(ggplot2)
library(caret)

source("helper.R")

data <- fread("classification.csv")
data$success <- as.factor(data$success)

set.seed(42)
train.index <- createDataPartition(data$success, p = 0.75, list = FALSE)
train <- data[train.index, ]
test <- data[-train.index, ]

# Aufgabe: Erstelle eine Validation-Curve f�r einen randomForest, und ermittle
#          so die ideale Groesse für die einzelnen Baeume!
#          Tipp: Rufe dazu die Dokumentation für die randomForest()-Funktion auf,
#                und schaue dir den Parameter "maxnodes" an. 
#
# --------------------------------->
#  [Allgemein] -----> [Spezifisch]

library(randomForest)

xs <- 2:25
test.acc <- numeric(0)
train.acc <- numeric(0)

for (x in xs) {
  model <- randomForest(success ~ age + interest, data = train, maxnodes = x)
  
  pred.test <- predict(model, test, type = "class")
  pred.test.acc <- confusionMatrix(pred.test, test$success)$overall["Accuracy"]
  test.acc <- c(test.acc, pred.test.acc)
  
  pred.train <- predict(model, train, type = "class")
  pred.train.acc <- confusionMatrix(pred.train, train$success)$overall["Accuracy"]
  train.acc <- c(train.acc, pred.train.acc)
}

data <- data.frame(x = xs, train = train.acc, test = test.acc)
print(data)

# install.packages("tidyr")
library(tidyr)
plot_data <- gather(data, "type", "value", -x)

g <- qplot(x = x, y = value, data = plot_data, color = type, geom = "path")
print(g)


