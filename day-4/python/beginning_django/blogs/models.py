from django.db import models

# Create your models here.
class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    publications    = models.ManyToManyField(Publication)
    headline        = models.CharField(max_length=100)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
