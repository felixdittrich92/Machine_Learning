import matplotlib.pyplot as plt

salaries = [40000, 40000, 41000, 50000, 55000, 70000, 90000]
plt.hist(salaries) # ,bins = 50 für große Daten
plt.show()