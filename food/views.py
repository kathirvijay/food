from asyncio import create_task
import http
from multiprocessing import context
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
#function views
def index(request):
    li= Item.objects.all()
    #template=loader.get_template("food/index.html")
    context={
        "li":li,
    }
    #return HttpResponse(li)
    #return HttpResponse(template.render(context,request))
    return render(request,"food/index.html",context)


#class view
class IndexView(ListView):
    model= Item;
    template_name="food/index.html"
    context_object_name="li"

def item(request):
    return HttpResponse("<h1>this is another view </h1>")

def detail(request,id):
    item=Item.objects.get(pk=id)
    context={
        "item":item,
    }
    #return HttpResponse("this is item/id : %s" % id)
    
    return render(request,"food/detail.html",context)

class DetailView(DetailView):
    model=Item;
    template_name="food/detail.html"
    

def add_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request,"food/forms.html",{"form":form}) 

def edit_item(request,id):
    item=Item.objects.get(id=id)
    form=ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request,"food/forms.html",{"form":form,"item":item})


# this is class based view for add item
class AddItem(CreateView):
    model= Item;
    fields= ["item_name","item_desc","item_price","item_img"]
    template_name = "food/forms.html"
    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)        
        

def delete(request,id):
    item=Item.objects.get(id=id)
    
    if request.method == "POST":
        item.delete()
        return redirect("food:index")
    return render(request,"food/delete.html",{"item":item})
    