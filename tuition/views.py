from django import forms
from django.shortcuts import render
from .models import Contact
from .forms import CantactForm

# Create your views here.
def contact(request):
    if request.method=="POST":
        form=CantactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CantactForm()
    return render(request,'contact.html',{'form':form})