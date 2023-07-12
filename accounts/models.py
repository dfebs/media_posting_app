from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False)
    # TODO add a date joined
    # TODO add profile pic