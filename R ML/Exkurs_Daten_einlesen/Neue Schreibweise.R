# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# install.packages("data.table")
library(data.table)

# g <- expand.grid(a = c(1, 2), b = c(3, 4))
# print(class(g))
# print(g)

df <- fread("classification.csv")
df[, success := as.factor(success)]
# df$success <- as.factor(df$success)
print(summary(df))
