# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

library(ggplot2)

# install.packages("imager")
library(imager)

dragon <- load.image("dragon.png")
# dragon[,450:470,,] <- 0
plot(dragon)
print(dragon[,450:470,,])

dragon <- dragon * 1.5 - 0.5

cscale <- function(r, g, b) {
  rgb(
    pmin(1, pmax(0, r)), 
    pmin(1, pmax(0, g)), 
    pmin(1, pmax(0, b)))
}
plot(dragon, colorscale = cscale, rescale = FALSE)