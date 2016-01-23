#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, json
from twython import Twython

print 'starting'

# load in secrets
print 'loading secrets'

secrets_file = open('secrets.json', 'r')
secrets = json.load(secrets_file)



# ~~~~~~~~~~~~~~~~~~~~~~~~
# load in the twitter data
print 'loading twitter data'

CONSUMER_KEY = secrets["twitter"]["consumer_key"]
CONSUMER_SECRET = secrets["twitter"]["consumer_secret"]
ACCESS_KEY = secrets["twitter"]["access_key"]
ACCESS_SECRET = secrets["twitter"]["access_secret"]

# tweepy - for posting
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# twython - for analysis
twython = Twython(app_key=CONSUMER_KEY,
            app_secret=CONSUMER_SECRET,
            oauth_token=ACCESS_KEY,
            oauth_token_secret=ACCESS_SECRET)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# data analysis
print 'starts analysis'

jaden_id = secrets["jaden"]["twitter_id"]
jaden_data = twython.lookup_user(user_id = jaden_id)

print 'obtained ' + jaden_data[0]["name"] + '\'s data'

print '\n\n~~~~\n' + json.dumps(jaden_data, indent=4, sort_keys=True) + '\n~~~~\n\n'


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# make status
def updateStatus(newStatus):
    print 'updating status'
    api.update_status(newStatus)
    return;

print 'exiting'