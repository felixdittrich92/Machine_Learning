# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# install.packages("data.table")
library(data.table)

df <- fread("classification.csv")
# print(mean(df$age))

# print(df[, c(mean(age), min(age))])

# print(df[success == 1, mean(age)])
# print(df[success == 0, mean(age)])

print(df[, mean(age), by = success]) # gruppieren nach success   Zeile , was tun , gruppieren nach