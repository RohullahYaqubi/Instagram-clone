from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .models import Post, Comment
from user.models import Profile

def home_page(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        my_profile = Profile.objects.get(user = request.user)

        if request.method == "POST":
            comment = request.post.get('comment')

        context = {
            'posts':posts,
            'myprofile':my_profile
        }
        return render(request, 'home.html', context)
    else:
        return render(request,'home.html')


@login_required
def like_post(request, pk):
    post = Post.objects.get(id = pk)
    action = request.POST['likeunlike']

    if action == 'like':
        post.likes.add(request.user)
    else:
        post.likes.remove(request.user)
    
    return redirect('home')

def comment(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            comment_text = request.POST.get('comment')
            current_post = Post.objects.get(id=pk)

            comment = Comment(post=current_post, user=request.user, body=comment_text)
            comment.save()
        
        return redirect('home')
            