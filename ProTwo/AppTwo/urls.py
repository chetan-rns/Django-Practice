from django.conf.urls import url
from AppTwo import views

urlpatterns=[
	#url(r'^$', views.help,name='help'),
	url(r'^$', views.users,name='user'),
]