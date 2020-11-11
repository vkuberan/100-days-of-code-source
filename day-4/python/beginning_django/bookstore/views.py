from django.shortcuts import render
from django.http import HttpResponse
import time

from . import models

# Create your views here.
def view_all_books(request):
    html = "<h1>Book Management - All Books</h1>"
    start = time.process_time()
    
    books = models.Book.objects.all().select_related(
        'publisher').prefetch_related('authors').only(
        'book_title', 'id', 'publisher__name',
        'authors__title','authors__first_name', 'authors__last_name').order_by('-id')[:10]

    # books = models.Book.objects.all().order_by('-id')[:50]

    html += '<ol>'
    for b in books:
        html += "<li>{} (ID: [{}])<br />Belongs To: {}<br />".format(b.book_title, b.id, b.publisher.name)
        
        authors = ", ".join("{} {} {}".format(a.title, a.first_name, a.last_name) for a in b.authors.all())
        # for a in b.authors.all():
        #     authors += ", ".join("{} {} {}".format())
        #     authors += "<br />{} {} {}".format(a.title, a.first_name, a.last_name)

        html += "Many to Many: {}<br><br>".format(authors)

        # html += "<li>{} <li>{}</li></li>".format(a.headline, a.category.name)
    html += '</ol>'
    end = time.process_time() - start
    html = "Time Taken: {}<br />".format(end) + html
    return HttpResponse(html)

def view_single_book(request, book_id):
    book = models.Book.objects.get(id=book_id)
    html = "Title: {}<br />Price: {}<br />Pages: {}".format(book.book_title, book.price, book.pages)
    return HttpResponse(html)