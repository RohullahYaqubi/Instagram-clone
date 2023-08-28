from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/img', blank=True, null=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    hobbi = models.CharField(max_length=50, null= True, blank=True)
    occupassion = models.CharField(max_length=250, null=True, blank=True)
    live_in = models.CharField(max_length=250, null= True, blank=True)


    def __str__(self):
        return self.user.username
    
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()

post_save.connect(create_profile, sender=get_user_model())

    

