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

train.pca <- prcomp(train[, -"Activity"], center = TRUE, scale. = TRUE, rank. = 3)

# install.packages("RColorBrewer", "rgl", "car")
library(RColorBrewer)
library(car) # Companion to Applied Regression

scatter3d(train.pca$x[, 1], train.pca$x[, 2], train.pca$x[, 3], 
          groups = train$Activity,
          surface = FALSE,
          ellipsoid = TRUE, 
          surface.col = brewer.pal(6, "Dark2"))
