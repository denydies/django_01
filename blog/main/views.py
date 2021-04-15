from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404

from .forms import PostForm, SubscriberForm
from .models import Post, Author, Subscriber
# from blog.main.subscribe_service import subs_add




def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html', {"title": "About company"})


def posts(request):
    posts = Post.objects.all()
    return render(request, 'main/post.html', {"title": "Posts", "posts": posts})


def subscribers(request):
    subs = Subscriber.objects.all()
    return render(request, 'main/subscribers.html', {"title": "Subscribers", "subs": subs})


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


# функция должна быть тонкой( логику  перенести в СЕРВИСЫ)
def subscriber_add(request):
    error = ""
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subscribers')
        else:
            error = 'Error on save Subscribe'
    else:
        form = SubscriberForm()
    context = {
        'form': form,
        'err': error
    }
    return render(request, 'main/subscribe_add.html', context=context)


def api_posts(request):
    every = Post.objects.all()
    data = list(every.values())

    return JsonResponse(data, safe=False)


def api_subscribe(request):
    sup = Subscriber.objects.all()
    data = list(sup.values())

    return JsonResponse(data, safe=False)


def api_authors(request):
    all = Author.objects.all()
    data = list(all.values())

    return JsonResponse(data, safe=False)
