import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sf_salaries.csv", low_memory=False)
#print(df)
#print(df["TotalPay"] > 100000)
high_paying_jobs = df[df["TotalPay"] > 100000] #df[filtern nach]
print(high_paying_jobs)

year_2011 = df[df["Year"] == 2011]
print(year_2011["TotalPay"].mean())

year_2012 = df[df["Year"] == 2012]
print(year_2012["TotalPay"].mean())

year_2013 = df[df["Year"] == 2013]
print(year_2013["TotalPay"].mean())

year_2014 = df[df["Year"] == 2014]
print(year_2014["TotalPay"].mean())

print(df["TotalPay"].mean())
print(df["TotalPay"].median())

plt.hist(df["TotalPay"], bins = 100)
plt.show()

