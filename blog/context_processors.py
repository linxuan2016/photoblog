from .models import Post


def blog_home(request):
    #context = {}
    #posts = Post.objects.all().order_by('-date')[:4]

    #context["posts"] = posts

    #return render(request, "home.html", context)

    return {'posts': Post.objects.all().order_by('-date')[:4],
            'request': request}

