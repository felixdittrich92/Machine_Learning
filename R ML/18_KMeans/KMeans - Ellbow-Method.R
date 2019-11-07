# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(data.table)
library(ggplot2)
library(caret)

cars <- fread("autos_prepared.csv")

cars.scaled <- scale(cars[, c("yearOfRegistration", "price")])

xs <- 2:10
ys <- sapply(xs, function(x) {
  model <- kmeans(cars.scaled, x)
  return(model$tot.withinss)
})

qplot(xs, ys, geom = "line")

