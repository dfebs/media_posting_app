from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    date_joined = models.DateField(auto_now_add=True)

class UserFollowing(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                    related_name='following', 
                                    on_delete=models.CASCADE)
    following = models.ForeignKey(settings.AUTH_USER_MODEL, 
                                    related_name='followers',
                                    on_delete=models.CASCADE)

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='pfp')