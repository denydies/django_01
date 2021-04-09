from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('about', views.about, name='about'),
    path('posts', views.posts, name='posts'),
    path('posts/create', views.post_create, name='posts_create'),

    path('api/posts', views.api_posts, name='api_posts'),
    # path('api/subscribe', views.api_subscribe, name='api_subscribe'),
]
