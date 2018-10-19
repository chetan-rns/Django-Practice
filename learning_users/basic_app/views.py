from django.shortcuts import render
from django.forms import UserForm,UserProfileInfoForm
# Create your views here.

def index(request):
	return render(request, 'basic_app/index.html')


def register(request):
	registered=False

	if request.method == 'POST':
		user_form=UserForm(request='POST')
		profile_form=UserProfileInfoForm(request='POST')

		if user_form.is_valid() and profile_form.is_valid():

			user=user_form.save()
			user.set_password(user.password)
			user.save()

			profile=profile_form.save(commit=False)
			