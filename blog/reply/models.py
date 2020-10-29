from django.db import models


# Create your models here.
from post.models import Post


class Reply(models.Model):
    """Reply Model Representation"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="replies", null=False)
    name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254)
    content = models.CharField(max_length=500, unique=True)
    created_on = models.DateField(auto_now=True)

    class Meta:
        ordering = ['created_on']
        verbose_name_plural = "Replies"

    def __str__(self):
        return self.name
