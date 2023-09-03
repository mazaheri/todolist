from urllib import request

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    user = models.ForeignKey(User, related_name='category', on_delete=models.CASCADE)
    title = models.CharField(max_length=70)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = 'Categories'

class Task(models.Model):
    user = models.ForeignKey(User, related_name='task', on_delete=models.CASCADE)
    title = models.CharField(max_length=70)
    description = models.TextField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False)
    category = models.ForeignKey(Category, related_name='task', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
