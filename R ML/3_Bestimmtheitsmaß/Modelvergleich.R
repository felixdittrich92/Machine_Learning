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
hotels <- fread("hotels.csv")

for (i in 1:10) {
  # Train / Test
  train.index <- createDataPartition(hotels$`Preis in Mio`, list = FALSE, p = 0.75)
  train <- hotels[train.index, ]
  test <- hotels[-train.index, ]
  
  options(scipen = 100) #verringert Exponentialschreibweise
  
  model.profit <- lm(`Preis in Mio` ~ Quadratmeter + Gewinn, data = train)
  model.noprofit <- lm(`Preis in Mio` ~ Quadratmeter, data = train)
  
  test$`Preis in Mio (Vorhersage, mit Gewinn)` <- predict(model.profit, test)
  test$`Preis in Mio (Vorhersage, ohne Gewinn)` <- predict(model.noprofit, test)
  
  #Bestimmtheitsmaß berechnen
  #print(summary(model.profit)$r.squared)
  r2.profit <- rSquared(test$`Preis in Mio`, test$`Preis in Mio` - test$`Preis in Mio (Vorhersage, mit Gewinn)`)
  r2.noprofit <- rSquared(test$`Preis in Mio`, test$`Preis in Mio` - test$`Preis in Mio (Vorhersage, ohne Gewinn)`)
  
  print(paste(r2.profit, "-", r2.noprofit))
}



