from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False)
    date_joined = models.DateField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    picture = models.ImageField()