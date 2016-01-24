#
#  grabbed most of this code from https://gist.github.com/yanofsky/5436496
#  only changed a bit of it
#
#
# i will be keeping a separate file for holding all of jaden smith's tweets.
# this should speed up the process of generating a tweet, because i won't constantly
# be grabbing it from online.

import json, tweepy, csv, os

secrets_file = open('secrets.json', 'r')
secrets = json.load(secrets_file)

# Twitter API credentials
CONSUMER_KEY = secrets["twitter"]["consumer_key"]
CONSUMER_SECRET = secrets["twitter"]["consumer_secret"]
ACCESS_KEY = secrets["twitter"]["access_key"]
ACCESS_SECRET = secrets["twitter"]["access_secret"]

screen_name = secrets["jaden"]["handle"]


def get_all_tweets():
    # Twitter only allows access to a users most recent 3240 tweets with this method

    # authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    # initialize a list to hold all the tweepy Tweets
    alltweets = []

    # make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name=screen_name, count=200)

    # save most recent tweets
    alltweets.extend(new_tweets)

    # save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    # keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)

        # all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)

        # save most recent tweets
        alltweets.extend(new_tweets)

        # update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        print "...%s tweets downloaded so far" % (len(alltweets))

    # transform the tweepy tweets into a 2D array that will populate the csv
    outtweets = [[tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

    # write the csv
    with open('%s_tweets.csv' % screen_name, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["created_at", "text"])
        writer.writerows(outtweets)

    pass

def isRetweet(row):
    # TODO: check if 'RT @' are the first letters of the tweet
    tweet = row.split(',')[2] # isolate the tweet

    return 'RT @' in tweet

def isLineBreak(row):

            # lots of tweets, for some reason, have line breaks in them.
            # if a line in the CSV doesn't have at least two commas, i'm assuming that
            # it's a mistake and i'm getting rid of it.

    count = row.count(",")
    return count < 2


def makeMarkovChain():

    print 'making markov chain'

    jadentweets_file = open('officialjaden_tweets.csv', 'r')
    # markovJSON = json.loads(request.POST.get('mydata', '{}'))
    markovData = {}

    for row in jadentweets_file:
        tweet = row.split(',')[2] # isolate the tweet
        tweetWords = tweet.split(' ')

        previousWord = ''
        for tweetWord in tweetWords:
            if previousWord is not '':
                if not markovData.get(previousWord): # key isn't there
                    markovData[0][previousWord] = [] # init
                    markovData[0][previousWord][tweetWord] = str(0) # start frequency at 0

                elif not markovData.get(tweetWord): # value isn't there
                    markovData[0][previousWord][tweetWord] = str(0) # start at 0

                else: # increment
                    index = markovData[0][previousWord][tweetWord]
                    index = int(index) + 1
                    markovData[0][previousWord][tweetWord] = str(index)

            previousWord = tweetWord


    markovJSONfile = open('markov.json', 'r+')
    markovJSONfile = json.dump(markovData)
    markovJSONfile.close()

    jadentweets_file.close()

    print 'finished, exiting'




def clean():
    editedfile = 'editedjadentweets.csv'

    try: # remove file if it exists
        os.remove(editedfile)
        print 'removed editedjadentweets file'
    except OSError:
        pass


    jadentweets_file = open('officialjaden_tweets.csv', 'r')
    output = open(editedfile, 'wb')

    for row in jadentweets_file:

        if isLineBreak(row):
            # don't write this to new file
            continue
        elif isRetweet(row):
            # don't write this either
            continue
        else:
            output.write(row)

    output.close()
    jadentweets_file.close()

    # remove old file
    official_file = 'officialjaden_tweets.csv'
    os.remove(official_file)
    os.rename(editedfile, official_file)

    return