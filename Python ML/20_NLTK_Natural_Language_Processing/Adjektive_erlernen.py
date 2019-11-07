import pandas as pd
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

df = pd.read_csv("Reviews_10000.csv.bz2")
texts = df["Text"]

texts_transformed = []
for review in texts:
    sentences = nltk.sent_tokenize(review)
    adjectives = []

    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words_tagged = nltk.pos_tag(words)

        for word_tagged in words_tagged:
            if word_tagged[1] == "JJ":
                adjectives.append(word_tagged[0])

    texts_transformed.append(" ".join(adjectives))

y = df["Score"] >= 4
X = texts_transformed

X_train, X_test, y_train, y_test = train_test_split(X, y)

cv = CountVectorizer(max_features = 50)

X_train = cv.fit_transform(X_train)
X_test = cv.fit_transform(X_test)

model = MultinomialNB()
model.fit(X_train, y_train)

print(model.score(X_test, y_test))

adj = list(zip(model.coef_[0], cv.get_feature_names()))
adj = sorted(adj)

for i in adj:
    print(i)
