from account.models import Avatar, User
from django.contrib import admin

from .models import Author, Book, Category, Comment, ContactUs, Post, Subscriber


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
    ]

    list_filter = [
        'title',
        'description',
    ]

    actions = None

    # readonly_fields = ['title', 'content']

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser or request.user.has_perm('sport_blog.post_edit_all'):
            return ()
        return super().get_readonly_fields(request, obj)


class BookAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'author',
        'category',
    ]

    list_filter = [
        'author',
        'category',
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Subscriber)
admin.site.register(Comment)
admin.site.register(ContactUs)
admin.site.register(User)
admin.site.register(Avatar)
