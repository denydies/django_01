from django.forms import ModelForm, Textarea, TextInput

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "content"]
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название поста",
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Краткое описание",
            }),
            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Содержимое",
            })
        }

#
# class SubscriberForm(ModelForm):
#     class Meta:
#         model = Subscriber
#         fields = ["author_to", "email_to"]
#         widgets = {
#             "author_to": TextInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "Id автора",
#             }),
#             "email_to": TextInput(attrs={
#                 "class": "form-control",
#                 "placeholder": "Email подписчика",
#             })
#         }
