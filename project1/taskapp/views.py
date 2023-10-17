
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

#client side validation of data
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(min_value=1,max_value=5)

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
        "form" : form

            })
        
    return render(request,"taskapp/add.html",{
        "form" : NewTaskForm()
    })

