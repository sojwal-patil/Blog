from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(unique=True,max_length=250,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category)
        super().save(*args, **kwargs)    

    def __str__(self):
        return self.category

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=250,blank=True)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    contains = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True,max_length=250,blank=True)
    date = models.DateField(auto_now_add=True)
    contains = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=50,unique=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,max_length=250,blank=True)
    date_of_birth = models.DateField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name 