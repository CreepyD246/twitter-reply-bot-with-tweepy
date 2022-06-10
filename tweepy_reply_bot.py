# Importing Modules/Libraries
import tweepy
import time
from datetime import datetime

# Credentials (Insert your keys and tokens below)
api_key = ""
api_secret = ""
bearer_token = r""
access_token = ""
access_token_secret = ""

# Connecting to Twitter API
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Message to reply with if someone mentions the bot
message = "Send me a message if you have any questions"

# Bot's unique ID
client_id = client.get_me().data.id

# This is so the bot only looks for the most recent tweets.
start_id = 1
initialisation_resp = client.get_users_mentions(client_id)
if initialisation_resp.data != None:
    start_id = initialisation_resp.data[0].id

# Looking for mentions tweets in an endless loop
while True:
    response = client.get_users_mentions(client_id, since_id=start_id)

    # Reply Code
    if response.data != None:
        for tweet in response.data:
            try:
                print(tweet.text)
                client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message)
                start_id = tweet.id
            except Exception as error:
                print(error)

    # Delay (so the bot doesn't search for new tweets a bucn of time each second)
    time.sleep(5)
