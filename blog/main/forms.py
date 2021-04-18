from django import forms
from django.forms import ModelForm, Textarea, TextInput, Select

from .models import Post, Subscriber, Author, Comment


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


class SubscriberForm(ModelForm):
    author_id = forms.ModelChoiceField(
        queryset=Author.objects.all().order_by('name'),
        empty_label='Выберите автора...',
        widget=forms.Select(attrs={
            "class": "form-control",
        }),
    )

    class Meta:
        model = Subscriber
        fields = ["email_to", "author_id"]
        widgets = {
            "email_to": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Email подписчика",
            }),
            # "author_id": Select(attrs={
            #     "class": "form-control",
            #     "placeholder": "ID автора",
            # })
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": Textarea(attrs={
                "class": "form-control",
                "placeholder": "Введите комментарий",
            })
        }