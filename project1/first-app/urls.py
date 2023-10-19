
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("webdjango/",include("webdjango.urls")),
    path("taskapp/",include("taskapp.urls")),
    path("newyear/",include("newyear.urls")) 
    
]
