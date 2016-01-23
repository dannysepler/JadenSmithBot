#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, json
from twython import Twython


# my interface
from updateTweets import get_all_tweets
    # use this to update our list of jaden's tweets
    # get_all_tweets()

from brain import analyze, getRandomTweet
    # use this to grab info about Jaden
    # jaden_data = analyze()

from beak import tweet
    # use this to make a new tweet from our lovely bot
    # tweet('hello, world')

print 'starting\n'
tweet('dear fans, i\'m testing this bot by posting random jaden tweets. the smarts are coming soon! stay beautiful.')

for x in range(0, 10):
    print 'tweet #' + str(x)
    tweet(getRandomTweet())

# run this function to update our current Tweet Bank
# get_all_tweets()

print '\ndone with loop'

tweet('thanks, fans')

print '\ndone with program'