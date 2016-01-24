#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, json, time
from twython import Twython


# my interface
from tweetlist import get_all_tweets, clean, makeMarkovChain
    # use get_all_tweets() to update our list of jaden's tweets
    # use clean() to make our list even better

from brain import analyze, getRandomTweet, thinkOfASentence
    # use this to grab info about Jaden
    # jaden_data = analyze()

from beak import tweet
    # use this to make a new tweet from our lovely bot
    # tweet('hello, world')

print 'starting\n'

for x in range(0,10):
    sentence = thinkOfASentence() # make wisdom
    tweet(sentence) # tweet it
    time.sleep(600) # sleep for ten minutes

print 'loop ended. shouldn\'t happen.\n'