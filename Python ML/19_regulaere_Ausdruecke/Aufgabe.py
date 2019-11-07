import re
from datetime import datetime

sentences = [
    "Am 05.06.2018 findet ein cooles Event statt",
    "Please follow our invitation and visit us on 2018/14/05",
    "Im Monat 05/2018 ist oft gutes Wetter",
    "Der Lottogewinn war 10.000.000€ groß. Er wurde am 04.06.2018 ausgeschüttet",
    "Im Monat 01/2018 war in Sofia heftiger Smog",
    "Dein Flug in den Urlaub geht am 06.07.2018",
]

re1 = re.compile("[0-9]{2}.[0-9]{2}.[0-9]{4}")
re2 = re.compile("[0-9]{4}/[0-9]{2}/[0-9]{2}")
re3 = re.compile("[0-9]{2}/[0-9]{4}")

for sentence in sentences:
    
    match1 = re1.search(sentence)
    match2 = re2.search(sentence)
    match3 = re3.search(sentence)
    
    if match1: 
        print(match1[0])
    elif match2: 
        print(match2[0])
    elif match3: 
        print(match3[0])
    
print("---------------------andere Lösung----------------------------")

re1 = re.compile("[0-9]{2}.[0-9]{2}.[0-9]{4}")
re2 = re.compile("[0-9]{4}/[0-9]{2}/[0-9]{2}")
re3 = re.compile("[0-9]{2}/[0-9]{4}")

dates = []
for sentence in sentences:
    
    match1 = re1.search(sentence)
    match2 = re2.search(sentence)
    match3 = re3.search(sentence)
    
    if match1: 
        dates.append(datetime.strptime(match1[0], "%d.%m.%Y"))
    elif match2: 
        dates.append(datetime.strptime(match2[0], "%Y/%d/%m"))
    elif match3: 
        dates.append(datetime.strptime(match3[0], "%m/%Y"))
        
for d in dates:
    print(d.strftime("%d.%m.%Y"))