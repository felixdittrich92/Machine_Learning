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

# Daten einlesen 
apartments <- fread("wohnungspreise.csv")

# install.packages("caret")
library(caret)

# Train / Test
set.seed(42)
train.index <- createDataPartition(apartments$Verkaufspreis, list = FALSE, p = 0.75)
train <- apartments[train.index, ]
test <- apartments[-train.index, ]

g <- qplot(Quadratmeter, Verkaufspreis, data = train) + 
  geom_smooth(method = "lm", se = FALSE, data = train) + #Linie
  geom_point(data = test, color = I("red")) #Testpunkte rot
print(g)

model <- lm(Verkaufspreis ~ Quadratmeter, data = train)
print(model)

test$VerkaufspreisPredicted <- predict(model, test)
print(test)