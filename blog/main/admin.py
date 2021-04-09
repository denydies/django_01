from django.contrib import admin

from .models import Author, Post

"""admin"""

admin.site.register(Post)
admin.site.register(Author)
