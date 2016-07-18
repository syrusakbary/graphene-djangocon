from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50)
    avatar = models.ImageField()


class Talk(models.Model):
    title = models.CharField(max_length=50)
    time = models.DateTimeField()
    speaker = models.ForeignKey(User, related_name='talks')

    def __str__(self):
        return self.title
