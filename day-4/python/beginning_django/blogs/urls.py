from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^publications/$', views.all_publications, name="allpubs"),
    re_path(r'^publication/(?P<publication_id>\d+)/$', views.single_publication, name="singlepub"),
    re_path(r'^articles/$', views.all_articles, name="allarticles"),
    re_path(r'^article/(?P<article_id>\d+)/$', views.single_article, name="singleart")
]