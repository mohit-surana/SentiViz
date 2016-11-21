import os
import csv
import re

filename = 'input.txt'

def clean_tweet(tweet, query=None):
	tweet = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet)
	tweet = re.sub('RT ', '', tweet)
	tweet = re.sub('amp', '', tweet)
	tweet = re.sub('\n', ' ', tweet)
	tweet = re.sub('[#.$%\-|~\/&0-9"\'*+=!?;:()^]', '', tweet)
	tweet = tweet.replace('\\', '')
	tweet = re.sub(' +', ' ', tweet)
	tweet = tweet.lower()
	if query:
		for i in query:
			tweet = re.sub(i, '', tweet)

	# tweet = [word for word in tweet.split() if word not in stop_words]
	return tweet

def preprocess(query=[]):
	f = open(filename, 'r')
	tweet = f.read()
	tweet = clean_tweet(tweet, query)
	f.close()
	print tweet[:500]
	f = open(filename, 'w')
	f.write(tweet)
	f.close()


if __name__ == "__main__":
	cleaned_tweets = []

	reader = csv.reader(open('data.csv', 'rU'))
	for i, row in enumerate(reader):
		print(i)
		row[3] = clean_tweet(row[3])
		cleaned_tweets.append([row[3], row[1]])

	with open('CleanData.csv', 'wb') as csvfile:
		writer = csv.writer(csvfile)
		for tweet in cleaned_tweets:
			writer.writerow(tweet)
