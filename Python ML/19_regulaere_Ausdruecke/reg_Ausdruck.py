import re

p = re.compile("[0-9]") # Gruppe Zahlen 

print(p.findall("Für 5 Knusperbrötchen habe ich 1.99€ bezahlt"))
print("---------------------------------------------")

p = re.compile(" [0-9] ") # Gruppe Zahlen mit Leerzeichen

print(p.findall("Für 5 Knusperbrötchen habe ich 1.99€ bezahlt"))
print("---------------------------------------------")

p = re.compile("[0-9].[0-9][0-9]€") # zusammenhängende Teile

print(p.findall("Für 5 Knusperbrötchen habe ich 1.99€ bezahlt"))
print("---------------------------------------------")

p = re.compile("[0-9].[0-9][0-9][€$]") 

print(p.findall("Für 5 Knusperbrötchen habe ich 1.99$ bezahlt"))
print("---------------------------------------------")

p = re.compile("[0-9]+") # größere Zahlen

print(p.findall("Für 1 Knusperbrötchen habe ich 1.99€ bezahlt"))
print(p.findall("Für 12 Knusperbrötchen habe ich 1.99$ bezahlt"))
print(p.findall("Für 123 Knusperbrötchen habe ich 10.99€ bezahlt"))
print("---------------------------------------------")

p = re.compile("[0-9]+[.][0-9]{2}[$€]?") # entweder € oder $

print(p.findall("Für 1 Knusperbrötchen habe ich 1.99€ bezahlt"))
print(p.findall("Für 12 Knusperbrötchen habe ich 1.99$ bezahlt"))
print(p.findall("Für 123 Knusperbrötchen habe ich 10.99€ bezahlt"))
print("---------------------------------------------")

p = re.compile("[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+") 

sentences = [
    "Meine E-Mail-Adresse ist hallo@codingcourses.tv",
    "Bitte keine E-Mails an info@codingcourses.tv senden",
    "Saturday@ Hotel XYZ findet ein Event statt. Zur Teilnahme kannst du eine E-Mail an veranstaltung@codingcourses.tv senden"
]

for sentence in sentences:
    match = p.search(sentence)
    if match:
        print(match[0]) # alle gefundenen