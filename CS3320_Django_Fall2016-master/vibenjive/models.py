from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class VibenjiveUser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    zipcode = models.CharField(max_length=5)
    genres = models.CharField(max_length=100)
    instruments = models.CharField(max_length=100)

    def __str__(self):
        return self.username

    class Admin:
        pass

class UserMusic(models.Model):
    song_id = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=30)
    title = models.CharField(max_length=256, default="None")
    genres = models.CharField(max_length=30, default="None")
    instruments = models.CharField(max_length=30)
    url = models.CharField(max_length=256)
    zipcode = models.CharField(max_length=5)
