from django.shortcuts import render
from django.http import HttpResponse
from fetch_tweets import fetch

from keras.models import load_model

import lstm
from lstm import *
import pickle
import os

def index(request):
	return HttpResponse("Hello, world. You're at the SentiViz index.")

def display(request):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	STATIC_URL = '/static/'
	# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	context = {'param': 'value', 'STATIC_URL': STATIC_URL}
	return render(request, 'senti_viz/home.html', context)

def search(request, query):
	results = fetch(query)
	if('error' in results or not results):
 		return HttpResponse('No results found.')
	else:
		model = load_model('senti_viz/lstm_model.h5')
		model.predict = BinarizedSentimentAnalyzer().predict
		predictions = model.predict(results['results'])
		# print predictions
		# print {'pos_predictions': predictions[1], 'neg_predictions': predictions[0]}
		return render(request, 'senti_viz/results.html', {'pos_predictions': predictions[1], 'neg_predictions': predictions[0]})
