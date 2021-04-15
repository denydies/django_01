from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('about', views.about, name='about'),
    path('posts', views.posts, name='posts'),
    path('posts/create', views.post_create, name='posts_create'),
    path('subscribers', views.subscribers, name='subscribers'),
    path('subscriber/add', views.subscriber_add, name='subscriber_add'),

    path('api/posts', views.api_posts, name='api_posts'),
    path('api/subscribe', views.api_subscribe, name='api_subscribe'),
    path('api/author', views.api_author, name='api_author'),
]
