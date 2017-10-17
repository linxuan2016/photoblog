from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import *


def post(request, p_id):
    context = {}
    post = get_object_or_404(Post, pk=p_id)
    try:
        previous_post = post.get_next_by_date()
    except Post.DoesNotExist:
        previous_post = None

    try:
        next_post = post.get_previous_by_date()
    except Post.DoesNotExist:
        next_post = None

    context["post"] = post
    context["next_post"] = next_post
    context["previous_post"] = previous_post

    return render(request, "post.html", context)


def category(request, c_id):
    context = {}
    category = Category.objects.get(pk=c_id)
    categories = Category.objects.all()
    context["category"] = category
    context["catiegories"] = categories
    
    posts = Post.objects.filter(category=category)
    context["posts"] = posts

    return render(request, "category.html", context)

def blog(request):
    context = {}
    posts = Post.objects.all().order_by('-date')[:10]
    context["posts"] = posts
    return render(request, "blog.html", context)


