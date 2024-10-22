# home/models.py
from django.db import models
from cloudinary.models import CloudinaryField  # To use Cloudinary for image storage (if needed)
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # The admin who posts the news
    headline = models.CharField(max_length=255)  # News headline
    content = RichTextField()  # News content (you can use CKEditor here if you want rich text)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', blank=True, null=True)  # Optional image for the news post

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.headline
