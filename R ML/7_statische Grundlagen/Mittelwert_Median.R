# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# Benoetigte Libraries laden
library(ggplot2)
library(data.table)

diamonds <- fread("diamonds.csv")

print(mean(diamonds$price)) #Mittelwert
print(median(diamonds$price)) #Median

print(summary(diamonds)) #komplette Übersicht mit min, max, median, Mittelwert, ...