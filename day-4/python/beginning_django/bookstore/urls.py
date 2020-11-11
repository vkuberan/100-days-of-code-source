from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^books/books/$', views.view_all_books, name='allbooks'),
    re_path(r'^books/(?P<book_id>\d+)/$', views.view_single_book, name='singlebook'),
    # re_path(r'^vblogs/categories/$', views.vblogs_categories, name='vcategories'),
    # re_path(r'^vblogs/category/(?P<category_id>\d+)/$', views.vblogs_category, name='vcategory'),
    # re_path(r'^vblogs/articles/$', views.vblogs_articles, name='varticles'),
    # re_path(r'^vblogs/article/(?P<article_id>\d+)/$', views.vblogs_article, name='varticle'),
]