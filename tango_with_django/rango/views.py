from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category,Page
# Create your views here.

def index(request):
	context_dict={'boldmessage':'Crunchy,creamy,cookie,candie'}
	return render(request, 'rango/index.html',context=context_dict)

def about(request):
	develop_context={'developer':'chetan'}
	return render(request,'rango/about.html',context=develop_context)	 