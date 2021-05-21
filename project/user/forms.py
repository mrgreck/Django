from django.forms import ModelForm, BooleanField
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group



# Создаём модельную форму
class BaseRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "password1",
                  "password2",)

    def save(self):
        user = super(BaseRegisterForm, self).save()
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user


