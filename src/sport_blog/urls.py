from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators import cache
from django.views.generic import RedirectView, TemplateView

from . import views

urlpatterns = [
    # path('', views.index, name='home_page'),
    # path('about', views.about, name='about'),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/sport_blog/static/assets/img/favicon/favicon.ico')),

    path('', TemplateView.as_view(template_name='sport_blog/index.html'), name='home_page'),
    path('about/', TemplateView.as_view(template_name='sport_blog/about.html'), name='about'),
    # path('posts/', views.posts, name='posts'),
    # path('posts/', cache.cache_page(60 * 2)(views.posts), name='posts'),
    path('posts/list/', views.PostsListView.as_view(), name='posts_list'),
    path('posts/list/csv/', views.PostXLSX.as_view(), name='posts_list_csv'),
    path('posts/create/', views.post_create, name='posts_create'),
    path('post/<int:post_id>/', views.post_show, name='post_show'),
    path('post/update/<int:post_id>/', views.post_update, name='post_update'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'),
    path('comments/', views.comments, name='comments'),
    path('comment/create/', views.comment_create, name='comment_create'),

    path('subscribers/', views.subscribers, name='subscribers'),
    path('subscriber/add/', views.subscriber_add, name='subscriber_add'),
    path('authors/new/', views.authors_new, name='authors_new'),
    # path('authors/all/', views.authors_all, name='authors_all'),
    path('authors/all/', cache.cache_page(60 * 2)(views.authors_all), name='authors_all'),

    path('books/all/', views.books_all, name='books_all'),
    path('categories/all/', views.categories_all, name='categories_all'),

    path('api/posts/', views.api_posts, name='api_posts'),
    path('api/subscribe/', views.api_subscribe, name='api_subscribe'),
    path('api/authors/', views.api_authors, name='api_authors'),
    path('api/authors/new/', views.api_fake_authors, name='api_authors_new'),
    path('api/comments/', views.api_comments, name='api_api_comments'),

    path('contact/us/create/', views.ContactUsView.as_view(), name='contact-us-create'),
    path('contact/us/list/', views.ContactUsListView.as_view(), name='contact-us-list'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
