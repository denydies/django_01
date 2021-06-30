from account.models import User
from django.contrib import admin

from .models import Author, Book, Category, Comment, ContactUs, Post, Subscriber

"""admin"""

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Subscriber)
admin.site.register(Comment)
admin.site.register(ContactUs)
admin.site.register(User)
