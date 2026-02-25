from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    country = models.CharField(max_length=30)

class Category(models.Model):
    category = models.CharField(max_length=20)
    slug = models.SlugField(unique=True,max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.OneToOneField(Author,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,max_length=50)

    def __str__(self):
        return self.title