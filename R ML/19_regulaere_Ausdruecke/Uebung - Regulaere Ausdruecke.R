#######################################################################################
# Hinweis: Sollten bei dir die Umlaute nicht korrekt angezeigt werden, so musst du 
#          die Datei als UTF-8 oeffnen. Das geht ueber File -> Reopen with Encoding...
#######################################################################################

# Übung: Reguläre Ausdrücke

# **Aufgabe:** Extrahiere die Datumsangaben mit Hilfe von regulären Ausdrücken.
# In diesem Fall sind die Datumswerte in verschiedenen Formaten angegeben. Du wirst
# daher u.U. mehrere reguläre Ausdrücke benötigen, um alle Datumsangaben zu extrahieren.

# Beispiel:
# match1 <- str_extract(s, "[...]")
# match2 <- str_extract(s, "[...]")
# if (!is.nan(match1)) {
#   print(match1)
# } else if (!is.nan(match2)) {
#   print(match2)
# }
#
# Bonusaufgabe 1: Schau dir die ifelse-Funktion in R an. Bekommst du eine
# Lösung komplett ohne for-Schleife hin?

library(stringr)

sentences <- c("Am 05.06.2018 findet ein cooles Event statt",
               "Please follow our invitation and visit us on 2018/14/05",
               "Im Monat 05/2018 ist oft gutes Wetter",
               "Der Lottogewinn war 10.000.000€ groß. Er wurde am 04.06.2018 ausgeschüttet",
               "Im Monat 01/2018 war in Sofia heftiger Smog",
               "Dein Flug in den Urlaub geht am 06.07.2018")

for (s in sentences) {
  match1 <- str_extract(s, "[0-9]{2}\\.[0-9]{2}\\.[0-9]{4}")
  match2 <- str_extract(s, "[0-9]{4}/[0-9]{2}/[0-9]{2}")
  match3 <- str_extract(s, "[0-9]{2}/[0-9]{4}")
  
  if (!is.na(match1)) {
    print(match1)
  } else if(!is.na(match2)) {
    print(match2)
  } else if(!is.na(match3)) {
    print(match3)
  }
}

match1 <- str_extract(sentences, "[0-9]{2}\\.[0-9]{2}\\.[0-9]{4}")
match2 <- str_extract(sentences, "[0-9]{4}/[0-9]{2}/[0-9]{2}")
match3 <- str_extract(sentences, "[0-9]{2}/[0-9]{4}")

match <- ifelse(!is.na(match1), match1, ifelse(!is.na(match2), match2, match3))
print(match)


# Bonusaufgabe 2: Wandel zudem auch alle Datumsangaben in ein einheitliches 
# Format um. Wenn  nur ein Monat angegeben ist, setze den Tag auf den Monatsersten. 

# Bonusaufgabe 2 - Schwere Lösung: Schau dir dazu auf jeden Fall die Datumsfunktionen
# von R an (strptime, strftime, ...), insbes. die Funktion strptime.
# Damit kannst du einen Datumswert nach R einlesen. Beachte, dass du hier das korrekte
# Format übergeben musst. Ggf. wirst du bei einem Datumsformat (Monat/Jahr)
# die fehlende Tag-Angabe über die paste()-Funktion hinzufügen müssen.

# **Bonusaufgabe 2 - Einfachere Lösung:** Alternativ kannst du auch einfach nur mit 
# einem strsplit(), die einzelnen Datumswerte z.B. am "." oder am "/" aufteilen,
# und anschließend in korrekter Reihenfolge mit einem paste() wieder zusammenführen. 

# **Bonusaufgabe - gewünschte Ausgabe:**
# 05.06.2018
# 14.05.2018
# 01.05.2017
# 04.06.2018
# 01.01.2018
# 06.07.2018

for (s in sentences) {
  match1 <- str_extract(s, "[0-9]{2}\\.[0-9]{2}\\.[0-9]{4}")
  match2 <- str_extract(s, "[0-9]{4}/[0-9]{2}/[0-9]{2}")
  match3 <- str_extract(s, "[0-9]{2}/[0-9]{4}")
  
  if (!is.na(match1)) {
    print(match1)
  } else if(!is.na(match2)) {
    d <- strptime(match2, "%Y/%d/%m")
    print(strftime(d, "%d.%m.%Y"))
  } else if(!is.na(match3)) {
    d <- strptime(paste("01/", match3, sep = ""), "%d/%m/%Y")
    print(strftime(d, "%d.%m.%Y"))
  }
}