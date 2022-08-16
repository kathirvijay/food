from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import Regform
# Create your views here.

def register(request):
    if request.method=="POST":
        form = Regform(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get("username")
            messages.success(request,f' Welcome {username}, froozen foods welcomes you....') 
            return redirect("login")  
    else:     
        form= Regform()
    return render(request,"user/register.html",{"form":form})

@login_required
def profile(request):
    return render(request,"user/profile.html",)






