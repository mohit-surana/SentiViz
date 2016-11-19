from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

import os

def index(request):
	return HttpResponse("Hello, world. You're at the SentiViz index.")

def display(request):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	STATIC_URL = '/senti_viz/static/'
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')
	context = {'param': 'value', 'STATIC_URL': STATIC_URL}
	return render(request, 'senti_viz/home.html', context)
