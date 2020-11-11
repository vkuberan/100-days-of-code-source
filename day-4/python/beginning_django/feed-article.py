import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beginning_django.settings")
django.setup()

from django.contrib.auth.models import User
from vblogs.models import Article
from faker import Faker
import random
from time import sleep

for i in range(1, 25001):

    fake = Faker()
    txt = fake.text()

    if len(txt) >= 129:
        txt = txt[0:125] + '...'

    category_id = random.randint(1, 55)

    article = Article(headline=txt, category_id=category_id)
    article.save()

    print('{}] {} \nLength: {}\nCategory Id: {}\n\n'.format(i, txt, len(txt), category_id))
    