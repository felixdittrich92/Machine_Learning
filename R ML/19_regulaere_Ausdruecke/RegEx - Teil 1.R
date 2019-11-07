# install.packages("stringr")
library(stringr)

# Hinweis: Sollten bei dir die Umlaute nicht korrekt angezeigt werden, so musst du 
#          die Datei als UTF-8 oeffnen. Das geht ueber File -> Reopen with Encoding...

s <- "Für 7 Knusperbrötchen habe ich 1.99€ gezahlt"
s2 <- "Für 7 Knusperbrötchen habe ich 1.99$ gezahlt"
# print(substring(s, 5, 6))

print(str_extract_all(s, " [1234567890] "))
print(str_extract_all(s, " [0-9] "))
print(str_extract_all(s, "[0-9]\\.[0-9][0-9][€$]"))
print(str_extract_all(s2, "[0-9]\\.[0-9][0-9][€$]"))