
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

#client side validation of data
class NewTaskForm(forms.Form):
    task = forms.CharField(label="Add Task\n")

class RemoveTaskForm(forms.Form):
    task = forms.CharField(label="Remove Task\n")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    else:
        request.session["tasks"]


    return render(request,"taskapp/index.html",{
        "tasks" :request.session["tasks"]
        })

def add(request):

    # server side validation
    if request.method == 'POST':
        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("taskapp:index"))
        else:
            return render(request,"taskapp/add.html",{
        "form" : form.capitalize()
            })
        
    return render(request,"taskapp/add.html",{
        "form" : NewTaskForm()
    })


def remove(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            if task in request.session["tasks"]:
                request.session["tasks"].remove(task)
                request.session.modified = True  # Save changes to the session
            return HttpResponseRedirect(reverse("taskapp:index"))
        else:
            return render(request, "taskapp/add.html", {
                "form": form
            })
    return render(request, "taskapp/remove.html", {
        "form": RemoveTaskForm()
    })

# def play(request):

#     musics = [
#         "hillsong.mp3",
#         "Notafraid.mp3",
#         "overcome.mp3",
#         "Shemipeace.mp3",
#         "Theecember.mp3"
#     ]

#     return render(request,"taskapp/play.html",{
#         "musics" :musics
#     })


