# install.packages("stringr")
library(stringr)

sentences <- c(
  "Hallo Welt",
  "Meine E-Mail-Adresse ist hallo+welt@codingcourses.tv",
  "Bitte keine E-Mails an info@codingcourses.tv senden",
  "Bitte keine E-Mails an info@www.codingcourses.tv senden",
  "Saturday@ Hotel XYZ findet ein Event statt. Zur Teilnahme, E-Mail an veranstaltung@codingcourses.tv schicken")

for (sentence in sentences) {
  match <- str_extract(sentence, "[a-zA-Z0-9\\+]+@[a-zA-Z0-9]+\\.[\\.a-zA-Z0-9]+")
  if (!is.na(match)) {
    print(match)
  }
}
