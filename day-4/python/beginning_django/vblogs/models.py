from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    views    = models.IntegerField(default=0, db_index=True)

    def __str__(self):
        return self.headline
