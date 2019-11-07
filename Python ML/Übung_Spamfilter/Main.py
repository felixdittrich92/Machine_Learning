import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("spam.csv")
print(len(df)) # Anzahl SMS

y = df["type"].values
X = df["message"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

cv = CountVectorizer(min_df = 0.01, max_df = 0.1)
cv.fit(X_train)
X_train = cv.transform(X_train)
X_test = cv.transform(X_test)

#cv.fit(pd.Series(["Hallo Welt", "Hallo Mars"])) # pd.Series() holt Spalte aus Dataframe
#cv.transform(pd.Series(["Hallo Welt", "Hallo Mars"]))
# in einem
#cv.fit_transform(pd.Series(["Hallo Welt", "Hallo Mars"])).toarray()

model = MultinomialNB()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))

print(model.predict(X_train))

