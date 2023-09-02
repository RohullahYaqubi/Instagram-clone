from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    caption = models.TextField(default="", max_length=400)
    image = models.ImageField(upload_to='static/posts', blank=False)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

# Create your models here.
