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
from twitter_keys import consumer_key, consumer_secret, access_token, access_token_secret

class twitterdaten(object):
    def __init__(self, twittername, dateinametwitter):
        self.twittername = twittername
        self.dateinametwitter = dateinametwitter
    
    def bargraph(reihenfolge, namen, daten, titel): # fuer die schönen Graphen
        fig = plt.figure()
        plt.bar(reihenfolge, daten, align="center")
        plt.xticks(reihenfolge, namen, rotation=45, ha='right')
        plt.title(titel)
        plt.tight_layout()
        plt.show()
 
    def timelinecheck(self, twittername, dateinametwitter):
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth)
            public_tweets = api.home_timeline()
            alletweets = []
            neustentweets = api.user_timeline(twittername, count=200)
            alletweets.extend(neustentweets)


            alletweets = api.user_timeline(twittername, count=200)
            print (alletweets)
            alletweets.extend(neustentweets)

            tweetsfuercsv = [[tweet.favorited, tweet.in_reply_to_user_id, tweet.contributors, tweet.truncated, tweet.text.encode("utf-8"), tweet.created_at, tweet.retweeted, tweet.in_reply_to_status_id, tweet.coordinates, tweet.id, tweet.source, tweet.in_reply_to_status_id_str, tweet.in_reply_to_screen_name, tweet.user, tweet.place, tweet.retweet_count, tweet.geo, tweet.in_reply_to_user_id_str, tweet.id_str] for tweet in alletweets]
            
            with open('%s_tweets.csv' % dateinametwitter, "wb") as csv_file:
                schreiben = csv.writer(csv_file, delimiter=';')
                schreiben.writerow(["favorited", "in_reply_to_user_id", "contributors","truncated","text","created_at","retweeted","in_reply_to_status_id","coordinates","id","source","in_reply_to_status_id_str","in_reply_to_screen_name","user","place","retweet_count","geo","in_reply_to_user_id_str","id_str"])
                schreiben.writerows(tweetsfuercsv)
        except BaseException as e:
            print ("error/exception", e)
            time.sleep(3)


    def timelinecheck1():
        for tweet in public_tweets:
            print (tweet.text.encode('utf8'))
            
def startdamit1(twittername, dateinametwitter):
    twittername = twittername
    dateinametwitter = dateinametwitter
    twitterxd = twitterdaten(twittername, dateinametwitter)
    twitterxd.timelinecheck(twittername, dateinametwitter) #automatisch timeline

if __name__ == '__main__':
    twittername = ("osakajinninaru")
    dateinametwitter = ("ich")
    starten = startdamit1(twittername, dateinametwitter)
