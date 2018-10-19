import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')

import django
django.setup()

import random

from AppTwo.models import *
from faker import Faker

def populate(N=10):
	fakegen=Faker()
	for i in range(N):
		fake_first_name=fakegen.first_name()
		fake_last_name=fakegen.last_name()
		fake_email=fakegen.email()
		usr=User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

if __name__ == '__main__':
	print("populating")
	populate(20)
	print("done")