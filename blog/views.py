from django.shortcuts import render
from .models import *


def post(request, p_id):
    context = {}
    post = Post.objects.get(pk=p_id)
    context["post"] = post

    return render(request, "post.html", context)


def category(request, c_id):
    context = {}
    category = Category.objects.get(pk=c_id)
    categories = Category.objects.all()
    context["category"] = category
    context["categories"] = categories
    
    posts = Post.objects.filter(category=category)
    context["posts"] = posts

    return render(request, "category.html", context)

def blog(request):
    context = {}
    posts = Post.objects.all().order_by('-date')[:5]

    context["posts"] = posts

    return render(request, "blog.html", context)
