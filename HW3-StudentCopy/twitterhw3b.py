
# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
print ("Jonathan Bracci")
print ("\n")


import tweepy
import nltk
import requests
import requests_oauthlib
from textblob import TextBlob

access_token = "331897710-t8nnZuAh1ofe0lCUSfKBQNlqBOMHgGUooIy5UN4x"
access_token_secret = "FNc3y1c8FgzFezvAf0ml5ofVEAE3JE7f1zSsyq7W8OeFE"
consumer_key = "ixWyhyZ1BDfiy2qgSLGjrA57y"
consumer_secret = "m1rjKpFhfXhRBzET9dEPIciaY4HHHQAj5urznBlm7yY7273BYk"


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

Tweets = api.search('Trump and Hillary')

averagesubjectivity = 0
averagepolarity = 0
count = 0 

for tweet in Tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	tweetsubjectivity = analysis.subjectivity
	tweetpolarity = analysis.polarity
	count += 1
	averagesubjectivity += tweetsubjectivity
	averagepolarity += tweetpolarity
	print("Tweet Subjectivity: ", tweetsubjectivity)
	print("Tweet Polarity: ", tweetpolarity)


print("Average Subjectivity: ", (averagesubjectivity / count))
print("Average Polarity: ", (averagepolarity / count))
