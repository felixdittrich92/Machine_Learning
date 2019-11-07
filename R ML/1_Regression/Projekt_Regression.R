# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# Benoetigte Libraries laden
library(ggplot2)
library(scales)
library(stats) # Eigentlich nicht benoetigt, wird i.d.R. automatisch geladen
library(data.table)

# Aufgabe: Auf Basis des Kilometerstandes den Verkaufspreis vorhersagen

# Aufgabe (Teil 1): Daten einlesen
cars <- fread("autos_prepared.csv")

# Aufgabe (Teil 2): Scatter-Plot zeichnen
g <- qplot(kilometer, price, data = cars)
print(g)

# Aufgabe (Teil 3): Modell berechnen
model <- lm(price ~ kilometer, data = cars)
print(model)
# Verkaufspreis = 15990 - 0.08797 * km

# Aufgabe (Teil 4): In Grafik einzeichnen
g <- qplot(kilometer, price, data = cars) + 
  geom_smooth(method = "lm", se = FALSE, color = I("red")) #zeichnet die Linie

print(g)