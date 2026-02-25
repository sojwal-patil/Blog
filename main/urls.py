from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("accounts/create_author", views.register_author_view, name="register_author"),
    path("accounts/login",views.login_view,name="login"),
    path("accounts/logout",views.logout_view,name="logout"),
    path("accounts/dashboard",views.dashboard,name="dashboard"),
]