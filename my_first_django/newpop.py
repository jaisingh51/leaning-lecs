import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_first_django.settings')

import django
django.setup()


import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker
fakegen= Faker()
topics=['search','socia media','marketplace','news','game']

def add_topics():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save
    return t

def populate(n=5):
    for entry in range(n):
        top=add_topics()
        fake_data=fakegen.date()
        fake_name=fakegen.name()
        fake_url=fakegen.url()


        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_data)[0]


if __name__ == '__main__':
    populate(20)
    print("done")
