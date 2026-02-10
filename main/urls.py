from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("dashboard/new-post",views.newpost,name="newpost"),
    path("dashboard/new-post/delete/<int:id>",views.delete,name="delete"),
    path("<slug:slug>",views.singlepost,name="singlepost")
]
