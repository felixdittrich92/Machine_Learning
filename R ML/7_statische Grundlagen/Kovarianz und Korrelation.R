# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(data.table)
library(ggplot2)
library(caret)

data <- fread("classification.csv")

# Wir fügen eine extra Spalte hinzu
data$extra <- rnorm(nrow(data), 5, 16)

# Wichtig: Alle Spalten müssen numerisch sein!
data$success <- as.numeric(data$success)

# Kovarianz
print(cov(data))

# Korrelation
print(cor(data))

# Aber Achtung!
x <- c(1, 2, 3, 4, 5, 6, 7)
y <- c(1, 1, 0, 0, 0, 1, 1)

print(cov(x, y))
print(cor(x, y))