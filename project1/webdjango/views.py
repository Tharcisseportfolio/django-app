from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"webdjango/web.html")


def brian(request):
    return HttpResponse("Hello, brian")

def david(request):
    return HttpResponse("Hello, david")

def greet(request,name):
    return render(request,"webdjango/greet.html",{"name":name.capitalize()})
