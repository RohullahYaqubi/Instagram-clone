from django.shortcuts import render
from django.db.models import Q
from .models import Profile


def profile_view(request):
    user_profile = Profile.objects.get(user= request.user)

    context={
        'profile':user_profile
    }
    return render(request, 'profile.html', context)

def profile_list(request):
    query = request.GET.get('q')
    profiles = Profile.objects.exclude(user = request.user).filter(
        Q(user__emailaddress__user__username__icontains=query) | Q(user__emailaddress__user__first_name__icontains=query) |
        Q(user__emailaddress__user__last_name__icontains=query)
    )
    context={
        'profiles':profiles
    }
    return render(request,'profile_list.html', context)

def profile_detail(request, pk):
    profile = Profile.objects.get(user_id = pk) 
    myprofile = Profile.objects.get(user = request.user)

    if request.method == "POST":
        action = request.POST['followunfollow']
        if action == "unfollow":
            myprofile.follows.remove(profile)
        elif action == "follow":
            myprofile.follows.add(profile)
   
    context={
        'profile':profile,
        'myprofile':myprofile
    }
    return render(request, 'profile_detail.html',context )


# Create your views here.
