#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, json, time
from twython import Twython


# my interface
from tweetlist import getAllTweets, cleanTweets, makeMarkovChain
    # use get_all_tweets() to update our list of jaden's tweets
    # use clean() to make our list even better

from brain import analyze, getRandomTweet, thinkOfASentence
    # use this to grab info about Jaden
    # jaden_data = analyze()

from beak import tweet
    # use this to make a new tweet from our lovely bot
    # tweet('hello, world')

# dear reader,
#
# there's several different things you can do with this twitter bot.
# as time goes on, it should keep gaining functionality.
#
# here's the run down of where it is right now....
#
# 1. GETTING THE DATA
#
# this twitter bot works by taking a twitter user, and putting all
# of his/her tweets into a CSV (comma-separated) file. wanna do that? run this:
#
#       getAllTweets(twitter_handle) -> where 'twitter_handle' is the
#                                         handle of the twitter user minus the @
#                                         so, like, "officialjaden" would work for jaden smith.
#
#
# 2. IMPROVING THE DATA
#
# for jaden, his tweets are located in "officialjaden_tweets.csv" -- the initial time
# i worked with this data, i noticed that about 2/3 of his tweets were "retweets" of
# other users. also, some of the data breaks the CSV form, which is no bueno.
# so, i removed all those bad cases. do that by running:
#
#      cleanTweets()
#
#
# 3. THE MARKOV CHAIN
#
# the main smarts behind this program relies on something called a Markov Chain.
# the central question is: we have a very large set of data that tells us how Jaden
# talks... how do we leverage that to reproduce his grammar?
#
# a markov chain takes all of his tweets, and splits them into two word chunks.
# take this...
#
#           "School is so overrated."   ->   {"School",     "is"        },
#                                            {"is",         "so"        },
#                                            {"so",         "overrated" },
#                                            {"overrated",  "."         }
#
# now imagine this without about 1,500 tweets of information. that's what we've
# got stored in "markov.json" -- the real magic comes when you have more data.
#
#   Let's take a random word: "School"
#
# Jaden's probably said "School" in several tweets. So we take all the
# different words he's said AFTER "School", and pick a random one. And then we follow that
# pattern, until we reach the end of a tweet -> either a period, or our word limit is used up.
#
# So... here's an example. We pick "School":
#
#       markov.json     ->   "School" : {
#                                 "is":   "2", # the "2" denotes the frequency that "is" appeared after "School"
#                                 "room": "1",
#                                 "can": "1"
#                            }
#
#
#       Say that the program randomly picks "is". Our sentence so far is "School is", and
#       here are we search "is" in markov.json in order to find the next word in our sentence.
#
#                       "is":  {
#                           "so": "3",
#                           "a":  "1",
#                           "happy": "1",
#                           "too": "1",
#                           "."
#                       }
#
#        and etc and etc until we randomly select a period, or our word count is reached.
#
#
# Currently, this app only goes for ten words. And it doesn't use the word frequencies at all.
# Those would be two great additions, for anyone that wants to improve the app! :)
#
#
# 4. GENERATING A SENTENCE
#
# Next up, we have the markov chain. To generate our tweet (in a process just like what I
# showed above, you use the function...
#
#   "thinkOfASentence()" -> this returns back a sentence, so make sure you save it into
#   a variable like so.... "sentence = thinkOfASentence()"
#
# 5. TWEET IT
#
# We Tweet using "Tweepy" -- a Python plugin that uses Twitter's API. Tweet by running:
#
#               tweet(sentence)
#
# where the sentence is any string you want to tweet. Remember that Twitter limits its
# Tweets to 140 characters.
#
# - danny



print 'starting\n'

while True:
    sentence = thinkOfASentence() # make wisdom
    tweet(sentence) # tweet it
    time.sleep(600) # sleep for ten minutes

print 'loop ended. shouldn\'t happen.\n'