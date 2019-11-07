import nltk
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet

sentences = nltk.sent_tokenize("He went into a supermarket in St. Petersburg. There, he bought a product for 9.99$. He knew it better")
print(sentences)

for sentence in sentences:
    word = nltk.word_tokenize(sentence)
    print(word)

# Part of Speech Tagging   // ist Wort :Verb, Nom, Adjekiv,.... (siehe Doku für IN, PRP, ..)
for sentence in sentences:
    tagged_words = nltk.pos_tag(nltk.word_tokenize(sentence), lang="eng")
    #print(tagged_words)

    final_sentence = []
    for tagged_word in tagged_words:
        final_sentence.append(tagged_word[0] + "/" + tagged_word[1])
    
    print(" ".join(final_sentence))

# Stemming (Wortendungen entfernen)
s = SnowballStemmer("english") # auch für deutsch z.B.: Autohäuser - autohaus
print(s.stem("cars")) # Wortstamm ausgeben

# Lemmatizer (Wortendungen entfernen)
l = WordNetLemmatizer()
print(l.lemmatize("going", "v")) # v- Verb (wordnet.VERB)

def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

words_tagged = nltk.pos_tag(nltk.word_tokenize("He's going to the supermarket"))
for word in words_tagged:
    l.lemmatize(word[0], get_wordnet_pos(word[1]))
