# -*- coding: utf-8 -*-

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import numpy as np
from tkinter import *
from tkinter.messagebox import *
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

class derzuhoerer(StreamListener):
    
    def __init__(self, dateinametwitter):

        self.dateinametwitter = dateinametwitter
        print (self.dateinametwitter)
        self.speicherTweet = open('%s_tweets.csv' % self.dateinametwitter, "w")
        self.speicherTweet.write("text; created_at;lang;retweet_count;retweeted;user_created_at;user_followers_count;user_lang;user_name;user_screen_name;user_time_zone" + "/n")
    def on_data(self, data):  
                        try:
                            with open('%s_tweets.csv' % self.dateinametwitter, "a") as csv_file:
                                speicherTweet = csv.writer(csv_file, delimiter=';')
                                text                 = json.loads(data)['text'].encode("utf-8")
                                created_at           = json.loads(data)['created_at'].encode("utf-8")
                                lang                 = json.loads(data)['lang'].encode("utf-8")
                                retweet_count        = json.loads(data)['retweet_count']
                                retweeted            = json.loads(data)['retweeted']
                                user_created_at      = json.loads(data)['user']['created_at'].encode("utf-8")
                                user_followers_count = json.loads(data)['user']['followers_count']                      
                                user_lang            = json.loads(data)['user']['lang'].encode("utf-8")
                                user_name            = json.loads(data)['user']['name'].encode("utf-8")
                                user_screen_name     = json.loads(data)['user']['screen_name'].encode("utf-8")
                                user_time_zone       = json.loads(data)['user']['time_zone']
                                speicherTweet.writerow([text, created_at, lang, retweet_count, retweeted, user_created_at, user_followers_count, user_lang, user_name, user_screen_name, user_time_zone])
                                print (text)
                            return True
                        except BaseException as e:
                            print ("error/exception", e)
                            time.sleep(3)
                
    def on_error(self, error):
        print (status)

def startdamit(twittername, dateinametwitter):
    twittername = twittername
    dateinametwitter = dateinametwitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    stream = Stream(auth = api.auth, listener=derzuhoerer(dateinametwitter)) 
    stream.filter(track=[twittername])   
    
if __name__ == '__main__':
    twittername = ("japan")
    dateinametwitter = ("japan")
    starten = startdamit(twittername, dateinametwitter)


# mit set_twitter_usw.twittername, set_twitter_usw.dateinametwitter funkt hier   




