import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("cancer.csv")
print(df)
df = df.drop("id", axis = 1)

X = df.drop("diagnosis", axis = 1).values
y = df["diagnosis"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0, test_size = 0.25)

model = LogisticRegression()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))
