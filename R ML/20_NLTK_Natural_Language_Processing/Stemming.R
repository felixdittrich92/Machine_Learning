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

print(text_tokens("He's going to the supermarket.", text_filter(
  stemmer = "en"
)))

t1 <- text_tokens("You need to buy 123 products.", text_filter(stemmer = "en", drop_number = TRUE))
t2 <- text_tokens("He needs to buy this product.", text_filter(stemmer = "en"))
print(t1)
print(t2)

print(stopwords_de)