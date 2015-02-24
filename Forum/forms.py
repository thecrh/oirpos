# -*- coding: utf-8 -*-

__author__ = 'windoo'

import re

from django import forms
from Forum.models import *
from django.core.exceptions import ObjectDoesNotExist

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('title', 'body')


class TopicForm(forms.ModelForm):
    # title = forms.CharField(max_length=60, required=True)
    # description = forms.CharField(max_length=10000, required=True)

    class Meta():
        model = Topic
        fields = ('title', 'description')

class RegisterForm(forms.Form):
    username = forms.CharField(label="Login:",max_length=30)
    password1 = forms.CharField(label="Hasło:",widget=forms.PasswordInput())
    password2 = forms.CharField(label="Powtórz hasło:",widget=forms.PasswordInput())

    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1==password2:
            return password2
        else:
            raise forms.ValidationError("Hasła są różne")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$',username):
            raise forms.ValidationError("Login zawiera niedozwolone znaki")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Taki użytkownik już istnieje")
