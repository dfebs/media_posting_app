from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField()
    text = models.TextField(max_length=50)

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    text = models.TextField(max_length=25)

class Reaction: # This should only be edited by admins
    image = models.ImageField()

class PostReaction:
    reactor = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey(Post)
    reaction = models.ForeignKey(Reaction)