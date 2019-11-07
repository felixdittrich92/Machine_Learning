# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(ggplot2)
library(data.table)

salaries <- fread("sf_salaries.csv")

salaries.2011 <- salaries[Year == 2011, ]

print(mean(salaries[Year == 2012, TotalPay]))
print(mean(salaries[Year == 2013, TotalPay]))
print(mean(salaries[Year == 2014, TotalPay]))

print(mean(salaries$TotalPay)) #Mittelwert
print(median(salaries$TotalPay)) #Median

hist <- qplot(salaries$TotalPay, binwidth = 5000)
print(hist)