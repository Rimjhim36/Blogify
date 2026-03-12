from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *
import sweetify

# Create your views here.

def index(request):
    return render(request,'index.html')

def login_view(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        try:
            user = LoginInfo.objects.get(username=un, password=pwd)
            if user:
                request.session['adminid'] = user.username
                sweetify.success(
                request,
                title="Success 🎉",
                text="Logged in Successfully"
                )
                return redirect('admindash')
            return redirect('admindash')
        except LoginInfo.DoesNotExist:
            sweetify.error(
            request,
            title="Error",
            text="invalid username or password"
            )
            return redirect('login') 
    return render(request, 'login.html')


def about(request):   
    return render(request,'about.html')


def viewblog(request):
    alldata = Blog.objects.all()
    context = {
        'alldata': alldata
    }
    return render(request,'viewblog.html',context)


def cardview(request,id):
    data = Blog.objects.get(id=id)
    context = {
        'data': data
    }
    return render(request,'cardview.html', context)


def admindash(request):
    if not 'adminid' in request.session :
            sweetify.error(
            request,
            title="Error",
            text="Login First"
            )
            return redirect('login')
    return render(request,'admindash.html')


def addblog(request):
    if not 'adminid' in request.session :
            sweetify.error(
            request,
            title="Error",
            text="Login First"
            )
            return redirect('login')
    data = BlogForm()
    context = {
        'data': data
    }    
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            sweetify.success(
            request,
            title="Successful  🎉",
            text="Saved Successfully"
            )
            return redirect('addblog')
    return render(request,'addblog.html',context)


def logout_view(request):
    if 'adminid' in request.session:
        del request.session['adminid']
        sweetify.success(
        request,
        title="Success 🎉",
        text="Logout Successfully"
    )
        return redirect('login')
    return redirect('login')
 

def adminview(request):
    if not 'adminid' in request.session :
        sweetify.error(
        request,
        title="Error",
        text="Login First"
        )
        return redirect('login') 
    alldata = Blog.objects.all()
    context = {
        'alldata': alldata
    }         
    return render(request,'adminview.html', context)
   

def adminedit(request, id):
    if not 'adminid' in request.session:
        sweetify.error(
        request,
        title="Error",
        text="Login First"
        )
        return redirect('login')
    blog = Blog.objects.get(id=id)
    form = BlogForm(instance=blog)    
    if request.method == 'POST':
        data = BlogForm(request.POST, request.FILES, instance=blog)
        if data.is_valid():
            data.save()
            sweetify.success(
            request,
            title="Success 🎉",
            text="Updated Successfully"
            )
            return redirect('adminview')
    return render(request, 'adminedit.html', {"form":form})   



def delblog(request,id):
     blog = Blog.objects.get(id=id)
     blog.delete()
     sweetify.success(
            request,
            title="Success 🎉",
            text="Deleted Successfully"
            )
     return redirect('adminview')
     return render(request,'adminview')
