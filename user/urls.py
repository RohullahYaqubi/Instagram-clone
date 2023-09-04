from django.urls import path

from .views import  profile_view, profile_list, profile_detail, profile_edit_view

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('profile_list/', profile_list, name='profile_list'),
    path('profile_detail/<int:pk>/', profile_detail, name='profile_detail'),
    path('profile/edit', profile_edit_view, name='profileedit')
]
