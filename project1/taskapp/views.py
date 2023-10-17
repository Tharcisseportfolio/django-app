from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

tasks = ["Eat","Study","Play","Party","Visit"]
def index(request):
    return render(request,"taskapp/index.html",{
        "tasks" :tasks
        })

def add(request):

    return render(request,"taskapp/add.html")