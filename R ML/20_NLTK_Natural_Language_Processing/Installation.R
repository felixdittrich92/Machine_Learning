# HINWEISE
# 
# Damit dieses Script funktioniert, muss dein System einige Vorraussetzungen erfüllen...
#
# Mac: Hier muessen die XCode Command Line Tools installiert werden. Zudem wird Java benoetigt.
#      Beide kannst du über das Terminal installieren:
#       - xcode-select --install
#       - java --version
# 
# Linux: Hier muessen auch einige Tools installiert werden, damit Pakete gebaut werden
#        koennen. Beispiel für Ubuntu: 
#         - sudo apt-get install make openjdk-9-jdk
#  
# Windows: Hier muessen auch einige Dinge beachtet werden:
#         - Java muss installiert sein. Bei mir (Windows 10) wurden folgende Versionen von Java benoetigt:
#             - http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html
#             - Java 8 (32 bit): Windows x86
#             - Java 8 (64 bit): Windows x64
#             - Java 9 hat bei mir nicht funktioniert
#             - Ich empfehle das JRE, nicht das JDK. Das JDK enthaelt zwar auch ein JRE, aber dann musst
#               du die Systemvariable JAVA_HOME ggf. manuell setzen.
#         - WICHTIG: Beide Versionen von Java mussten installiert sein (32 und 64 bit)
#         - Zudem muss R Pakete selbst erstellen koennen. Dazu müssen die rTools installiert sein:
#            - Du musst Rtools für die korrekte Version von R installieren
#            - Diese findest du über ein print(version[["version.string"]]) heraus
#            - https://cran.r-project.org/bin/windows/Rtools/


# Sicherstellen, dass rJava installiert ist, aber noch nicht laden
if (!"rJava" %in% rownames(installed.packages())) {
  install.packages("rJava")
}

# Mac
if (Sys.info()['sysname'] == 'Darwin') {
  javahome <- system2('/usr/libexec/java_home',stdout = TRUE)[1]
  libjvm <- paste0(javahome, '/jre/lib/server/libjvm.dylib')
  if (!file.exists(libjvm)) {
    # Java 9 hat anscheinend keinen "jre" - Ordner mehr
    libjvm <- paste0(javahome, '/lib/server/libjvm.dylib')
  }
  if (!file.exists(libjvm)) {
    stop("Ist Java korrekt installiert?")
  } else {
    message (paste0('Load libjvm.dylib from: ', libjvm))
    dyn.load(libjvm)
    
    # Java-Installation wurde gefunden. Jetzt noch als
    # Umgebungsvariable setzen, damit spaeter RDRPOSTagger
    # installiert werden kann.
    Sys.setenv(JAVA_HOME=javahome)
  }
}

# Linux
if (Sys.info()['sysname'] == 'Linux') {
  print("Versuche, JAVA HOME zu finden")
  print(" -- Wichtig: Es muss das JDK installiert sein, das JRE reicht nicht aus!")
  if (Sys.getenv("JAVA_HOME") == "") {
    javahome <- system2('/usr/bin/jrunscript', ' -e \'java.lang.System.out.println(java.lang.System.getProperty("java.home"));\'',stdout = TRUE)[1]
    print(paste("Java Home: ", javahome))
    Sys.setenv(JAVA_HOME=javahome)
  }
}

# Windows
if (Sys.info()['sysname'] == "Windows") {
  # Installing rTools
  if (!require("devtools", quietly = TRUE)) {
    install.packages("devtools")
    library(devtools)
  }
  if (!require("corpus", quietly = TRUE)) {
    install.packages("installr")
    library(installr)
  }
  install.Rtools()
  
  rbit <- Sys.info()[["machine"]]
  if (rbit == "x86-64") {
    print("[DEBUG] R laeuft mit 64 bit")
    print("Bitte achte darauf, dass Java 8 JDK in 32 *und* 64 bit installiert ist!")
  } else if (rbit == "x86-32") {
    print("[DEBUG] R laeuft mit 32 bit")
  }
}

# Versuche, Java zu laden...
library("rJava")
if (!"rJava" %in% loadedNamespaces()) {
  print("rJava konnte nicht geladen werden. Liegt Java in der richtigen Version (32/64 bit vor)?")
}

if (!require("corpus", quietly = TRUE)) {
  install.packages("corpus")
  library("corpus")
}
if (!require("data.table", quietly = TRUE)) {
  install.packages("data.table")
  library("data.table")
}
if (!require("rJava", quietly = TRUE)) {
  install.packages("rJava")
  library("rJava")
}
if (!require("RDRPOSTagger", quietly = TRUE)) {
  install.packages("RDRPOSTagger", repos = "http://www.datatailor.be/rcube", type = "source")
  library("RDRPOSTagger")
}
if (!require("NLP", quietly = TRUE)) {
  install.packages("NLP")
  library("NLP")
}
if (!require("tm", quietly = TRUE)) {
  install.packages("tm")
  library("tm")
}
if (!require("stringr", quietly = TRUE)) {
  install.packages("stringr")
  library("stringr")
}
if (!require("plyr", quietly = TRUE)) {
  install.packages("plyr")
  library("plyr")
}
if (!require("R.utils", quietly = TRUE)) {
  install.packages("R.utils")
  library(R.utils)
}

# Extract file
if (!file.exists("Reviews_10000.csv") && file.exists("Reviews_10000.csv.bz2")) {
  bunzip2("Reviews_10000.csv.bz2", remove = FALSE)
}
