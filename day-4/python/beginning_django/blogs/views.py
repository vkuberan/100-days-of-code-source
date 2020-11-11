from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Publication, Article
# Create your views here.
def all_publications(requst):
    publications = Publication.objects.all()
    html = ''
    for p in publications:
        html += '{} ({}) <br />'.format(p.title, publications.query)

        articles = p.article_set.all()

        for a in articles:
            html += "<li>{} ({}) </li>".format(a.headline, articles.query)

    return HttpResponse(html)

def single_publication(response, publication_id):
    html = ''
    
    try:
        publication = Publication.objects.get(pk=publication_id)
        html += publication.title + "<br />"
        articles = publication.article_set.all()
        for a in articles:
            html += '<li>' + a.headline + '</li>'
        
    except Publication.DoesNotExist:
        html += "Publication not found or Something went wrong.<br />"

    return HttpResponse(html)

def all_articles(requst):
    articles = Article.objects.all()
    html = ''
    for a in articles:
        html += a.headline + '<br />'
    return HttpResponse(html)

def single_article(response, article_id):
    html = ''
    
    try:
        article = Article.objects.get(id=article_id)
        html += article.headline + "<br />"
    except Article.DoesNotExist:
        html += "Article not found or Something went wrong.<br />"

    return HttpResponse(html)