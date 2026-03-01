# Shortcuts
from django.shortcuts import render,redirect,get_object_or_404

# Forms
from .forms import SearchForm,PostForm,RegisterForm,LoginForm

# Models
from .models import Post,Author,Category

# Authentication
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Message
from django.contrib import messages


def index(request):
    search_results = Post.objects.all()
    posts = Post.objects.order_by('-id')

    if request.method == "POST":
        search_form = SearchForm(request.POST)

        if search_form.is_valid():
            search_title = search_form.cleaned_data.get("search_title")

            if search_title:
                search_results = Post.objects.filter(
                    title__icontains=search_title
                )

        # return partial for AJAX
        return render(
            request,
            "results_partial.html",
            {"search_results": search_results}
        )

    # Normal page load
    search_form = SearchForm()

    return render(request, "index.html", {
        "search_form": search_form,
        "search_results": search_results,
        "posts" : posts,
    })


# Dashboard Views

@login_required
def dashboard(request):
    user = request.user
    author = get_object_or_404(Author,user=user)
    posts = Post.objects.filter(author=author)

    context = {
        "user" : user,
        "author" : author,
        "posts" : posts,
    }

    return render(request,"dashboard/index.html",context)


@login_required
def create_post(request):
    post_form = PostForm()
    user = request.user
    if request.method == "POST":
        post_form = PostForm(request.POST)
        
        if post_form.is_valid():
            post = post_form.save(commit=False)
            author = Author.objects.get(user=request.user)
            post.author = author
            post.save()
            post_form.save_m2m()
            return redirect("index")
    context = {
        "post_form" : post_form,
        "user" : user,
    }
    return render(request,"dashboard/create-post.html",context)

@login_required
def profile(request):
    user = request.user
    author = Author.objects.get(user__username=user.username)
    context = {
        "user" : user,
        "author" : author
    }
    return render(request,"dashboard/profile.html",context)

def authors(request):
    authors = Author.objects.all()
    context = {
        "authors" : authors
    }
    return render(request,"pages/auth_main.html",context)

def categories(request):
    categories = Category.objects.all()
    context = {
        "categories" : categories
    }
    return render(request,"pages/cat_main.html",context)

def author_page(request,slug):
    author = get_object_or_404(Author,slug=slug)
    posts = Post.objects.filter(author=author)

    context = {
        "author" : author,
        "posts" : posts,
    }

    return render(request,"pages/author_page.html",context)

def category_page(request,slug):
    category = get_object_or_404(Category,slug=slug)
    posts = Post.objects.filter(category=category)

    context = {
        "category" : category,
        "posts" : posts,
    }

    return render(request,"pages/category_page.html",context)

# @login_required
# def delete(request, slug):
#     post = get_object_or_404(Post, slug=slug)
    
#     if request.user != post.author:
#         return redirect("index") 
    
#     if request.method == "POST":
#         post.delete()
#         return redirect("dashboard")
    
#     return redirect("dashboard")
    

@login_required
def delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.user == post.author.user: 
        if request.method == "POST":
            post.delete()
            return redirect("dashboard")
    else:

        return redirect("index")
    
    return redirect("dashboard")


# Accounts

def login_view(request):
    login_form = LoginForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]   

            user = authenticate(username=username,password=password)

            if user:
                login(request,user)
                messages.success(request,"Login Successfull",extra_tags="login_success")
                return redirect("dashboard")
            else:
                messages.success(request,"Login Failed, Check Credentials",extra_tags="login_error")


    context = {
        "login_form" : login_form,
    }
    return render(request,"accounts/login.html",context)


def logout_view(request):
    logout(request)
    return redirect("index")


def register_author_view(request):
    register_form = RegisterForm()

    if request.method == "POST":
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():

            a_username = register_form.cleaned_data["username"]
            first_name = register_form.cleaned_data["first_name"]
            last_name = register_form.cleaned_data["last_name"]
            password = register_form.cleaned_data["password"]
            country = register_form.cleaned_data["country"]
            profile_picture = register_form.cleaned_data["profile_picture"]

            if User.objects.all().filter(username__exact=a_username).exists():
                messages.error(request,"Username already Exists, Please choose another Username",extra_tags="username_exist_error")
            else:
                author_user = User.objects.create_user(username=a_username,first_name=first_name,last_name=last_name,password=password)
                author = Author.objects.create(user=author_user,country=country,profile_picture=profile_picture)
                login(request,author_user)
                messages.success(request,"User Created Successfully",extra_tags="register_author_success")

    context = {
        "register_form" : register_form,
    }
    return render(request,"accounts/register.html",context)

# Single Post View

def single_post(request,slug):
    blog_post = get_object_or_404(Post,slug=slug)
    categories = blog_post.category.all()
    context = {
        "blog_post" : blog_post,
        "categories" :categories,
    }
    return render(request,"dashboard/singlepost.html",context)
