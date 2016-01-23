#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, json

print 'starting'

# load in secrets
print 'loading secrets'

secrets_file = open('secrets.json', 'r')
secrets_decode = json.load(secrets_file)


# ~~~~~~~~~~~~~~~~~~~~~~~~
# load in the twitter data
print 'loading twitter data'

CONSUMER_KEY = secrets_decode["twitter"]["consumer_key"]
CONSUMER_SECRET = secrets_decode["twitter"]["consumer_secret"]
ACCESS_KEY = secrets_decode["twitter"]["access_key"]
ACCESS_SECRET = secrets_decode["twitter"]["access_secret"]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# do things
print 'doing things'

api.update_status("i'm alive!!")

print 'done'