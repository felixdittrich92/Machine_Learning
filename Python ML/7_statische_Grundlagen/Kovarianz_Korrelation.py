# Kovarianz: Die Kovarianz (selten Mitstreuung) ist in der Stochastik 
# ein nichtstandardisiertes Zusammenhangsmaß für einen monotonen Zusammenhang 
# zweier Zufallsvariablen mit gemeinsamer Wahrscheinlichkeitsverteilung.

# Korrelation: Eine Korrelation beschreibt eine Beziehung zwischen zwei oder mehreren Merkmalen, 
# Ereignissen, Zuständen oder Funktionen. 
# Die Beziehung muss keine kausale Beziehung sein: 
# manche Elemente eines Systems beeinflussen sich gegenseitig nicht, 
# oder es besteht eine stochastische, also vom Zufall beeinflusste Beziehung zwischen ihnen.
# 1 beeinflussen sich positiv 0 beeinflussen sich nicht -1 beeinflussen sich negativ

import pandas as pd
import numpy as np

df = pd.read_csv("classification.csv")
df["extra"] = np.random.normal(5, 16, len(df))

print(df.cov())
print(df.corr())

print("-------------------------------------")
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 1, 0, 0, 0, 1, 1]

print(np.cov(x, y))  # x und x / x und y / y und x / y und y

print(np.corrcoef(x, y)) # Beeinflussung: positiv / negativ / negativ / positiv