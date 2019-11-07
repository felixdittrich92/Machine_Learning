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
# Quelle: https://www.kaggle.com/shivam2503/diamonds
diamonds <- fread("diamonds.csv")

splits = createMultiFolds(diamonds$price, k = 4, times = 10)

r2.carat = numeric()
r2.xyz = numeric()

for (split in splits) {
  train <- diamonds[split, ]
  test <- diamonds[-split, ]
  
  # Teil 1: Lineare Regression auf Basis der Spalte "carat"
  model1 <- lm(price ~ carat, data = train)
  test$model1 <- predict(model1, test)
  r2.carat <- c(r2.carat, rSquared(test$price, test$price - test$model1))
  
  # Teil 2: Lineare Regression auf Basis der Spalten "x", "y" und "z"
  model2 <- lm(price ~ x + y + z, data = train)
  test$model2 <- predict(model2, test)
  r2.xyz <- c(r2.xyz, rSquared(test$price, test$price - test$model2))
}

print(mean(r2.carat))
print(mean(r2.xyz))
val <- (mean(r2.carat) - mean(r2.xyz))
if (val > 0.025) {
  print("ist signifikant")
}else {
  print("ist nicht signifikant")
}


