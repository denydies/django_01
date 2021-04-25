from django.conf.urls import url
from django.urls import path
from django.views.generic import TemplateView, RedirectView

from . import views

urlpatterns = [
    # path('', views.index, name='home_page'),
    # path('about', views.about, name='about'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/main/static/assets/img/favicon/favicon.ico')),

    path('', TemplateView.as_view(template_name='main/index.html'), name='home_page'),
    path('about/', TemplateView.as_view(template_name='main/about.html'), name='about'),

    path('posts/', views.posts, name='posts'),
    path('posts/create/', views.post_create, name='posts_create'),
    path('post/<int:post_id>/', views.post_show, name='post_show'),
    path('post/update/<int:post_id>/', views.post_update, name='post_update'),
    path('comments/', views.comments, name='comments'),
    path('comment/create/', views.comment_create, name='comment_create'),

    path('subscribers/', views.subscribers, name='subscribers'),
    path('subscriber/add/', views.subscriber_add, name='subscriber_add'),
    path('authors/new/', views.authors_new, name='authors_new'),
    path('authors/all/', views.authors_all, name='authors_all'),

    path('api/posts/', views.api_posts, name='api_posts'),
    path('api/post/<int:post_id>/', views.api_post_show, name='api_post_show'),
    path('api/subscribe/', views.api_subscribe, name='api_subscribe'),
    path('api/authors/', views.api_authors, name='api_authors'),
    path('api/authors/new/', views.api_authors_new, name='api_authors_new'),
    path('api/comments/', views.api_comments, name='api_api_comments'),

]
