from django.contrib import admin

# Register your models here.
from .models import Publication, Article

admin.site.register(Publication)
admin.site.register(Article)
