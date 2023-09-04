from django.shortcuts import render

from .models import Post
from user.models import Profile

def home_page(request):
    posts = Post.objects.all()
    
    context = {
        'posts':posts,
    }
    return render(request, 'home.html', context)