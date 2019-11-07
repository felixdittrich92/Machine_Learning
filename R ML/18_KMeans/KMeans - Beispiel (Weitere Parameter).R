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

model <- kmeans(cars.scaled, 3, iter.max = 100, nstart = 4, algorithm = "MacQueen")
print(model$centers)

# install.packages("DMwR")
library(DMwR)
centers <- data.table(unscale(model$centers, cars.scaled))

g <- qplot(cars$yearOfRegistration, cars$price, 
           color = as.factor(model$cluster),
           xlab = "Erstzulassung", 
           ylab = "Wert in Euro") +
  geom_point(aes(x = yearOfRegistration, y = price), color = "black", data = centers) +
  labs(color='Cluster #')

print(g)
