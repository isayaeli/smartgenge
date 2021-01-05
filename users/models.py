from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image', default='default.png')
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user}'s Profile"

def create_profile(sender, **kwargs):
    if kwargs['created']:
       profile = Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)