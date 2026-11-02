from django.shortcuts import get_object_or_404, render

from .models import Post


def lista(request):
    posts = Post.objects.filter(publicado=True)
    return render(request, 'blog/lista.html', {'posts': posts})


def detalhe(request, slug):
    post = get_object_or_404(Post, slug=slug, publicado=True)
    return render(request, 'blog/detalhe.html', {'post': post})
