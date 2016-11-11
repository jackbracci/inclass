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

access_token = "331897710-t8nnZuAh1ofe0lCUSfKBQNlqBOMHgGUooIy5UN4x"
access_token_secret = "FNc3y1c8FgzFezvAf0ml5ofVEAE3JE7f1zSsyq7W8OeFE"
consumer_key = "ixWyhyZ1BDfiy2qgSLGjrA57y"
consumer_secret = "m1rjKpFhfXhRBzET9dEPIciaY4HHHQAj5urznBlm7yY7273BYk"


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
image = "/Users/JonathanBracci/Desktop/problemset3/SI206/Barcelona.jpg"  
print("Posting... ")
api.update_with_media(image, status="#UMSI-206 #Proj3")
print("Posted")