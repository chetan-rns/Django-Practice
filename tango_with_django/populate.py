import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django.settings')
import django
django.setup()
from rango.models import Category, Page
from faker import Faker

def populate(N=10):
	fakegen=Faker()
	cat=['python','django','other']
	i=0
	for i in range(3): #For each category add many pages
		fake_name=cat[i]
		c=Category.objects.get_or_create(name=fake_name,views=i*10,likes=i*5)[0]
		c.save()
		for j in range(10):
			fake_title=fakegen.company()
			fake_url=fakegen.url()
			fake_views=j*10
			p=Page.objects.get_or_create(category=c,title=fake_title,url=fake_url,views=fake_views)[0]
			p.save()

if __name__ == '__main__':
	print('Populating the database')
	populate(50)
	print('Done!!')
