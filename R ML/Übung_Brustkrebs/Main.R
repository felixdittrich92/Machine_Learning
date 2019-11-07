# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(data.table)
library(ggplot2)
library(caret)

source("helper.R")

# Aufgabe: Lese die Datei "cancer.csv" ein, und sage die Spalte "diagnosis" vorher. 
#          Erstelle dazu ein Modell, welches alle Spalten betrachtet!
#          (Die Formel hierzu ist: "diagnosis ~ .").
# 
#          Berechne anschließend die "Accuracy" auf Basis der Test-Daten!
# 
#          Folgende Warnmeldung darfst du ignorieren: 
#              glm.fit: fitted probabilities numerically 0 or 1 occurred 

cancer <- fread("cancer.csv")
cancer$id <- NULL
cancer$diagnosis <- cancer$diagnosis == "M"
print(cancer)

train.index <- createDataPartition(cancer$diagnosis, p = 0.75, list = FALSE)
train <- cancer[train.index, ]
test <- cancer[-train.index, ]

model <- glm(diagnosis ~ ., data = train, family = binomial(), control = list(maxit = 100))

test$diagnosis.pred <- predict(model, test, type = "response")

result <- print(confusionMatrix(table(test$diagnosis.pred > 0.5, test$diagnosis)))
print(result$overall["Accuracy"])

