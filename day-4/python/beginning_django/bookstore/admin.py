from django.contrib import admin

from .models import Author, Publisher, Book, Store

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'author_name', 'email', 'phone_number']

    def author_name(self, obj):
        return "{} {} {}".format(obj.title, obj.first_name, obj.last_name)

    author_name.short_description = "Author Name"

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'publisher_name', 'total_books']

    def publisher_name(self, obj):
        return obj.name

    def total_books(self, obj):
        return Book.objects.filter(publisher__id=obj.id).count()

    publisher_name.short_description = "Publisher Name"

class BookAdmin(admin.ModelAdmin):
    # list_display = ['id', 'title', 'myprice', 'pub', 'display_authors']
    list_display = ['id', 'title', 'myprice', 'pages', 'rating']
    
    # list_select_related = ('publisher', 'authors')

    def title(self, obj):
        title = obj.book_title
        if len(title) >= 100:
            title = title[0:97] + '...'
        return title

    def myprice(self, obj):
        return '${}'.format(obj.price)

    def pub(self, obj):
        return obj.publisher.name

    def display_authors(self, obj):
        # return '<br/>'.join(['{} {} {}'.format(a.title, a.first_name, a.last_name) for a in obj.authors.all()])
        return ', '.join([a.first_name for a in obj.authors.all()])


    myprice.short_description = 'Price'
    pub.short_description = 'Publisher Name'
    display_authors.short_description = 'Authors'

# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Store)