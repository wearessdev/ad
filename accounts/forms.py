from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SSUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = SSUser
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = SSUser
        fields = '__all__'