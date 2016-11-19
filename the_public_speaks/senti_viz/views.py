from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world. You're at the SentiViz index.")

def display(request):
	context = {'param': 'value'}
	return render(request, 'home.html', context)
