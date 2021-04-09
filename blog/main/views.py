from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm
from .models import Post
# from .notify_service import notify
# from  .post_service import
# from .subscribe_service import subscriber


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html', {"title": "About company"})


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


def api_posts(request):
    every = Post.objects.all()
    data = list(every.values())

    return JsonResponse(data, safe=False)


# def api_subscribe(request):
#     author_id = request.GET['author_id']
#     email_to = request.GET['email_to']

    # get_object_or_404(Author, pk=author_id)
    #
    # subscribe_process(author_id, email_to)

    # data = {'author_id': author_id}
    # return JsonResponse(data, safe=False)

#
# def subscribe(request):
#     author_id = request.GET['author_id']
#     email_to = request.GET['email_to']
#
#     subscribe_process(author_id, email_to)
#
#     return render(request, 'main/subscribe.html', context=context)
#
#
# def subscribe_process(author_id, email_to):
#     subscribe(author_id, email_to)
#     # notify(email_to)
