from django.db import models

# Create your models here.
class Publisher(models.Model):
    name    = models.CharField(max_length=30)
    address = models.CharField(max_length=60)
    city    = models.CharField(max_length=60)
    state   = models.CharField(max_length=30)
    country = models.CharField(max_length=2)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Author(models.Model):
    TITILE = (
        ('Mr.',  'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Miss', 'Miss'),
        ('Ms', 'Ms'),
    )

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unknown/Other')
    )

    title   = models.CharField(max_length=5, choices=TITILE)
    gender  = models.CharField(max_length=1, choices=GENDER)
    name    = models.CharField(max_length=60)
    email   = models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title            = models.CharField(max_length=100)
    authors          = models.ManyToManyField('Author')
    publisher        = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title