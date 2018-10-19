import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random

from first_app.models import *
from faker import Faker

fakegen=Faker()
topics=['Search','Social','MarketPlace','News','Games']

def add_topic():
	t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t

def populate(N=5):
	for entry in range(N):

		#get the topic for the entry
		top=add_topic()

		#create fake data for that entry
		fake_url=fakegen.url()
		fake_date=fakegen.date()
		fake_name=fakegen.company()


		#create web page entry
		webpg=WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

		#create a fake access record
		acc_record=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
	print('populating script')
	populate(20)
	print("populating complete")