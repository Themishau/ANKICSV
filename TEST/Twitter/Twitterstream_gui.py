# -*- coding: utf-8 -*-

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import numpy as np
from tkinter import *
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
import re
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import csv
import nltk
from nltk.tokenize import RegexpTokenizer
import collections
from collections import Counter
import codecs
import itertools
import sys
import json
import time
from streaming import *
from Twittertimeline import *


from twitter_keys import consumer_key, consumer_secret, access_token, access_token_secret


class MenuStreaming(object):
    def __init__(self):

        self.streamF = tk.Tk()
        self.streamF.geometry("300x300") # Groesse des Fensters kann nicht veraendert werden
        self.streamF.title("MasterMenue")
        #Programmliste
        Programm1 = "Twitterstream"
        Programm2 = "Twitteranalyse"
        self.mastermenu = [Programm1, Programm2]# Verwaltung der Programm-Instanzen
        self.programmliste = Listbox(self.streamF)
        for programm in self.mastermenu:
            self.programmliste.insert(END, programm)
        self.programmliste.grid(row=0, column=0, columnspan=4)
        self.programmliste_scrollbar = Scrollbar(self.programmliste, orient=VERTICAL)
        self.programmliste.config(yscrollcommand=self.programmliste_scrollbar.set)
        self.programmliste_scrollbar.config(command=self.programmliste.yview)

        self.starten_button = Button(self.streamF, text='Ausfuehren', command=self.programmausfuehren)
        self.starten_button.grid(row=2, column=0)

        self.streamF.mainloop()

    def programmausfuehren(self):    
        if not self.programmliste.curselection():
            showerror('Fehler', 'Es wurde kein Programm ausgewaehlt!')
        else:
            auswahl1 = self.programmliste.curselection()
            self.gewaehltes_programm = self.programmliste.get(auswahl1)
            print (self.gewaehltes_programm)
            if self.gewaehltes_programm == "Twitterstream":
                print ("lol" , self.gewaehltes_programm)
                self.TwitterStream()    
            if self.gewaehltes_programm == "Twitteranalyse":
                print ("lol" , self.gewaehltes_programm)
                self.TwitterAnalyse()

        
# --------------------Program 1 ------------------       
    def TwitterStream(self):
        self.programmausfuehren_fenster_stream = tk.Toplevel(self.streamF)
        self.programmausfuehren_fenster_stream.geometry("600x400")
        self.programmausfuehren_fenster_stream.title('TwitterStream')
        auswahl_anzeigen_stream = tk.Text(master=self.programmausfuehren_fenster_stream, height=15, width=30)
        auswahl_anzeigen_stream.grid(column=0, row=0, columnspan=1)
        auswahl_anzeigen_stream.insert(tk.END, "Programmauswahl: " + "\n"+ self.gewaehltes_programm + "\n" + "---------------" + "\n" + "Erfolgreich gestartet")
        self.label1_stream = tk.Label(master=self.programmausfuehren_fenster_stream, text="Hashtag eingeben pls: ")
        self.label1_stream.grid(column=0, row=1, columnspan=1)
        self.label2_stream = tk.Label(master=self.programmausfuehren_fenster_stream, text="Dateiname zum speichern eingeben pls: ")
        self.label2_stream.grid(column=0, row=2, columnspan=1)
        self.entry_stream = tk.Entry(master=self.programmausfuehren_fenster_stream)
        self.entry_stream.grid(column=1, row=1, columnspan=1)
        self.entry_name = tk.Entry(master=self.programmausfuehren_fenster_stream)
        self.entry_name.grid(column=1, row=2, columnspan=1)
        self.entry_stream_bt = Button(self.programmausfuehren_fenster_stream, text='Stream starten!', command=self.Twitterstream_ausfuehren)
        self.entry_stream_bt.grid(column=2, row=3, columnspan=2)

    def Twitterstream_ausfuehren(self):
        twittername = str(self.entry_stream.get())
        dateinametwitter = str(self.entry_name.get())
        return startdamit1(twittername, dateinametwitter)
        
        

       
# --------------------Program 2 ------------------  
  
    def TwitterAnalyse(self):
        self.programmausfuehren_fenster_stream = tk.Toplevel(self.streamF)
        self.programmausfuehren_fenster_stream.geometry("600x400")
        self.programmausfuehren_fenster_stream.title('TwitterAnalyse')
        auswahl_anzeigen_stream = tk.Text(master=self.programmausfuehren_fenster_stream, height=15, width=30)
        auswahl_anzeigen_stream.grid(column=0, row=0, columnspan=1)
        auswahl_anzeigen_stream.insert(tk.END, "Programmauswahl: " + "\n"+ self.gewaehltes_programm + "\n" + "---------------" + "\n" + "Erfolgreich gestartet")
        self.label1_stream = tk.Label(master=self.programmausfuehren_fenster_stream, text="Twitternutzername eingeben: ")
        self.label1_stream.grid(column=0, row=1, columnspan=1)
        self.label2_stream = tk.Label(master=self.programmausfuehren_fenster_stream, text="Dateiname zum speichern eingeben pls: ")
        self.label2_stream.grid(column=0, row=2, columnspan=1)
        self.entry_stream = tk.Entry(master=self.programmausfuehren_fenster_stream)
        self.entry_stream.grid(column=1, row=1, columnspan=1)
        self.entry_name = tk.Entry(master=self.programmausfuehren_fenster_stream)
        self.entry_name.grid(column=1, row=2, columnspan=1)
        self.entry_stream_bt = Button(self.programmausfuehren_fenster_stream, text='Stream starten!', command=self.Twitterstream_ausfuehren)
        self.entry_stream_bt.grid(column=2, row=3, columnspan=2)

    def Twitterstream_ausfuehren(self):
        twittername = str(self.entry_stream.get())
        dateinametwitter = str(self.entry_name.get())
        return startdamit(twittername, dateinametwitter)


                
                
"""
            self.programmausfuehren_fenster = Toplevel()
            self.programmausfuehren_fenster.title('Ausfuehren?')
            self.auswahl_anzeigen = tk.Text(master=self.programmausfuehren_fenster, height=10, width=30)
            self.auswahl_anzeigen.grid(column=0, row=0)
            self.auswahl_anzeigen.insert(tk.END, "Programmauswahl: " + self.gewaehltes_programm)
            self.programmausfuehren_fenster_button = Button(self.programmausfuehren_fenster, text='Starten!', command=self.gewaehltes_programfunktion)
            self.programmausfuehren_fenster_button.grid(row=1, column=0, columnspan=2)
"""

if __name__ == '__main__':
    MenuStreaming()



      

  

















"""
            with open('%s_tweets.csv' % dateiname_twitter, "w") as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(["favorited", "text", "created_at","favorite_count","filter_level","lang","retweet_count","retweeted","source","truncated","user_created_at","user_followers_count","user_location","user_lang","user_name","user_screen_name","user_time_zone","user_utc_offset","user_friends_count"])
                for eintrag in alles:
                    writer.writerow([eintrag['favorited'],
                                    eintrag['text'],
                                    eintrag['created_at'],
                                    eintrag['favorite_count'],
                                    eintrag['filter_level'],
                                    eintrag['lang'],
                                    eintrag['retweet_count'],
                                    eintrag['retweeted'],
                                    eintrag['source'],
                                    eintrag['truncated']
                                    ])

            speicherTweet.write(text.encode("utf-8"))
            speicherTweet.write(created_at)
            #speicherTweet.write('/n') , created_at, favorite_count, favorited, filter_level, lang, retweet_count, retweeted, source, truncated, user_created_at, user_followers_count, user_location, user_lang, user_name, user_screen_name, user_time_zone, user_utc_offset, user_friends_count
           
            tweetsfuercsv = [favorited, text.encode("utf-8"), created_at, favorite_count, filter_level, lang, retweet_count, retweeted, source, truncated, user_created_at, user_followers_count, user_location, user_lang, user_name, user_screen_name, user_time_zone, user_utc_offset, user_friends_count]
            speicherTweet = open('%s_tweets.csv' % dateiname_twitter, "a")
            speicherTweet.write(tweetsfuercsv)
            speicherTweet.write('/n')
            speicherTweet.close()

            #nurtweet = data
            daten = alles["text"].encode("utf-8")
            print daten
                            #nurtweet = data.split(',"text":')[1].split('","source')[0] *mit json.loads ist es besser einzelne Twitterdinger zu filtern
            
            speicherTweet = open('%s_tweets.csv' % dateiname_twitter, "a")
            speicherTweet.write(daten)
            speicherTweet.write('/n')
             
            speicherTweet.close()
            
            
                def on_data(self, data):  
        try:
            for eintrag in json.loads(data):
                print json.loads(data)['text'].encode("utf-8")
                speicherTweet = csv.writer(self.speicherTweet, delimiter=";")
                favorited            = json.loads(data)['favorited'].encode("utf-8")
                text                 = json.loads(data)['text'].encode("utf-8")
                print text
                created_at           = json.loads(data)['created_at'].encode("utf-8")
                favorite_count       = json.loads(data)['favorite_count'].encode("utf-8")
                filter_level         = json.loads(data)['filter_level'].encode("utf-8")
                lang                 = json.loads(data)['lang'].encode("utf-8")
                retweet_count        = json.loads(data)['retweet_count'].encode("utf-8")
                retweeted            = json.loads(data)['retweeted'].encode("utf-8")
                source               = json.loads(data)['source'].encode("utf-8")
                truncated            = json.loads(data)['truncated'].encode("utf-8")
                user_created_at      = json.loads(data)['user']['created_at'].encode("utf-8")
                user_followers_count = json.loads(data)['user']['followers_count'].encode("utf-8")
                user_location        = json.loads(data)['user']['location'].encode("utf-8")
                user_lang            = json.loads(data)['user']['lang'].encode("utf-8")
                user_name            = json.loads(data)['user']['name'].encode("utf-8")
                user_screen_name     = json.loads(data)['user']['screen_name'].encode("utf-8")
                user_time_zone       = json.loads(data)['user']['time_zone'].encode("utf-8")
                user_utc_offset      = json.loads(data)['user']['utc_offset'].encode("utf-8")
                user_friends_count   = json.loads(data)['user']['friends_count'].encode("utf-8")
                speicherTweet.writerow([favorited, text, created_at, favorite_count, filter_level, lang, retweet_count, retweeted, source, truncated, user_created_at, user_followers_count, user_location, user_lang, user_name, user_screen_name, user_time_zone, user_utc_offset, user_friends_count])
                speicherTweet.close()
            return True   

        except BaseException, e:
            print "error/exception", e
            time.sleep(3)
    
    def on_error(self, error):
        print status
"""

"""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
stream = Stream(auth = api.auth, listener=derzuhoerer(twittername, dateinametwitter))
stream.filter(track=[twittername]) 
"""

