from django.shortcuts import render
from django.http import HttpResponse
import time

from . import models

# Create your views here.
def vblogs_categories(request):
    html = "Video Blog - Categories"
    return HttpResponse(html)

def vblogs_category(request, category_id):
    html = "Video Blog - Category ID: " + category_id
    return HttpResponse(html)

def vblogs_articles(request):
    html = "<h1>Video Blog - Articles</h1>"
    start = time.process_time()
    # articles = models.Article.objects.select_related('category').all().order_by('-id')[5000:10000]
    articles = models.Article.objects.all().order_by('-id')[5000:10000]
    html += '<ol>'
    for a in articles:
        html += "<li>{} (ID: [{}])<li>Belongs To: {}</li></li>".format(a.headline, a.id, a.category.name)
        # html += "<li>{} <li>{}</li></li>".format(a.headline, a.category.name)
    html += '</ol>'
    end = time.process_time() - start
    html = "Time Taken: {}<br />".format(end) + html
    return HttpResponse(html)

def vblogs_article(request, article_id):
    html = "Video Blog - Article ID: " + article_id
    return HttpResponse(html)
