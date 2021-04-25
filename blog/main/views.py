from time import sleep, time
from django.core.exceptions import ValidationError
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from faker import Faker

from .forms import PostForm, SubscriberForm, CommentForm
from .models import Post, Author, Subscriber, Comment
from .services import notify_service
# from .post_service import post_all, post_find
# from .subscribe_service import subscribe
from .tasks import noyify_async


# def index(request):
#     return render(request, 'main/index.html')


# def about(request):
#     return render(request, 'main/about.html', {"title": "About company"})x


def comments(request):
    all = Comment.objects.all()
    return render(request, 'main/comments.html', {"title": "Comments", "comments": all})


def posts(request):
    posts = Post.objects.all()
    return render(request, 'main/posts.html', {"title": "Posts", "posts": posts})


def post_create(request):
    err = ""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            err = 'Error on save Post'
    else:
        form = PostForm()
    context = {
        'form': form,
        'err': err
    }
    return render(request, 'main/post_create.html', context=context)


def post_show(request, post_id):
    post = post_find(post_id)
    return render(request, 'main/post_show.html', {"title": post.title, "post": post})
    pass


def post_update(request, post_id):
    err = ""
    pst = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(instance=pst, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            err = 'Error on update Post'
    else:
        form = PostForm(instance=pst)
    context = {
        'form': form,
        'err': err
    }
    return render(request, 'main/post_update.html', context=context)


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
    return render(request, 'main/comment_create.html', context=context)


def subscribers(request):
    subs = Subscriber.objects.all()
    return render(request, 'main/subscribers.html', {"title": "Subscribers", "subs": subs})


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
    return render(request, 'main/subscribe_add.html', context=context)


def authors_new(request):
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    return redirect('authors_all')


def authors_all(request):
    authors = Author.objects.all()
    return render(request, 'main/authors.html', {"title": "Authors", "authors": authors})


def api_posts(request):
    every = Post.objects.all()
    data = list(every.values())

    return JsonResponse(data, safe=False)


def api_comments(request):
    all = Comment.objects.all()
    data = list(all.values())

    return JsonResponse(data, safe=False)


def api_post_show(request):
    pass


def api_subscribe(request):
    sup = Subscriber.objects.all()
    data = list(sup.values())

    return JsonResponse(data, safe=False)


def api_authors(request):
    all = Author.objects.all()
    data = list(all.values())

    return JsonResponse(data, safe=False)


def api_authors_new(request):
    faker = Faker()
    Author(name=faker.name(), email=faker.email()).save()
    all = Author.objects.all().values('name', 'email')
    return JsonResponse(list(all), safe=False)


# вспомагательные функции

def post_find(post_id: int) -> Post:
    return Post.objects.get(id=post_id)
