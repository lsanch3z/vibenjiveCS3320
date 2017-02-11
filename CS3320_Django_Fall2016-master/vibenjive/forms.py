from vibenjive.models import VibenjiveUser, UserMusic
from django.contrib.auth.models import User
from django.forms.widgets import *
from django.forms import *
from django import forms
from django.forms import ModelForm
from django.db import models

class RegistrationForm(ModelForm):
    class Meta:
        model = VibenjiveUser
        fields = ['username', 'zipcode','genres','instruments']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class AddMusicForm(ModelForm):
    class Meta:
        model = UserMusic
        fields = ['username','title','genres','instruments','url']
