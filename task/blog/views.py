from django.shortcuts import render

from .models import Blogger, Post


def home_page(request):
    return render(request, 'blog/home_page.html')


def all_blog_posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/list_of_all_blog_posts.html', context)


def all_bloggers(request):
    bloggers = Blogger.objects.all()
    context = {'bloggers': bloggers}
    return render(request, 'blog/list_of_all_bloggers.html', context)

def practica(request):
    return render(request, 'blog/practica.html')



