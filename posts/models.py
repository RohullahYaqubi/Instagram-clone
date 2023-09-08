from django.db import models
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
user = EmailAddress.user
class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    caption = models.TextField(default="", max_length=400)
    image = models.ImageField(upload_to='static/posts', blank=False)
    created_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(get_user_model(), related_name='post_like')
    

    def __str__(self):
        return str(self.pk)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)



