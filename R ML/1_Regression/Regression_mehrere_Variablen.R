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

# Daten einlesen 
hotels <- fread("hotels.csv")


# Train / Test
train.index <- createDataPartition(hotels$`Preis in Mio`, list = FALSE, p = 0.75)
train <- hotels[train.index, ]
test <- hotels[-train.index, ]

options(scipen = 100) #verringert Exponentialschreibweise

model <- lm(`Preis in Mio` ~ Quadratmeter + Gewinn, data = train)
print(model)

test$`Preis in Mio (Vorhersage)` <- predict(model, test)
print(test)