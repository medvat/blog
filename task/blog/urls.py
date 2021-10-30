from django.urls import path

from .views import home_page, practica, all_blog_posts, all_bloggers

app_name = 'blog'

urlpatterns = [
    path('', home_page, name='home_page'),
    path('blogs/', all_blog_posts, name='all_blog_posts'),
    path('bloggers/', all_bloggers, name='all_bloggers'),
    path('practica/', practica, name='practica'),
]
