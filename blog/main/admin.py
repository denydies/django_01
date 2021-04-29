from django.contrib import admin

from .models import Author, Post, Subscriber, Comment, ContactUs

"""admin"""

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Subscriber)
admin.site.register(Comment)
admin.site.register(ContactUs)
