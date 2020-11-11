from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'vblogs/categories/^$', views.vblogs_categories, name='vcategories'),
    re_path(r'^vblogs/category/(?P<category_id>\d+)/$', views.vblogs_category, name='vcategory'),
    re_path(r'^vblogs/articles/$', views.vblogs_articles, name='varticles'),
    re_path(r'^vblogs/article/(?P<article_id>\d+)/$', views.vblogs_article, name='varticle'),
]