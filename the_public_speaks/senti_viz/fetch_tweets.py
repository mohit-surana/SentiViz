from constants import *
import tweepy
import sys
import jsonpickle
import os


# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)

if not api:
	print 'Can\'t Authenticate'
	sys.exit(-1)


f = open('tweets.txt', 'w')

i = 0
for tweet in tweepy.Cursor(api.search, q='trump', since='2016-10-23', until='2016-11-19', lang='en').items():
	print i; i += 1
	print type(tweet.text)
	f.write(tweet.text.encode('utf-8'))

f.close()
