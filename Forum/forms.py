__author__ = 'windoo'

from django import forms
from Forum.models import *


class ReplyForm(forms.Form):
    content = forms.CharField(max_length=10000)


class TopicForm(forms.ModelForm):

    title = forms.CharField(max_length=60, required=True)
    description = forms.CharField(max_length=10000, required=True)

    class Meta():
        model = Topic
        exclude = ('creator','updated', 'created', 'closed',)