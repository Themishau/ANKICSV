# -*- coding: utf-8 -*-

import numpy as np
from Tkinter import *
from tkMessageBox import *
import re
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import csv
import nltk
from nltk.tokenize import RegexpTokenizer
import collections
from collections import Counter
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
root = Tk()
root.title("Larrystatistik")

def bargraph(reihenfolge, namen, daten, titel): # fuer die schönen Graphen
    fig = plt.figure()
    plt.bar(reihenfolge, daten, align="center")
    plt.xticks(reihenfolge, namen, rotation=45, ha='right')
    plt.title(titel)
    plt.tight_layout()
    plt.show()
    
def aehnlichkeit_aller_begriffe_esa_nasa(): # aehnlichkeit der woerter, hashtags, @ in den tweets beider accounts
    aehnlichkeit_nasa_esa = []
    worte_nasa = []
    worte_esa = []
    affen_esa_nasa = []
    affen_nasa = []
    affen_esa = []
    hashtag_esa_nasa = []
    hashtag_nasa = []
    hashtag_esa =[]
    
    stopwords = nltk.corpus.stopwords.words("english")
    with codecs.open("esa.csv", "r", "utf-8") as csv_input:
        esa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte2 in esa_reader:
            for kotoba2 in spalte2[4].split():
                if not kotoba2 in stopwords: 
                    worte_esa.append(kotoba2)
                if "@" in kotoba2:
                    affen_esa.append(kotoba2)
                if "#" in kotoba2:
                    hashtag_esa.append(kotoba2)
                                                             
    with codecs.open("nasa.csv", "r", "utf-8") as csv_input:
        nasa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte in nasa_reader:
            for kotoba in spalte[4].split():
                if not kotoba in stopwords:
                    worte_nasa.append(kotoba)
                if "@" in kotoba:
                    affen_nasa.append(kotoba)
                if "#" in kotoba:
                    hashtag_nasa.append(kotoba)

    for word in worte_nasa:
        if word in worte_esa:

            aehnlichkeit_nasa_esa.append(word)

    for affe in affen_nasa:
        if affe in affen_esa:

            affen_esa_nasa.append(word)

    for hashtag in hashtag_nasa:
        if hashtag in hashtag_esa:

            hashtag_esa_nasa.append(word)
            
    jaccard_sneath = float(len(aehnlichkeit_nasa_esa)) / (float(len(worte_nasa)) + float(len(worte_esa))- float(len(aehnlichkeit_nasa_esa)))
    jaccard_sneath_affe = float(len(affen_esa_nasa)) /  (float(len(affen_nasa)) + float(len(affen_esa))- float(len(affen_esa_nasa)))
    jaccard_sneath_hashtag = float(len(hashtag_esa_nasa)) /  (float(len(hashtag_esa)) + float(len(hashtag_nasa))- float(len(hashtag_esa_nasa)))
    
    text2.insert(END,"Die Anzahl der gleichen Worte in den beiden Twitter-Kanälen ist: ")
    text2.insert(END, len(aehnlichkeit_nasa_esa))
    text2.insert(END,". Die insgesamte Ähnlichkeit zwischen allen Worten ist: ")
    text2.insert(END, jaccard_sneath )
    
    text2.insert(END,". ----- Die Anzahl der gleichen Worte mit @ in den beiden Twitter-Kanälen ist: ")
    text2.insert(END, len(affen_esa_nasa))
    text2.insert(END,". Die insgesamte Ähnlichkeiten aller Worte mit @ ist: ")
    text2.insert(END,jaccard_sneath_affe )
    
    text2.insert(END,". ----- Die Anzahl der gleichen Worte in den beiden Twitter-Kanälen mit Hashtags ist: ")
    text2.insert(END, len(hashtag_esa))
    text2.insert(END,". Die insgesamte Ähnlichkeiten aller Worte mit Hashtags ist: ")
    text2.insert(END,jaccard_sneath_hashtag )
    
    
def worte_ranking_esa():
    wort2 = []
    with codecs.open("esa.csv", "r", "utf-8") as csv_input:
        esa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        stopwords = nltk.corpus.stopwords.words("english")
        for spalte2 in esa_reader:
            for kotoba2 in spalte2[4].split():
                if not kotoba2 in stopwords: # ranking alle wörter

                    wort2.append(kotoba2) 
    counts2 = Counter(wort2)
    
    
    
    text2.insert(END, counts2.most_common(25))
    counts2_als_dict = dict(counts2.most_common(25))
    
    woerter = counts2_als_dict.keys()
    haeufigkeit_woerter = counts2_als_dict.values()
    x_graph = range(1,26)
    titel = u"häufigsten Wörter bei ESA"
    

    bargraph(x_graph, woerter, haeufigkeit_woerter, titel)

def affe_ranking_esa():
    wort_mitaffe2 = []
    with codecs.open("esa.csv", "r", "utf-8") as csv_input:
        esa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte2 in esa_reader:
            for kotoba2 in spalte2[4].split():               
                if "@" in kotoba2:
                    wort_mitaffe2.append(kotoba2) # ranking aller begriffe mit @
    counts_affe2 = Counter(wort_mitaffe2)
    text2.insert(END, counts_affe2.most_common(25))
    
    counts_affe2_dict = dict(counts_affe2.most_common(25))
    
    woerter = counts_affe2_dict.keys()
    haeufigkeit_woerter = counts_affe2_dict.values()
    x_graph = range(1,26)
    titel = u"häufigsten Wörter mit @ bei ESA"
    
    
    bargraph(x_graph, woerter, haeufigkeit_woerter, titel)
           
                
def hashtag_ranking_esa():
    wort_mithashtag2 = []
    with codecs.open("esa.csv", "r", "utf-8") as csv_input:
        esa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte2 in esa_reader:
            for kotoba2 in spalte2[4].split():               
                if "#" in kotoba2:
                    wort_mithashtag2.append(kotoba2) # ranking von begriffen mit hashtag 
    counts_hashtag2 = Counter(wort_mithashtag2)
    text2.insert(END, counts_hashtag2.most_common(25))  
    
    counts_hashtag2_dict = dict(counts_hashtag2.most_common(25))
    
    woerter = counts_hashtag2_dict.keys()
    haeufigkeit_woerter = counts_hashtag2_dict.values()
    x_graph = range(1,26)
    titel = u"häufigsten Wörter mit # bei ESA"
    
    
    bargraph(x_graph, woerter, haeufigkeit_woerter, titel)
                
def datum_ranking_esa():
    datum_t2 = []
    datum_und_tweet2 = []
    with codecs.open("esa.csv", "r", "utf-8") as csv_input:
        esa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte2 in esa_reader:            
            for datum2 in spalte2[5].split():
                if "-" in datum2:
                    datum_t2.append(datum2) #ranking datum
                # mit tweet ?   
    counts_datum2 = Counter(datum_t2)
    text2.insert(END, counts_datum2.most_common(25))      
    
    counts_datum2_dict = dict(counts_datum2.most_common(25))
    
    woerter = counts_datum2_dict.keys()
    haeufigkeit_woerter = counts_datum2_dict.values()
    x_graph = range(1,26)
    titel = u"häufigste Tweets nach Datum bei ESA"
    
    
    bargraph(x_graph, woerter, haeufigkeit_woerter, titel)
    
    
         
def worte_ranking_nasa():
    stopwords = nltk.corpus.stopwords.words("english")
    wort = []
    with codecs.open("nasa.csv", "r", "utf-8") as csv_input:
        nasa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte in nasa_reader:
            for kotoba in spalte[4].split():
                if not kotoba in stopwords: # ranking alle wörter
                    wort.append(kotoba) 
    counts = Counter(wort)
    text2.insert(END, counts.most_common(25))
    
    counts_als_dict = dict(counts.most_common(25))
    
    woerter = counts_als_dict.keys()
    haeufigkeit_woerter = counts_als_dict.values()
    x_graph = range(1,26)
    titel = u"häufigsten Wörter bei NASA"
    

    bargraph(x_graph, woerter, haeufigkeit_woerter, titel)
    
def affe_ranking_nasa():
    wort_mitaffe = []
    with codecs.open("nasa.csv", "r", "utf-8") as csv_input:
        nasa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte in nasa_reader:
            for kotoba in spalte[4].split():              
                if "@" in kotoba:
                    wort_mitaffe.append(kotoba) # ranking aller begriffe mit @
    counts_affe = Counter(wort_mitaffe)
    text2.insert(END, counts_affe.most_common(25))   
    
    counts_affe_dict = dict(counts_affe.most_common(25))
    
    woerter = counts_affe_dict.keys()
    haeufigkeit_woerter = counts_affe_dict.values()
    x_graph = range(1,26)
    titel = u"häufigsten Wörter mit @ bei NASA"
    
    
    bargraph(x_graph, woerter, haeufigkeit_woerter, titel)
           
def hashtag_ranking_nasa():
    wort_mithashtag = []
    with codecs.open("nasa.csv", "r", "utf-8") as csv_input:
        nasa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte in nasa_reader:
            for kotoba in spalte[4].split():               
                if "#" in kotoba:
                    wort_mithashtag.append(kotoba) # ranking von begriffen mit hashtag 
    counts_hashtag = Counter(wort_mithashtag)
    text2.insert(END, counts_hashtag.most_common(25))
    
    
    counts_hashtag_dict = dict(counts_hashtag.most_common(25))
    
    woerter = counts_hashtag_dict.keys()
    haeufigkeit_woerter = counts_hashtag_dict.values()
    x_graph = range(1,26)
    titel = u"häufigsten Wörter mit # bei NASA"
    
    
    bargraph(x_graph, woerter, haeufigkeit_woerter, titel)
           
    
    
                 
def datum_ranking_nasa():
    datum_t = []
    datum_und_tweet = []
    with codecs.open("nasa.csv", "r", "utf-8") as csv_input:
        nasa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte in nasa_reader:
            for datum in spalte[5].split():
                if "-" in datum:
                    datum_t.append(datum) #ranking datum               
                                
    counts_datum = Counter(datum_t)
    text2.insert(END, counts_datum.most_common(25))
    
    
    counts_datum_dict = dict(counts_datum.most_common(25))
    
    woerter = counts_datum_dict.keys()
    haeufigkeit_woerter = counts_datum_dict.values()
    x_graph = range(1,26)
    titel = u"meisten Tweets mit Datum bei NASA"
    
    
    bargraph(x_graph, woerter, haeufigkeit_woerter, titel)
           
def datum_tweets_ranking_nasa():

    datum_und_tweet = []
    with codecs.open("nasa.csv", "r", "utf-8") as csv_input:
        nasa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte in nasa_reader:
            if "2015-09-28" in spalte[5]:
                    datum_und_tweet.append(spalte[4]) # mit tweet               
                                
    
    text2.insert(END, datum_und_tweet)

def datum_tweets_ranking_esa():

    datum_und_tweet = []
    with codecs.open("esa.csv", "r", "utf-8") as csv_input:
        esa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte in esa_reader:
            if "2015-12-15" in spalte[5]:
                    datum_und_tweet.append(spalte[4]) # mit tweet               
                                
    
    text2.insert(END, datum_und_tweet)

def aehnlichkeiten_haeufigste_begriffe_nasa_esa(): 
    stopwords = nltk.corpus.stopwords.words("english")
    wort2 = []
    with codecs.open("esa.csv", "r", "utf-8") as csv_input:
        esa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        stopwords = nltk.corpus.stopwords.words("english")
        for spalte2 in esa_reader:
            for kotoba2 in spalte2[4].split():
                if not kotoba2 in stopwords: # ranking alle wörter
                    wort2.append(kotoba2) 
    
        
    wort = []
    
    with codecs.open("nasa.csv", "r", "utf-8") as csv_input:
        nasa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte in nasa_reader:
            for kotoba in spalte[4].split():
                if not kotoba in stopwords: # ranking alle wörter
                    wort.append(kotoba) 
    
    beide = []
    
    for word in wort:
        if word in wort2:
            beide.append(word)
    
    for word in wort2: 
        if word in wort: 
            beide.append(word)
    
    counts = Counter(beide)
    
    counts_ad = dict(counts.most_common(25)) # ad als Abkürzung für "als Dictionary"
    
    
    
    text2.insert(END, counts.most_common(25))
    
    
    
    woerter = counts_ad.keys()
    haeufigkeit_woerter = counts_ad.values()
    x_graph = range(1,26)
    titel = u"häufigsten Wörter, die bei NASA und ESA gleich sind"
    

    bargraph(x_graph, woerter, haeufigkeit_woerter, titel)
    

def aehnlichkeiten_haeufigste_affe_nasa_esa():    
    wort_mitaffe = []
    with codecs.open("nasa.csv", "r", "utf-8") as csv_input:
        nasa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte in nasa_reader:
            for kotoba in spalte[4].split():              
                if "@" in kotoba:
                    wort_mitaffe.append(kotoba) # ranking aller begriffe mit @
    
    
    wort_mitaffe2 = []
    with codecs.open("esa.csv", "r", "utf-8") as csv_input:
        esa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte2 in esa_reader:
            for kotoba2 in spalte2[4].split():               
                if "@" in kotoba2:
                    wort_mitaffe2.append(kotoba2) # ranking aller begriffe mit @
    
    
    beide = []
    
    for word in wort_mitaffe:
        if word in wort_mitaffe2:
            beide.append(word)
    
    for word in wort_mitaffe2: 
        if word in wort_mitaffe: 
            beide.append(word)
    
    counts = Counter(beide)
    
    counts_ad = dict(counts.most_common(25)) # ad als Abkürzung für "als Dictionary"
    
    
    
    text2.insert(END, counts.most_common(25))
    
    woerter = counts_ad.keys()
    haeufigkeit_woerter = counts_ad.values()
    x_graph = range(1,26)
    titel = u"häufigsten Wörter mit @ bei NASA und ESA zusammen"
    

    bargraph(x_graph, woerter, haeufigkeit_woerter, titel)
    

def aehnlichkeiten_hashtags():
    wort_mithashtag2 = []
    with codecs.open("esa.csv", "r", "utf-8") as csv_input:
        esa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte2 in esa_reader:
            for kotoba2 in spalte2[4].split():               
                if "#" in kotoba2:
                    wort_mithashtag2.append(kotoba2) # ranking von begriffen mit hashta
    
    wort_mithashtag = []
    with codecs.open("nasa.csv", "r", "utf-8") as csv_input:
        nasa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte in nasa_reader:
            for kotoba in spalte[4].split():               
                if "#" in kotoba:
                    wort_mithashtag.append(kotoba) # ranking von begriffen mit hashtag    

    beide = []
    for word in wort_mithashtag:
        if word in wort_mithashtag2:
            beide.append(word)    
    
    for word in wort_mithashtag2: 
        if word in wort_mithashtag: 
            beide.append(word)
    
    counts = Counter(beide)
    
    counts_ad = dict(counts.most_common(25)) # ad als Abkürzung für "als Dictionary"
    
    
    
    text2.insert(END, counts.most_common(25))
    
    woerter = counts_ad.keys()
    haeufigkeit_woerter = counts_ad.values()
    x_graph = range(1,26)
    titel = u"häufigsten Wörter mit # bei ESA und NASA zusammen"
    

    bargraph(x_graph, woerter, haeufigkeit_woerter, titel)

def aehnlichkeiten_datum():
    datum_t = []
    datum_und_tweet = []
    with codecs.open("nasa.csv", "r", "utf-8") as csv_input:
        nasa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte in nasa_reader:
            for datum in spalte[5].split():
                if "-" in datum:
                    datum_t.append(datum) #ranking datum 
    
    datum_t2 = []
    datum_und_tweet2 = []
    with codecs.open("esa.csv", "r", "utf-8") as csv_input:
        esa_reader = csv.reader(csv_input, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL)
        for spalte2 in esa_reader:            
            for datum2 in spalte2[5].split():
                if "-" in datum2:
                    datum_t2.append(datum2)
                    
    
    beide = []
    for word in datum_t2:
        if word in datum_t:
            beide.append(word)    
    
    for word in datum_t: 
        if word in datum_t2: 
            beide.append(word)
    
    counts = Counter(beide)
    
    counts_ad = dict(counts.most_common(25)) # ad als Abkürzung für "als Dictionary"
    
    
    
    text2.insert(END, counts.most_common(25))
    
    woerter = counts_ad.keys()
    haeufigkeit_woerter = counts_ad.values()
    x_graph = range(1,26)
    titel = u"häufigst getweete Tage, bei ESA und NASA zusammen"
    

    bargraph(x_graph, woerter, haeufigkeit_woerter, titel)
    
scrollbar = Scrollbar(root)
text2 = Text(root, height=30, width=50)
 
scrollbar.pack(side=RIGHT, fill=Y)
text2.pack(side=LEFT, fill=Y)
 
scrollbar.config(command=text2.yview)
text2.config(yscrollcommand=scrollbar.set)

text2.insert(END, "")


Button(root, text='Ranking alle Wörter bei NASA', command=worte_ranking_nasa).pack()
Button(root, text='Ranking aller Begriffe mit @ bei NASA', command=affe_ranking_nasa).pack()
Button(root, text='Ranking aller Begriffen mit # bei NASA', command=hashtag_ranking_nasa).pack()
Button(root, text='Ranking beim Datum bei NASA', command=datum_ranking_nasa).pack()
Button(root, text='Ranking aller Wörter bei ESA', command=worte_ranking_esa).pack()
Button(root, text='Ranking aller Begriffe mit @ bei ESA', command=affe_ranking_esa).pack()
Button(root, text='Ranking von begriffen mit hashtag bei ESA', command=hashtag_ranking_esa).pack()
Button(root, text='Ranking Datum bei ESA', command=datum_ranking_esa).pack()
Button(root, text='Ranking Datum bei NASA mit Tweet', command=datum_tweets_ranking_nasa).pack()
Button(root, text='Ranking Datum bei ESA mit Tweet', command=datum_tweets_ranking_esa).pack()
Button(root, text='Aehnlichkeit beim Inhalt ESA und NASA', command=aehnlichkeit_aller_begriffe_esa_nasa).pack()
Button(root, text='Aehnlichkeit häufigste Begriffe ESA und NASA', command=aehnlichkeiten_haeufigste_begriffe_nasa_esa).pack()
Button(root, text='Aehnlichkeit häufigste Begriffe ESA und NASA mit @', command=aehnlichkeiten_haeufigste_affe_nasa_esa).pack()
Button(root, text='Aehnlichkeit häufigste Begriffe ESA und NASA mit #', command=aehnlichkeiten_hashtags).pack()
Button(root, text='Aehnlichkeit beim Datum bei ESA und NASA', command=aehnlichkeiten_datum).pack()
Button(root, text='Quit', command=quit).pack()


# Datum nasa und esa            
"""
2015-09-28

2015-12-15

"""
        


# Versuche und Referenzen unten

"""         
fd = nltk.FreqDist(wort_re)
print sorted(dict(fd).items(), key=lambda x:x[1], reverse=True)[:5]

        stopwords = nltk.corpus.stopwords.words("english")
        words_re = [w for w in wort if w.lower() not in stopwords]
"""            


         
"""  
stopwords = nltk.corpus.stopwords.words("english")
words_re = [w for w in words_re if w.lower() not in stopwords]

counter_words = collections.Counter(wort)
print counter_words.most_common(20)
                word_pattern = RegexpTokenizer(r'\w+')
                words_re = word_pattern.tokenize(line[4])
                
                tokenizer = RegexpTokenizer(r'\w+') # RE als Muster angeben
            words = tokenizer.tokenize(line[4])
            frequency_distribution_words = nltk.FreqDist(words)
"""   

#Versuch mit Dict zu arbeiten - zu umständlich // "import panda" scheint eine gute Methode zu sein, aber funktioniert nicht wie gewollt.


"""
def worte_ranking_esa_bargraph(): 
	y_graph = range(1,100)
	woerter = 
	haeufigkeit_woerter = 
	titel = u"häufigsten Wörter bei ESA"
	bargraph (y_graph, woerter, haeufigkeit_woerter, titel)

# speichern und die abbildungen/statistik hinzufügen

def speichern():
def abbildungen():
"""
   
"""
for hangman_word in spielergebnisse:
    hwortdict = {}
    hwortdict['Wort'] = hangman_word[0]
    wort.append(hwortdict)

for hangman_word in spielergebnisse:
    hwortdict = {}
    hwortdict['Geraten'] = hangman_word[2]
    geraten.append(hwortdict)
"""

"""
# Darstellung der Daten in einem Diagramm 
fig = plt.figure()
plt.bar(reihenfolge, geraten_int, align="center")
plt.xticks(reihenfolge, wort, rotation=45, ha='right')
plt.title(u'geratene Woerter')
plt.tight_layout()
plt.show()
"""

"""

stopwords = nltk.corpus.stopwords.words("english")
words_re= [w for w in words_re if w.lower() not in stopwords]

counter_words = collections.Counter(words_re)
print counter_words.most_common(20)

-----------------------------------------------------------------------------------------

tokenizer = RegexpTokenizer(r'\w+') # RE als Muster angeben
words = tokenizer.tokenize(text)
text = nltk.Text(words)
dispersion_words = ["Dracula", "blood", "bat", "Lucy", "Seward", "Transylvania"]
text.dispersion_plot(dispersion_words)


word_pattern = RegexpTokenizer(r'\w+')
words_re = word_pattern.tokenize(content_dracula)

top_5_words = Counter(words_re).most_common(5)
print top_5_words

# Alternativ: Erstellung des Haeufigkeitsverteilung
# Sortierung nach Werte-Seite und Ausgabe der ersten fuenf Elemente
fd = nltk.FreqDist(words_re)
print sorted(dict(fd).items(), key=lambda x:x[1], reverse=True)[:5]

---------------------------------------------------------------------------------------------
# Aufgabe 02

counter_words = Counter(words_re)
counter_words_top_20 = [word for word, value in counter_words.most_common(20)]
print "third most common word is \'{}\' and occurs {} times in the text 'dracula'".format(counter_words_top_20[2], counter_words[counter_words_top_20[2]])

words_top_20 = [word for word in words_re if word in counter_words_top_20]
top_20 = nltk.FreqDist(words_top_20)
top_20.plot()

words_top_20_string = " ".join(counter_words_top_20)
words_top_20_tokenized = word_pattern.tokenize(words_top_20_string)

print words_top_20_string

"""
"""        
# alle str in Zahlen umwandeln
del wort[0]       
del geraten[0]
for zahl in geraten:
    geraten_int.append(int(float(zahl)))
"""        
root.mainloop()
