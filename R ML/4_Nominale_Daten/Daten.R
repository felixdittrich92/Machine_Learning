# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}


# Benoetigte Libraries laden
library(ggplot2)
library(scales)
library(stats)
library(data.table)
library(caret)
library(miscTools)

# Daten einlesen. Der encoding-Parameter sorgt dafuer, dass Umlaute aus der Datei
# immer korrekt eingelesen werden.
hotels <- fread("hotels.csv", encoding = "UTF-8")

hotels$Stadt <- as.factor(hotels$Stadt)

train.index <- createDataPartition(hotels$`Preis in Mio`, p = 0.75, list = FALSE)
train <- hotels[train.index, ]
test <- hotels[-train.index, ]

# Hiermit verringern wir die Fälle, in denen R die Exponentialschreibweise
# verwendet
options(scipen = 100)

# Modell trainieren
model <- lm(`Preis in Mio` ~ Quadratmeter + Gewinn + Stadt, data = train)
print(model)

# Preis in Mio = 6.117182689 + qm * 0.003946123 + Gewinn * 0.000008606 + [Stadt Koeln] * -2.693788942 
#  + [Stadt München] * 3.344617983 

# Daten vorhersagen
test$`Preis in Mio (Vorhersage)` <- predict(model, test)
print(rSquared(test$`Preis in Mio`, test$`Preis in Mio` - test$`Preis in Mio (Vorhersage)`))