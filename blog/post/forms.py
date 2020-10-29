"""Module that will contain all forms related to Post object"""
from django import forms
from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'is_published')
        labels = {
            "is_published": "Publish"
        }

