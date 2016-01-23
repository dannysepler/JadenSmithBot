import json
from twython import Twython

secrets_file = open('secrets.json', 'r')
secrets = json.load(secrets_file)

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
def analyze():
    print 'starting analysis'

    jaden_id = secrets["jaden"]["twitter_id"]
    jaden_data = twython.lookup_user(user_id = jaden_id)

    return jaden_data

    # sample parsing:
    #
    # print 'obtained ' + jaden_data[0]["name"] + '\'s data'
    # print '\n\n~~~~\n' + json.dumps(jaden_data, indent=4, sort_keys=True) + '\n~~~~\n\n'

