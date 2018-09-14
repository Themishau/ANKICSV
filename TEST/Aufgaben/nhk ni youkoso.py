# -*- coding: utf-8 -*-

import nltk
from nltk.tokenize import RegexpTokenizer
import collections

with open('stoker_dracula.txt', 'r') as text:
    # zeilenweise einlesen, jedes Listenelement ist ein Datensatz
     text = text.read()
# Aufgabe 1 http://stackoverflow.com/questions/3594514/how-to-find-most-common-elements-of-a-list
tokenizer = RegexpTokenizer(r'\w+') # RE als Muster angeben
words = tokenizer.tokenize(text)
frequency_distribution_words = nltk.FreqDist(words)

# Aufgabe 2
stopwords = nltk.corpus.stopwords.words("english")
words_re= [w for w in words_re if w.lower() not in stopwords]

counter_words = collections.Counter(words_re)
print counter_words.most_common(20)

counter words_top_20 = [word for 
# Aufgabe 3




# Aufgabe 4
tokenizer = RegexpTokenizer(r'\w+') # RE als Muster angeben
words = tokenizer.tokenize(text)
text = nltk.Text(words)
dispersion_words = ["Dracula", "blood", "bat", "Lucy", "Seward", "Transylvania"]
text.dispersion_plot(dispersion_words)
