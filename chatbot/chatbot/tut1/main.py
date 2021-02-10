import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json

data = json.load(open('intents.json'))

words = []
labels = []
docs_x = []
docs_y = []

for intent in data['intents']:
    for pattern in intent['pattern']:
        wrds = nltk.word_tokenize(pattern)
        words.extend(wrds)
        docs_x.append(pattern)
        docs_y.append(intent['tag'])

    labels.append(intent['tag'])

words = [stemmer.stem(w.lower()) for w in words]
words = sorted(list(set(words)))

labels = sorted(labels)



print(data)