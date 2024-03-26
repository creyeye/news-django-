from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media/image', blank=True, null=True)
    file = models.FileField(upload_to='media/video', blank=True, null=True)
