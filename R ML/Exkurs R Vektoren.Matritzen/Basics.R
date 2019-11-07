if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# Vektoren
a <- c(4, 5)
print(a)

b <- -1:50
print(b)

c <- seq(1, 10, 2)
print(c)

d <- c(1, 2, 3)
print(d * 2)

e <- c(1, 2, "Hallo")
print(e)

f <- c(6, 7, 8, 9, 10)
print(f[1])

g <- c(1, 2)
print(f[g])

print(f[c(3, 4, 3)])

# Zugriff über die Index-Schreibweise
success = c(0, 1, 1, 1, 0, 1, 0)
h <- c("nicht bestanden", "bestanden") #1  2
print(h[success + 1])

# Zugriff über TRUE/FALSE-Werte
entries <- c(1, 2, 3)
print(entries[c(TRUE, TRUE, FALSE)])
print(entries[c(TRUE)])

print("--------------------------")

# Elemente benennen
v <- c(30, 120000, 1)
names(v) <- c("Quadratmeter", "Preis", "Anzahl Zimmer")
print(v)
print(v[2])
print(v["Quadratmeter"])
print(v[c("Quadratmeter", "Preis")])
print(names(v))

print("--------------------------")

# Matrizen
m <- matrix((1:6), ncol = 3, byrow = TRUE)  #nrow - Spalte / byrow - erst Zeile dann Spalte füllen
print(m)
print(m[2, ])
print(m[ ,2])
print(m[2, 3])

m[2, 3] <- 7
print(m)

print("Spalte setzen")
m[ , 2] <- c(8, 9)
print(m)

n <- matrix((1:6), ncol = 3, byrow = TRUE)
print(n[1:2, 2:3])

print("--------------------------")

# Matrizen benennen
o <- matrix(c(30, 120000, 1, 60, 250000, 2), ncol = 3, byrow = TRUE)
colnames(o) <- c("Quadratmeter", "Preis", "Zimmer")
rownames(o) <- c("Erste", "Zweite")
print(o)

print("--------------------------")

# DataTables
library(data.table)

diamonds <- fread("diamonds.csv")
print(diamonds)
print(diamonds[, c("carat", "cut")])
print(diamonds[, c(carat, cut)])
print(diamonds[, .(carat, cut)])

print(diamonds[1:10], )
print(diamonds[diamonds$cut == "Premium",])
print(diamonds[diamonds$cut == "Premium" | diamonds$cut == "Good",])
print(diamonds[cut == "Premium"])
diamonds[cut == "Premium" | cut == "Good",]$price = 10000
print(diamonds)
