from django.urls import path
from . import views

app_name = "taskapp"
urlpatterns = [
    path("",views.index, name = "index"),
    path("add",views.add, name = "add"),
    path("remove",views.remove, name = "remove"),
    path("play", views.play, name="play"),
]
