from django.db import models
from django.utils.timezone import now


class Author(models.Model):
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    name = models.CharField('Имя автора', max_length=100)
    email = models.EmailField('Email автора', max_length=50)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"

    email_to = models.EmailField("Email подписчика")
    author_id = models.ForeignKey("Author", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)


    def __str__(self):
        return self.email_to


class Post(models.Model):
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    title = models.CharField('Заголовок', max_length=150)
    description = models.CharField('Краткое описание', max_length=250)
    content = models.TextField('Статья')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.title
