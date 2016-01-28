import json, csv, random
from twython import Twython

secrets_file = open('secrets.json', 'r')
secrets = json.load(secrets_file)

jadentweets_file = open('officialjaden_tweets.csv', 'r')

CONSUMER_KEY = secrets["twitter"]["consumer_key"]
CONSUMER_SECRET = secrets["twitter"]["consumer_secret"]
ACCESS_KEY = secrets["twitter"]["access_key"]
ACCESS_SECRET = secrets["twitter"]["access_secret"]


# twython - for analysis
twython = Twython(app_key=CONSUMER_KEY,
            app_secret=CONSUMER_SECRET,
            oauth_token=ACCESS_KEY,
            oauth_token_secret=ACCESS_SECRET)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# data analysis

def thinkOfASentence():
    markov_file = open('loganMarkov.json', 'r')
    markov = json.load(markov_file)

    print 'Choosing First Word'

    sentence = ''
    addWord = random.choice(markov['data'].keys())
    sentence += addWord
    previousWord = addWord

    for x in range(0,10):
        try:
            addWord = random.choice(markov['data'][previousWord].keys())
            sentence += ' ' + addWord
            previousWord = addWord
        except KeyError:
            print 'Key Error'

            # try again
            return thinkOfASentence()

    print 'Setence Generated Fully'
    return sentence




def analyze():
    print 'starting analysis'

    jaden_id = secrets["jaden"]["twitter_id"]
    jaden_data = twython.lookup_user(user_id = jaden_id)

    return jaden_data

    # sample parsing:
    #
    # print 'obtained ' + jaden_data[0]["name"] + '\'s data'
    # print '\n\n~~~~\n' + json.dumps(jaden_data, indent=4, sort_keys=True) + '\n~~~~\n\n'

def censor(tweet):
    # this goes through all the bad words in "censor.json"
    # and then replaces them with 'better' words

    badwords_json = json.load(open('censor.json', 'r'))

    for word in badwords_json:
        for bad, better in word.iteritems():
            tweet = tweet.replace(bad, better)

    return tweet

def getRandomTweet():
    # got most of this code from http://stackoverflow.com/questions/10819911/read-random-lines-from-huge-csv-file-in-python

    filesize = sum(1 for row in jadentweets_file)
    offset = random.randrange(filesize)

    jadentweets_file.seek(offset)                  #go to random position
    jadentweets_file.readline()                    # discard - bound to be partial line
    random_line = jadentweets_file.readline()      # bingo!

    # extra to handle last/first line edge cases
    if len(random_line) == 0:       # we have hit the end
        jadentweets_file.seek(0)
        random_line = jadentweets_file.readline()  # so we'll grab the first line instead

    tweet = random_line.split(',')[2]

    tweet = censor(tweet)

    return tweet