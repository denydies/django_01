from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('about', views.about, name='about'),

    path('posts', views.posts, name='posts'),
    path('posts/create', views.post_create, name='posts_create'),
    # path('post/<int:post_id>', views.post_show, name='post_show'),  # НУЖНО РЕАЛИЗОВАТЬ
    # path('post/update/<int:post_id>', views.post_update, name='post_update'),  # НУЖНО РЕАЛИЗОВАТЬ

    path('subscribers', views.subscribers, name='subscribers'),
    path('subscriber/add', views.subscriber_add, name='subscriber_add'),
    # path('authors/new', views.authors_new, name='authors_new'),  # НУЖНО РЕАЛИЗОВАТЬ (FAKER)
    # path('authors/all', views.authors_all, name='authors_all'),  # НУЖНО РЕАЛИЗОВАТЬ

    path('api/posts', views.api_posts, name='api_posts'),
    # path('api/post/<int:post_id>', views.api_post_show, name='api_post_show'), # НУЖНО РЕАЛИЗОВАТЬ
    path('api/subscribe', views.api_subscribe, name='api_subscribe'),
    path('api/authors', views.api_authors, name='api_authors'),
    # path('api/authors/new', views.api_authors_new, name='api_authors_new'), # НУЖНО РЕАЛИЗОВАТЬ
]
