#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, json
from twython import Twython


# my interface
from tweetlist import get_all_tweets, clean, makeMarkovChain
    # use get_all_tweets() to update our list of jaden's tweets
    # use clean() to make our list even better

from brain import analyze, getRandomTweet
    # use this to grab info about Jaden
    # jaden_data = analyze()

from beak import tweet
    # use this to make a new tweet from our lovely bot
    # tweet('hello, world')

print 'cleaning\n'

makeMarkovChain()

print 'done\n'




'''tweet('dear fans, i\'m testing this bot by posting random jaden tweets. the smarts are coming soon! stay beautiful.')

for x in range(0, 10):
    print 'tweet #' + str(x)
    tweet(getRandomTweet())

# run this function to update our current Tweet Bank
# get_all_tweets()

print '\ndone with loop'

tweet('thanks, fans')
'''