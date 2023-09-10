from django.urls import path
from .views import home_page, like_post, comment

urlpatterns = [
    path('', home_page, name='home'),
    path('<int:pk>/', like_post, name='post_like'),
    path('comment/<int:pk>/', comment, name='post_comment' ),
]
