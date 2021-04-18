from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from faker import Faker

from .forms import PostForm, SubscriberForm
from .models import Post, Author, Subscriber


# def index(request):
#     return render(request, 'main/index.html')


# def about(request):
#     return render(request, 'main/about.html', {"title": "About company"})


def posts(request):
    posts = Post.objects.all()
    return render(request, 'main/post.html', {"title": "Posts", "posts": posts})


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


def subscribers(request):
    subs = Subscriber.objects.all()
    return render(request, 'main/subscribers.html', {"title": "Subscribers", "subs": subs})


# функция должна быть тонкой( логику  перенести в СЕРВИСЫ)
def subscriber_add(request):
    error = ""
    if request.method == "POST":
        form = SubscriberForm(request.POST)  # ВЫТАЩИТЬ В ОТДВВЕЛЬНЫЙ СЕРВИС
        if form.is_valid():  # ВЫТАЩИТЬ В ОТДВВЕЛЬНЫЙ СЕРВИС
            form.save()  # ВЫТАЩИТЬ В ОТДВВЕЛЬНЫЙ СЕРВИС
            return redirect('subscribers')  # ВЫТАЩИТЬ В ОТДВВЕЛЬНЫЙ СЕРВИС
        else:
            error = 'Error on save Subscribe'
    else:
        form = SubscriberForm()
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
