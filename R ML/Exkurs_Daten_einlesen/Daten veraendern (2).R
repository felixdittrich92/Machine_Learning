# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# install.packages("data.table")
library(data.table)

df <- fread("classification.csv")
# df[, adult := age >= 18]
# df[, success := as.logical(success)]

# df[, `:=`(adult = age >= 18, success = as.logical(success))]

# df[, age := NULL]
# df[, `:=`(age = NULL, interest = NULL)] mehrere Spalten beeinflussen

df[, c("age", "interest") := .(age + 100, NULL)]

print(df)

