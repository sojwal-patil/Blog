from django.shortcuts import render,redirect
from .forms import AuthorForm,BlogForm
from .models import Author,BlogPost
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,"index.html")

def dashboard(request):
    blogposts = BlogPost.objects.all()
    context = {
        "blogposts" : blogposts
    }
    return render(request,"dash.html",context)

def newpost(request):
    blog_form = BlogForm()
    if request.method == "POST":
        blog_form = BlogForm(request.POST)
        if blog_form.is_valid():
            blog_form.save()
    context = {
        "blog_form" : blog_form
    }
    return render(request,"newpost.html",context)\
    