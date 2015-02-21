__author__ = 'windoo'

from django import forms
from Forum.models import *


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