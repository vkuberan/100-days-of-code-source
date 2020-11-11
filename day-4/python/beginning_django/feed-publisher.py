import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beginning_django.settings")
django.setup()

from bookstore.models import Publisher
from faker import Faker
import phonenumbers

cnt = 1

for i in range(1, 221):
        
    fake    = Faker()
    profile = fake.profile()
    company = fake.company()

    pub = Publisher()
    pub.name = company
    pub.save()

    print('%d] %s' % (cnt, company))
    
    cnt += 1