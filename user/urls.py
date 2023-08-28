from django.urls import path

from .views import homepage, profile_view, profile_list

urlpatterns = [
    path('', homepage, name='home'),
    path('profile/', profile_view, name='profile'),
    path('profile_list/', profile_list, name='profile_list')
]
