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

# params <- expand.grid(sigma = c(0.5, 0.75, 1, 1.25, 1.5, 2), C = c(0.5, 1, 1.5, 2))
params <- expand.grid(sigma = seq(0.5, 2, 0.25), C = seq(0.5, 2, 0.5))

model <- train(success ~ age + interest, 
               method = "svmRadial", 
               data = train,
               preProcess = c("scale", "center"),
               trControl = trainControl(
                 method = "repeatedcv", 
                 repeats = 10, 
                 classProbs = TRUE),
               tuneGrid = params)

pred <- predict(model, test)
print(pred)

pred <- predict(model, test, type = "prob")
print(pred)

