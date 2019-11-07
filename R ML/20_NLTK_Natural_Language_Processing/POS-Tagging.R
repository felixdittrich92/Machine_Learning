# Damit setzen wir das Working Directory auf den Ordner dieser Datei
if (!is.null(parent.frame(2)$ofile)) {
  this.dir <- dirname(parent.frame(2)$ofile)
  setwd(this.dir)
}

# Sicherstellen, dass alle Pakete korrekt geladen werden, etc. 
source("Installation.R", echo = FALSE)

######################################################################

library(RDRPOSTagger)

# https://www.sketchengine.co.uk/penn-treebank-tagset/
# https://www.linguistik.hu-berlin.de/de/institut/professuren/korpuslinguistik/mitarbeiter-innen/hagen/STTS_Tagset_Tiger

tagger <- rdr_model(language = "German", annotation = "UniversalPOS")
r <- rdr_pos(tagger, x = "Er geht in den neuen Supermarkt.")
print(r)

tagger <- rdr_model(language = "German", annotation = "POS")

# Hinweis: Sollte bei dir der Umlaut in "Boese" nicht korrekt angeziegt werden, musst du
#          die Datei als UTF-8 oeffnen. 
#          Das geht ueber File -> Reopen with Encoding...

r <- rdr_pos(tagger, x = "Das Böse ist böse.")
print(paste(r$token, r$pos, sep = "/", collapse = " "))

