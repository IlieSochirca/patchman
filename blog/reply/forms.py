"""Module that will contain all forms related to Reply object"""
from django import forms
from .models import Reply


class ReplyCreateForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('name', 'email', 'content')