from django.shortcuts import render
from blog.models import post, categorias

def blog(request):
    posts = post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def categoria(request, categoria_id):
    categoria_obj = categorias.objects.get(id=categoria_id)
    posts = post.objects.filter(categorias=categoria_obj)
    return render(request, "blog/categoria.html", {'categoria': categoria_obj, "posts": posts})