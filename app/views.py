from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm,PostForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Post
from django.contrib.auth.models import User,Group
from django.contrib import messages
from .forms import PostForm

# Create your views here.


def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{"posts":posts})


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def login_user(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=LoginForm(request=request,data=request.POST)
            if fm.is_valid():
                un=fm.cleaned_data['username']
                pw=fm.cleaned_data['password']
                reg=authenticate(username=un,password=pw)
                if reg != None:
                    login(request,reg)
                    messages.success(request,'Congratulations! You have successfully logged in.')
                    return HttpResponseRedirect('/dashboard')
        else:
            fm=LoginForm()
        return render(request,'login.html',context={'fm':fm})
    else:
        return HttpResponseRedirect('/')


def signup_user(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm=SignUpForm(request.POST)
            if fm.is_valid():
                user=fm.save()
                group=Group.objects.get(name='Author')
                user.groups.add(group)

                # fm=SignUpForm()
                messages.success(request,'Congratulations! You have become an author.')
                return HttpResponseRedirect('/login')
        else:
            fm=SignUpForm()
        return render(request,'signup.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/')


def dashboard(request):
    if request.user.is_authenticated:
        fm=Post.objects.all()
        return render(request,'dashboard.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/login')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login')


def addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=PostForm(request.POST)
            if fm.is_valid():
                fm.save()
                # messages.success(request,"Form Submitted Successfully!!!")
                # fm=PostForm()
                return HttpResponseRedirect('/dashboard')
        else:
            fm=PostForm()
        return render(request,'addpost.html',{'fm':fm})
    else:
        return HttpResponseRedirect('/login')

def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=Post.objects.get(pk=id)
            form=PostForm(request.POST,instance=fm)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard')
        else:
            fm=Post.objects.get(pk=id)
            form=PostForm(instance=fm)
        return render(request,'update.html',{'fm':form})
    else:
        return HttpResponseRedirect('/login')

def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=Post.objects.get(pk=id)
            fm.delete()
        return HttpResponseRedirect('/dashboard')
    else:
        return HttpResponseRedirect('/login')
