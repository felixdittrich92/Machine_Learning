# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(data.table)
library(ggplot2)
library(caret)

source("helper.R")

# Daten einlesen
data <- fread("classification.csv")
data$success <- as.logical(data$success)

# Daten in Trainings und Testdaten aufteilen
train.index <- createDataPartition(data$success, p = 0.75, list = FALSE)
train <- data[train.index, ]
test <- data[-train.index, ]

# Modell tranieren
model <- glm(success ~ age + interest, family = binomial(), data = train)
print(model)

# Modell visualisieren
g <- plot_classifier(model, train, success ~ age + interest, proba = FALSE)
print(g)

g <- plot_classifier(model, test, success ~ age + interest, proba = FALSE)
print(g)


predictions <- predict(model, test, type = "response")
print(confusionMatrix(predictions > 0.5, test$success))