import logging

from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect,get_object_or_404
from django.template.context_processors import request
from .models import Explores
from .models import Profile
from.forms import ExploreForm
from.forms import VregistrationForm
from.forms import VloginForm
from.forms import UregistrationForm
from.forms import UloginForm

# Create your views here.
def home(request):
    return render(request,'home.html')
def package(request):
    return render(request,'package.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def register(request):
    return render(request,'register.html')
def successreg(request):
    return render(request,'reg success.html')
def vendordash(request):
    current_user = request.user.id
    packages=Explores.objects.filter(user=current_user)
    return render(request,'vendordash.html',{'packages':packages})
def create(request):
    if request.method=='POST':
        form=ExploreForm(request.POST,request.FILES)
        if form.is_valid():
            tour_packages = form.save(commit=False)
            tour_packages.user = request.user
            tour_packages.save()
            return redirect('vendordash')
    else:
        form=ExploreForm()
    return render(request,'create n p.html',{'form':form,'current_user': request.user.id})

def userdash(request):
    packages=Explores.objects.filter(approved=1)
    return render(request,'userdash.html',{'packages':packages})
def book(request):
    return render(request,'book.html')
def payment(request):
    return render(request,'payment.html')
def book1(request):
    return render(request,'book1.html')
def book2(request):
    return render(request,'book2.html')
def book3(request):
    return render(request,'book3.html')
def book4(request):
    return render(request,'book4.html')
def book5(request):
    return render(request,'book5.html')
def book6(request):
    return render(request,'book6.html')
def book7(request):
    return render(request,'book7.html')
def book8(request):
    return render(request,'book8.html')
def book9(request):
    return render(request,'book9.html')
def vendorreg(request):
    if request.method=='POST':
        form=VregistrationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return render(request,'reg success.html')
    else:
        form=VregistrationForm()
    return render(request,'vendor reg.html',{'form':form})
def vendorlog(request):
    if request.method=='POST':
        form=VloginForm(request.POST,request.FILES)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                profile = Profile.objects.get(user=user)
                return redirect('vendordash')

            else:
                logging.log(logging.CRITICAL,"invalid creds")
    else:
        form=VloginForm()
    return render(request,'vendor log.html',{'form':form})
def userreg(request):
    if request.method=='POST':
        form=UregistrationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return render(request,'reg success.html')
    else:
        form=UregistrationForm()
    return render(request,'user reg.html',{'form':form})

def userlog(request):
    if request.method=='POST':
        form=UloginForm(request.POST,request.FILES)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            logging.log(logging.CRITICAL,username)
            logging.log(logging.CRITICAL,password)
            logging.log(logging.CRITICAL,user)
            if user:
                login(request,user)
                profile = Profile.objects.get(user=user)
                return redirect('userdash')
            else:
                logging.log(logging.CRITICAL,"invalid creds")
    else:
        form=UloginForm()
    return render(request,'user log.html',{'form':form})
def delete_item(request,id):
    item=Explores.objects.get(id=id)
    item.delete()
    return redirect("/vendordash")
def edit(request,id):
    explore_instance=Explores.objects.get(id=id)
    if request.method =='POST':
        form=ExploreForm(request.POST,instance = explore_instance)
        if form.is_valid():
            form.save()
            return redirect('/vendordash')
    else:
        form=ExploreForm(instance = explore_instance)
    return render(request,"edit.html",{'form':form})
def user_logout(request):
    logout(request)  # Logs out the user
    return redirect('home')


