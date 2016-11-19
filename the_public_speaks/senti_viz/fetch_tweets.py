from constants import *
import tweepy
import sys
import os
import json

MAX_TWEETS = 10

def fetch(query, lang='en', **kwargs):
	auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	api = tweepy.API(auth, wait_on_rate_limit=True,
					   wait_on_rate_limit_notify=True)
	results = []
	if not api:
		return {'error' : 'Can\'t Authenticate'}
	else:
		f = open('tweets.txt', 'w')
		i = 0
		l = []
		for tweet in tweepy.Cursor(api.search, q=query, lang=lang, **kwargs).items():
			i += 1
			s = tweet.text.encode('utf-8')
			f.write(s)
			l.append(s)
			if(i == MAX_TWEETS):
				break
		f.close()
		results = l

	return {'results' : results}
