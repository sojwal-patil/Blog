from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Moderator(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    country = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user.username}"

class Category(models.Model):
    category = models.CharField(max_length=30)
    slug = models.SlugField(unique=True,max_length=20,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category
    

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextUploadingField()
    date = models.DateField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,max_length=50,blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title