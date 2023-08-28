from django.shortcuts import render
from .models import Profile

def homepage(request):
    return render(request, 'home.html')

def profile_view(request):
    user_profile = Profile.objects.get(user= request.user)

    context={
        'profile':user_profile
    }
    return render(request, 'profile.html', context)


# Create your views here.
