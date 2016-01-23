import tweepy, json, csv

secrets_file = open('secrets.json', 'r')
secrets = json.load(secrets_file)

# ~~~~~~~~~~~~~~~~~~~~~~~~
# load in the twitter data

CONSUMER_KEY = secrets["twitter"]["consumer_key"]
CONSUMER_SECRET = secrets["twitter"]["consumer_secret"]
ACCESS_KEY = secrets["twitter"]["access_key"]
ACCESS_SECRET = secrets["twitter"]["access_secret"]

# tweepy - for posting
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# make status
def tweet(newStatus):
    print 'updating status'
    api.update_status(newStatus)
    return;
