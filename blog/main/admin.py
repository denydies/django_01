from django.contrib import admin

from .models import Author, Post, Subscriber, Comment

"""admin"""

admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Subscriber)
admin.site.register(Comment)
