from django.contrib import admin

# Register your models here.
from . import models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'total_articles']

    def total_articles(self, obj):
        return obj.article_set.count()

    total_articles.short_description = 'Total Articles'

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'headline', 'category']


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Article, ArticleAdmin)


