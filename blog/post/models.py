from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post Model Definition"""
    title = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
