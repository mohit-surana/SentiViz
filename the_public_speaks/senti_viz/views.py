from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from fetch_tweets import fetch

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
	print(results)
	if('error' in results or not results):
 		return HttpResponse('Yen illa boss!')
	else:
		return render(request, 'senti_viz/results.html', results)
