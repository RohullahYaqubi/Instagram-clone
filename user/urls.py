from django.urls import path

from .views import homepage, profile_view, profile_list, profile_detail

urlpatterns = [
    path('', homepage, name='home'),
    path('profile/', profile_view, name='profile'),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile_detail/<int:pk>/', profile_detail, name='profile_detail')
]
