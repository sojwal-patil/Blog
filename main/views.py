from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
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
            return redirect("dashboard")
    context = {
        "blog_form" : blog_form
    }
    return render(request,"newpost.html",context)

@require_POST    
def delete(request,id):
    post = get_object_or_404(BlogPost,pk=id)
    post.delete()
    return redirect("dashboard")

def singlepost(request,slug):
    post = get_object_or_404(BlogPost,slug=slug)
    context = {
        "post" : post
    }
    return render(request,"singlepost.html",context)