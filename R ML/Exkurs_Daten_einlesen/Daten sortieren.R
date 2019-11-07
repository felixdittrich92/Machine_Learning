# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# install.packages("data.table")
library(data.table)

df <- fread("classification.csv")
# print(df[order(age)])

# print(df[order(success, age)])
# print(df[order(-age)])

setorder(df, age)
print(df)