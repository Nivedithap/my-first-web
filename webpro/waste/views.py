from django.shortcuts import render
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,reverse
from .forms import MyRegistrationForm
from .forms import Prodform
from .forms import Imageform

# Create your views here.
def prod_list(request):
    latest_prods = Product.objects.all()
    context={'latest_prods':latest_prods}
    return render(request, 'waste/prod_list.html', context)

def mainpage(request):
    return render(request,'waste/mainpage.html',{})
def about(request):
    return render(request,'waste/about.html',{})
def contact(request):
    return render(request,'waste/contact.html',{})
def blog(request):
    return render(request,'waste/blog.html',{})

def register(request):
    if request.method=="POST":
        form= MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('waste:main_page')
    else :
        form=MyRegistrationForm()
    return render(request,'waste/reg.html',{'form':form})

def myprod_list(request):
    latest_prods = Product.objects.all()
    context={'latest_prods':latest_prods}
    return render(request, 'waste/myprod_list.html', context)

def activate(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    product.activate=True
    product.save()
    return redirect('waste:myprod_list')

def deactivate(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    product.activate=True
    product.save()
    return redirect('waste:myprod_list')

def addprod(request):
    if request.method=="POST":
        form=Prodform(request.POST, request.FILES)
        if form.is_valid():
            prod_item=form.save(commit=False)
            prod_item.user=request.user
            prod_item.save()
            return redirect('waste:myprod_list')
    else:
        form=Prodform()
    return render(request,'waste/addprod.html',{'form':form})


    
    
