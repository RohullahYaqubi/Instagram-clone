from django.shortcuts import render
from .models import Post

def home_page(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }

    return render(request, 'home.html', context)