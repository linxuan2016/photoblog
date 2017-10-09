from .models import Post


def blog_home(request):

    return {'posts': Post.objects.all().order_by('-date')[:4],
            'request': request}

