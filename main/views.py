# Shortcuts
from django.shortcuts import render,redirect

# Forms
from .forms import SearchForm,PostForm,RegisterForm,LoginForm

# Models
from .models import Post,Author

# Authentication
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Message
from django.contrib import messages

from django.shortcuts import render

def index(request):
    search_results = Post.objects.all()

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
    })


def single_post(request,slug):
    return render(request,"singlepost.html")


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

            if User.objects.all().filter(username__exact=a_username).exists():
                messages.error(request,"Username already Exists, Please choose another Username",extra_tags="username_exist_error")
            else:
                author_user = User.objects.create_user(username=a_username,first_name=first_name,last_name=last_name,password=password)
                author = Author.objects.create(user=author_user,country=country)
                login(request,author_user)
                messages.success(request,"User Created Successfully",extra_tags="register_author_success")

    context = {
        "register_form" : register_form,
    }
    return render(request,"register.html",context)



@login_required
def dashboard(request):
    return render(request,"dashboard.html")

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
    return render(request,"login.html",context)



def logout_view(request):
    logout(request)
    return redirect("index")



@login_required
def create(request):
    post_form = PostForm()
    user = request.user
    if request.method == "POST":
        post_form = PostForm(request.POST)
        
        if post_form.is_valid():
            post = post_form.save(commit=False)
            author = Author.objects.get(user=request.user)
            post.author = author
            post.save()
            return redirect("index")
    context = {
        "post_form" : post_form,
        "user" : user,
    }
    return render(request,"create.html",context)