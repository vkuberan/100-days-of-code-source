import os, django, time, random
from datetime import timedelta, date
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beginning_django.settings")
django.setup()

from bookstore.models import Book, Author
from faker import Faker
import random
from time import sleep

cnt = 1

for i in range(1, 50001):
        
    fake    = Faker()
    title   = fake.text()
    pages   = random.randint(99, 699)
    price   = '{:02.2f}'.format(random.uniform(0.99, 49.99))
    rating  = '{:02.2f}'.format(random.uniform(1.0, 5.0))
    publisher = random.randint(1, 220)

    tempYear = random.randint(1950, 2020)
    tempMonth = random.randint(1, 12)
    tempDay = random.randint(1, 28)

    published_date = date(tempYear, tempMonth, tempDay)


    if len(title) >= 300:
        title = title[0:295] + '...'

    books  = '{}\n'.format(cnt)
    books += 'Book Title: {}\n'.format(title)
    books += 'Pages: {}\n'.format(pages)
    books += 'Price: {}\n'.format(price)
    books += 'Rating: {}\n'.format(rating)
    books += 'Publisher: {}\n'.format(publisher)
    books += 'Published Date: {}\n'.format(published_date.strftime("%Y-%m-%d"))

    book = Book()
    book.book_title = title
    book.pages = pages
    book.price = price
    book.rating = rating
    book.publisher_id = publisher
    book.published_date = published_date

    author_id = [random.randint(1, 1572)]

    if cnt % 17 == 0:
        for i in range(1, 3):
            author_id.append(random.randint(1,1572))

    if cnt % 29 == 0:
        for i in range(1, 4):
            author_id.append(random.randint(1,1572))

    if cnt % 71 == 0:
        for i in range(1, 5):
            author_id.append(random.randint(1, 1572))

    if cnt % 97 == 0:
        for i in range(1, 7):
            author_id.append(random.randint(1, 1572))


    book.save()

    tAuthors = Author.objects.filter(pk__in=author_id)
    # print(author_id, tAuthors)

    book.authors.set(tAuthors)

    print(books)
    
    cnt += 1