from django.shortcuts import render, redirect, get_list_or_404

from .models import Post, Comment
from user.models import Profile

def home_page(request):
    posts = Post.objects.all()
    my_profile = Profile.objects.get(user = request.user)
    
    context = {
        'posts':posts,
        'myprofile':my_profile
    }
    return render(request, 'home.html', context)


def like_post(request, pk):
    post = Post.objects.get(id = pk)
    action = request.POST['likeunlike']

    if action == 'like':
        post.likes.add(request.user)
    else:
        post.likes.remove(request.user)
    
    return redirect('home')