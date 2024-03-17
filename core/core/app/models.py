from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='media/image', blank=True, null=True)
    file = models.FileField(upload_to='media/video', blank=True, null=True)
