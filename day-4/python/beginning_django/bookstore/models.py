from django.db import models

# Create your models here.
class Author(models.Model):
    TITLE = (
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Ms.', 'Ms.'),
        ('Miss', 'Miss')
    )

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others/Unknown')
    )

    title           = models.CharField(max_length=5, choices=TITLE)
    first_name      = models.CharField(max_length=30)
    last_name       = models.CharField(max_length=30)
    gender          = models.CharField(max_length=1, choices=GENDER)
    birth_date      = models.DateField("Date Of Birth")
    phone_number    = models.CharField(max_length=35)
    email           = models.EmailField()
    ssn             = models.CharField("SSN", max_length=20)
    address         = models.CharField(max_length=100)
    city            = models.CharField(max_length=30)
    state           = models.CharField(max_length=30)
    postal_code     = models.CharField(max_length=15)
    country         = models.CharField(max_length=5)


    def __str__(self):
        return '{} {} {}'.format(self.title, self.first_name, self.last_name)

class Publisher(models.Model):
    name = models.CharField("Publisher Name", max_length=300)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_title      = models.CharField("Book Title", max_length=300)
    pages           = models.IntegerField("Total Pages")
    price           = models.DecimalField(max_digits=10, decimal_places=2)
    rating          = models.FloatField()
    authors         = models.ManyToManyField(Author)
    publisher       = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    published_date  = models.DateField("Published Date")

    def __str__(self):
        return self.book_title

class Store(models.Model):
    store_name  = models.CharField(max_length=300)
    books       = models.ManyToManyField(Book)

    def __str__(self):
        return self.store_name

