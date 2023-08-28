from django.urls import path

from .views import homepage, profile_view

urlpatterns = [
    path('', homepage, name='home'),
    path('profile/', profile_view, name='profile')
]
