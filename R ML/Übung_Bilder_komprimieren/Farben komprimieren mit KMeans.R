# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(ggplot2)

# install.packages("imager")
library(imager)

dragon <- load.image("dragon.png")

df <- as.data.frame(dragon, wide = "c")
head(df)

model <- kmeans(df[, c("c.1", "c.2", "c.3")], 15, iter.max = 100, nstart = 5)
print(model)

df$cc <- rgb(model$centers[model$cluster, ])
head(df)

g <- ggplot(df, aes(x = x, y = y)) +
  geom_raster(aes(fill = cc)) + 
  scale_fill_identity() + 
  scale_y_reverse()
print(g)