import csv
import re
from nltk.corpus import stopwords

stop_words = [u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves', u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its', u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what', u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has', u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an', u'the', u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of', u'at', u'by', u'for', u'with', u'about', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again', u'further', u'then', u'once', u'here', u'there', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other', u'some', u'such', u'only', u'own', u'same', u'so', u'than', u'too', u's', u't', u'will', u'just', u'now', u'd', u'll', u'm', u'o', u've', u'y', u'ma']
stop_words = [str(x) for x in stop_words]

def clean_tweet(tweet):
	tweet = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet)
	tweet = re.sub('RT ', '', tweet)
	tweet = re.sub('amp', '', tweet)
	tweet = re.sub('\n', ' ', tweet)
	tweet = re.sub('[#.$%\-|~\/&0-9"\'*+=!?;:()^]', '', tweet)
	tweet = tweet.replace('\\', '')
	tweet = re.sub(' +', ' ', tweet)
	tweet = tweet.lower()

	tweet = [word for word in tweet.split() if word not in stop_words]
	return ' '.join(tweet)

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
