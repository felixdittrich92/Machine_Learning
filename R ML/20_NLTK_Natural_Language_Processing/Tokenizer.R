# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# Sicherstellen, dass alle Pakete korrekt geladen werden, etc. 
source("Installation.R", echo = FALSE)

######################################################################

library(corpus)
library(data.table)

print(text_split("Buy this product for $ 15.99. It is amazing."))

print(text_tokens("He's going to the supermarket."))