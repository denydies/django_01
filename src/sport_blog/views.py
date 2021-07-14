import csv

from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView
from faker import Faker

from .forms import CommentForm, PostForm, SubscriberForm

from .models import Author, Book, Category, Comment, ContactUs, Post, Subscriber

# from .post_service import post_all, post_find
# from .subscribe_service import subscribe
from .tasks import noyify_async


# def index(request):
#     return render(request, 'sport_blog/index.html')

# def about(request):
#     return render(request, 'sport_blog/about.html', {"title": "About company"})x

# def posts(request):
#     posts = Post.objects.all()
#     return render(request, 'sport_blog/posts.html', {"title": "Posts", "posts": posts})


def post_create(request):
    err = ""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
        else:
            err = 'Error on save Post'
    else:
        form = PostForm()
    context = {
        'form': form,
        'err': err
    }
    return render(request, 'sport_blog/post_create.html', context=context)


def post_show(request, post_id):
    post = post_find(post_id)
    return render(request, 'sport_blog/post_show.html', {"title": post.title, "post": post})


def post_update(request, post_id):
    err = ""
    pst = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(instance=pst, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
        else:
            err = 'Error on update Post'
    else:
        form = PostForm(instance=pst)
    context = {
        'form': form,
        'err': err
    }
    return render(request, 'sport_blog/post_update.html', context=context)


def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return render(request, 'sport_blog/posts_list.html')


def comments(request):
    all_comments = Comment.objects.all()
    return render(request, 'sport_blog/comments.html', {"title": "Comments", "comments": all_comments})


def comment_create(request):
    err = ""
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments')
        else:
            err = 'Ошибка при сохранении комментария'
    else:
        form = CommentForm()
    context = {
        'form': form,
        'err': err
    }
    return render(request, 'sport_blog/comment_create.html', context=context)


def subscribers(request):
    subs = Subscriber.objects.all()
    return render(request, 'sport_blog/subscribers.html', {"title": "Subscribers", "subs": subs})


# функция должна быть тонкой( логику  перенести в СЕРВИСЫ)
def subscriber_add(request):
    error = ""
    subscribe_success = False
    email_to = request.POST.get('email_to')
    author_name = request.POST.get('author id')
    # author_id = request.POST.get('author_id')
    # author_name = Author.objects.get(id=author_id)

    if request.method == "POST":
        form = SubscriberForm(request.POST)  # ВЫТАЩИТЬ В ОТДВВЕЛЬНЫЙ СЕРВИС
        try:
            if form.is_valid():  # ВЫТАЩИТЬ В ОТДВВЕЛЬНЫЙ СЕРВИС
                form.save()  # ВЫТАЩИТЬ В ОТДВВЕЛЬНЫЙ СЕРВИС
                # return redirect('subscribers')  # ВЫТАЩИТЬ В ОТДВВЕЛЬНЫЙ СЕРВИС
                subscribe_success = True
            else:
                error = form.errors
        except ValidationError:
            error = 'Already subscribed'
    else:
        form = SubscriberForm()

    if subscribe_success:
        noyify_async.delay(email_to, author_name)
        return redirect('subscribers')

    context = {
        'form': form,
        'err': error
    }
    return render(request, 'sport_blog/subscribe_add.html', context=context)


def authors_new(request):
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    return redirect('authors_all')


def authors_all(request):
    authors = Author.objects.all().prefetch_related('books')
    context = {
        "title": "Authors",
        "authors": authors,
    }
    return render(request, 'sport_blog/authors.html', context)


def books_all(request):
    books = Book.objects.all().only('id', 'title', 'author__name').select_related('author')
    context = {
        "title": "Books",
        "books": books
    }
    return render(request, 'sport_blog/books.html', context)


def categories_all(request):
    categories = Category.objects.all().only('name')
    context = {
        "title": "Categories",
        "categories": categories
    }
    return render(request, 'sport_blog/categories.html', context)


# API

def api_posts(request):
    every = Post.objects.all()
    data = list(every.values())

    return JsonResponse(data, safe=False)


def api_comments(request):
    all_comments = Comment.objects.all()
    data = list(all_comments.values())

    return JsonResponse(data, safe=False)


def api_subscribe(request):
    sup = Subscriber.objects.all()
    data = list(sup.values())

    return JsonResponse(data, safe=False)


def api_authors(request):
    all_authors = Author.objects.all()
    data = list(all_authors.values())

    return JsonResponse(data, safe=False)


def api_fake_authors(request):
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    all_fake_authors = Author.objects.all().values('name', 'email')
    return JsonResponse(list(all_fake_authors), safe=False)


# Вспомагательные функции

def post_find(post_id: int) -> Post:
    return Post.objects.get(id=post_id)


# Классовые вью


# class BooksListView(ListView):
#     queryset = Book.objects.all()


class PostsListView(ListView):
    queryset = Post.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['cnt'] = context['object_list'].count()
        context['title'] = 'Все посты'
        return context

    template_name = 'sport_blog/posts_list.html'


class ContactUsListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'sport_blog/contact-us-list.html'


class ContactUsView(CreateView):
    success_url = reverse_lazy('contact-us-list')
    model = ContactUs
    fields = ('email', 'subject', 'message')


def display_attr(obj, atrr: str):
    get_display = f'get_{atrr}_display'
    if hasattr(obj, get_display):
        return getattr(obj, get_display)()

    return getattr(obj, atrr)


class PostXLSX(View):
    headers = ['title']
    filename = 'posts_all_list.xlsx'

    def get(self, request, *args, **kwargs):
        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
            headers={'Content-Disposition': f'attachment; filename="{self.filename}"'},
        )

        writer = csv.writer(response)

        writer.writerow(self.headers)
        for post in Post.objects.all().iterator():
            writer.writerow([display_attr(post, header) for header in self.headers])

        return response
