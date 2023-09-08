from django.urls import path
from .views import home_page, like_post

urlpatterns = [
    path('', home_page, name='home'),
    path('<int:pk>/', like_post, name='post_like')
]
