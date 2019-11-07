# install.packages("stringr")
library(stringr)

# Hinweis: Sollten bei dir die Umlaute nicht korrekt angezeigt werden, so musst du 
#          die Datei als UTF-8 oeffnen. Das geht ueber File -> Reopen with Encoding...

s1 <- "Für 1 Knusperbrötchen habe ich 10,99€ gezahlt"
s2 <- "Für 12 Knusperbrötchen habe ich 1.99$ gezahlt"
s3 <- "Für 123 Knusperbrötchen habe ich 1.99 gezahlt"

print(str_extract_all(s1, " [0-9]+ "))
print(str_extract_all(s2, " [0-9]+ "))
print(str_extract_all(s3, " [0-9]+ "))

print(str_extract_all(s1, " [0-9]+[\\.,][0-9]{2}[€$]? "))
print(str_extract_all(s2, " [0-9]+[\\.,][0-9]{2}[€$]? "))
print(str_extract_all(s3, " [0-9]+[\\.,][0-9]{2}[€$]? "))