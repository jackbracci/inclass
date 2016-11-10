#
# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
print ("Jonathan Bracci")
print ("\n")
print("""No output necessary although you 
	can print out a success/failure message if you want to.""")

import tweepy
import nltk
import requests
import requests_oauthlib

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
image = "/Users/JonathanBracci/Desktop/problemset3/SI206/Barcelona.jpg"  
print("Posting... ")
api.update_with_media(image, status="#UMSI-206 #Proj3")
print("Posted")