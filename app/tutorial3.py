import tweepy
import random

from authorization_tokens import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


# Option 5: Basic search
search_results = api.search(q="Bezos filter:safe", lang="en")

# Option 5: Basic search
search_results = api.search(q="Bezos filter:safe", lang="en")
random_tweet = random.choice(search_results)

# Option 5: Basic search
search_results = api.search(q="Bezos filter:safe", lang="en")
random_tweet = random.choice(search_results)
print( dir(random_tweet) )

# Option 5: Basic search
text = random_tweet.text
message = text.replace("Bezos", "Bezos, who pays no taxes,")
print(message)



api.update_status(message)
print("Done.")
