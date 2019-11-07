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
data$success <- as.logical(data$success)

set.seed(42)
train.index <- createDataPartition(data$success, p = 0.75, list = FALSE)
train <- data[train.index, ]
test <- data[-train.index, ]

model <- glm(success ~ age + interest, train, family = binomial())
pred <- predict(model, test, type = "response")

# install.packages("ROCR")
library(ROCR)

p <- prediction(pred, test$success)
perf <- performance(p, measure="tpr", x.measure="fpr")

plot(perf)

auc <- performance(p, measure = "auc")
print(auc@y.values[[1]])
