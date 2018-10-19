from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.forms import NewUserForm
# Create your views here.


def index(request):
	return HttpResponse("<em>My second app</em>")

def help(request):
	my_dict={'help_me':'PLease help me!!'}
	return render(request, 'AppTwo/help.html',context=my_dict)

def users(request):
	
	form=NewUserForm()
	if request.method=='POST':
		form=NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return help(request)
		else:
			print('Invalid form details')
	return render(request, 'AppTwo/users.html',{'form':form})