from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),


    # CRUD
    path("create-post/", views.create_post, name="create-post"),
    path("delete/<slug:slug>",views.delete,name="delete"),

    # Accounts
    path("accounts/register/", views.register_author_view, name="register"),
    path("accounts/login/",views.login_view,name="login"),
    path("accounts/logout/",views.logout_view,name="logout"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("dashboard/profile",views.profile,name="profile"),

    # Author Slug
    path("authors/",views.authors,name="authors"),
    path("categories/",views.categories,name="categories"),

    path("author/<slug:slug>",views.author_page,name="author_page"),

    # Category Slug
    path("category/<slug:slug>",views.category_page,name="category_page"),

    # Single Post 
    path("post/<slug:slug>/",views.single_post,name="single_post"),

]