from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

def index(request):
	print "i m here ....."
	context = {'latest_question_list': "latest_question_list"}
	return render(request, 'homx/index.html', context)
