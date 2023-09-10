from django.shortcuts import render
from django.db.models import Q
from .models import Profile
from posts.models import Post


def profile_view(request):
    if request.user.is_authenticated:
        user_profile = Profile.objects.get(user= request.user)
        post = Post.objects.filter(user = request.user)

        context={
            'profile':user_profile,
            'post':post
        }
        return render(request, 'profile.html', context)
    else:
        return render(request,'home.html')

def profile_list(request):
    if request.user.is_authenticated:

        query = request.GET.get('q')
        profiles = Profile.objects.exclude(user = request.user).filter(
            Q(user__emailaddress__user__username__icontains=query) | Q(user__emailaddress__user__first_name__icontains=query) |
            Q(user__emailaddress__user__last_name__icontains=query)
        )
        context={
            'profiles':profiles
        }
        return render(request,'profile_list.html', context)
    else:
        return render(request,'home.html')

def profile_detail(request, pk):
    if request.user.is_authenticated:

        profile = Profile.objects.get(user_id = pk) 
        myprofile = Profile.objects.get(user = request.user)
        post = Post.objects.filter(user_id = pk)

        if request.method == "POST":
            action = request.POST['followunfollow']
            if action == "unfollow":
                myprofile.follows.remove(profile)
            elif action == "follow":
                myprofile.follows.add(profile)
    
        context={
            'profile':profile,
            'myprofile':myprofile,
            'post':post
        }
        return render(request, 'profile_detail.html',context )
    else:
        return render(request,'home.html')

def profile_edit_view(request):
    return render(request, 'profile_edit.html')


