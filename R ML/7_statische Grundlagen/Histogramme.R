# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(ggplot2)
library(data.table)

salaries = c(40000, 40000, 41000, 50000, 55000, 70000, 90000)

hist <- qplot(salaries, bins = 10) #,binwidth = .. Balkenbreite
print(hist)

diamonds <- fread("diamonds.csv")
hist2 <- qplot(diamonds$price, binwidth = 1000)
print(hist2)