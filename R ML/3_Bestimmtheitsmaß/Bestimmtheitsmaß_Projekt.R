# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# Benoetigte Libraries laden
library(ggplot2)
library(scales)
library(stats)
library(data.table)
library(caret)
library(miscTools)

# Daten einlesen 
cars <- fread("autos_prepared.csv")

for (i in 1:10) {
  # Train / Test
  train.index <- createDataPartition(cars$price, list = FALSE, p = 0.75)
  train <- cars[train.index, ]
  test <- cars[-train.index, ]
  
  options(scipen = 100) #verringert Exponentialschreibweise
  
  model <- lm(price ~ kilometer, data = train)
  model.ps <- lm(price ~ kilometer + powerPS, data = train)
  
  test$price.pred <- predict(model, test)
  test$price.pred <- predict(model.ps, test)
  
  r2.without.ps <- rSquared(test$price, test$price - test$price.pred)
  r2.with.ps <- rSquared(test$price, test$price - test$price.pred.ps)
  
  print(paste(r2.without.ps, "-", r2.with.ps))
}