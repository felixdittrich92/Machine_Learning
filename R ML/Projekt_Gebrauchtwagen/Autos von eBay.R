library(data.table)

# Damit setzen wir den aktuellen Pfad auf den Pfad zur aktuellen Datei
this.dir <- dirname(parent.frame(2)$ofile)
setwd(this.dir)

if(!file.exists("autos.csv")){
  if (!require("R.utils")) {
    install.packages("R.utils")
    library(R.utils)
  }
  download.file(
    "http://downloads.codingcoursestv.eu/035%20-%20machine%20learning/data/autos.csv.bz2", 
    "autos.csv.bz2"
  )
  print("Decompressing autos.csv.bz2 to autos.csv...")
  bunzip2("autos.csv.bz2", remove = FALSE)
}

cars <- fread("autos.csv", encoding = "UTF-8")
cars[, c("dateCrawled", "abtest", "dateCreated", "nrOfPictures", "lastSeen", "postalCode", "seller", "offerType") := NULL]

cars[cars$monthOfRegistration == 0]$monthOfRegistration = 6

cars$registration <- cars$yearOfRegistration + (cars$monthOfRegistration - 1) / 12
cars[, c("yearOfRegistration", "monthOfRegistration") := NULL]

cars <- cars[cars$price != 0]
cars <- cars[cars$powerPS != 0]

cars$notRepairedDamage <- ifelse(cars$notRepairedDamage == "ja", "TRUE", cars$notRepairedDamage)
cars$notRepairedDamage <- ifelse(cars$notRepairedDamage == "nein", "FALSE", cars$notRepairedDamage)
cars <- cars[cars$notRepairedDamage != ""]
cars$notRepairedDamage <- as.logical(cars$notRepairedDamage)

cars <- cars[cars$powerPS < 200]
cars <- cars[cars$registration > 1900 & cars$registration < 2018]
print(summary(cars))

cars$fuelType <- as.factor(cars$fuelType)
print(summary(cars))

library(graphics)

pairs.data <- cars[fuelType == "benzin" | fuelType == "diesel" | cars$fuelType == "elektro"][sample(.N, 150), ]
pairs(
  pairs.data[, c("price", "kilometer", "notRepairedDamage", "registration", "powerPS")], 
  pch = 21,
  bg = c("", "", "red", "", "blue", "green", "red", "")[unclass(pairs.data$fuelType)],
  oma = c(2, 2, 2, 9))

library(GGally)
library(ggplot2)

graph <- ggpairs(
  pairs.data[, notRepairedDamage := as.integer(notRepairedDamage)],
  columns = c("price", "kilometer", "notRepairedDamage", "registration", "powerPS"),
  mapping = aes(color = fuelType))
print(graph)


library(lattice)

d <- pairs.data[,  c("price", "kilometer", "notRepairedDamage", "registration", "powerPS", "fuelType")]
graph2 <- splom(~d[, 1:4], data = d, groups = fuelType, panel = panel.superpose)
print(graph2)
