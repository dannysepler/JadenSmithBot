#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, json
from twython import Twython


# my interface
from updateTweets import get_all_tweets
    # use this to update our list of jaden's tweets
    # get_all_tweets()

from brain import analyze
    # use this to grab info about Jaden
    # jaden_data = analyze()

from beak import tweet
    # use this to make a new tweet from our lovely bot
    # tweet('hello, world')

print 'starting'

# load in secrets
print 'loading secrets'

# for obvious reasons, i'm not putting this file on github
# to get access, reach out to me!

secrets_file = open('secrets.json', 'r')
secrets = json.load(secrets_file)


# run this function to update our current Tweet Bank
# get_all_tweets()

print 'exiting'