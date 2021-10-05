import tweepy

from authorization_tokens import *

import random
import sys, os

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# calling the api
api = tweepy.API(auth)

#Different Tweets To Use

Diff_Tweets = ["A behind the scenes look at And It Began To Rain", "A look back at retro Aetheria"]

# Text in Tweet
status = random.choice(Diff_Tweets)

#Image Lists

image_list_Retro=["Images/RetroLogo.jpg",
"Images/80sTest3.png",
"Images/80sTest2.png",
"Images/80sTest.png"]

image_list_contemp= [
"Images/EveWhiteEyeTest1.png",
"Images/EveWhiteEyeTest2.png",
"Images/Wren.png"]

# The Picture That is Uploaded

if status == "A behind the scenes look at And It Began To Rain":
    filename = random.choice(image_list_contemp)

if status == "A look back at retro Aetheria":
    filename = random.choice(image_list_Retro)

full_filename = os.path.join( sys.path[0], filename )

# Posting
api.update_with_media(full_filename, status)
