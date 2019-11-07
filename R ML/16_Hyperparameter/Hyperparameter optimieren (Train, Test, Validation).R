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
levels(data$success) <- make.names(levels(data$success))

set.seed(42)
train.index <- createDataPartition(data$success, p = 0.75, list = FALSE)
train <- data[train.index, ]
test <- data[-train.index, ]

# Caret Dokumentation: https://topepo.github.io/caret/index.html
# install.packages("kernlab")

params <- expand.grid(sigma = seq(0.5, 2, 0.25), C = seq(0.5, 2, 0.5))

# install.packages("randomForest")
model <- train(success ~ age + interest, 
               method = "svmRadial", 
               data = train,
               # preProcess = c("scale", "center"),
               trControl = trainControl(
                 method = "repeatedcv", 
                 repeats = 10, 
                 classProbs = TRUE),
               tuneGrid = params)

print(model)

pred <- predict(model, test)
print(confusionMatrix(pred, test$success)$overall["Accuracy"])

