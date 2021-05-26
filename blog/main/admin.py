from django.contrib import admin

from .models import Author, Post, Subscriber, Comment, ContactUs, Book, Category

"""admin"""

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Subscriber)
admin.site.register(Comment)
admin.site.register(ContactUs)
