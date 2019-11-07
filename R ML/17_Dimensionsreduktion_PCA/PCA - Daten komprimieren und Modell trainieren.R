# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(data.table)
library(ggplot2)
library(caret)

# Daten: https://www.kaggle.com/uciml/human-activity-recognition-with-smartphones/data

# install.packages("R.utils")
library(R.utils)
if (!file.exists("train.csv")) {
  bunzip2("train.csv.bz2", "train.csv", remove = FALSE, skip = TRUE)
}
if (!file.exists("test.csv")) {
  bunzip2("test.csv.bz2", "test.csv", remove = FALSE, skip = TRUE)
}

train <- fread("train.csv")
train$subject <- NULL
train$Activity <- as.factor(train$Activity)

test <- fread("test.csv")
test$subject <- NULL
test$Activity <- as.factor(test$Activity)

train.pca <- prcomp(train[, -"Activity"], center = TRUE, scale. = TRUE, rank. = 25)
train.compressed <- as.data.table(train.pca$x)
train.compressed$Activity <- train$Activity

test.compressed <- predict(train.pca, test[, -"Activity"])

library(nnet)
model <- multinom(Activity ~ ., data = train.compressed)
print(model)

pred <- predict(model, test.compressed)
print(confusionMatrix(pred, test$Activity))