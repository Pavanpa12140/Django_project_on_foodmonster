from django.shortcuts import render,redirect
from .forms import userForm
from vender.forms import venderForm
from django.contrib import messages,auth
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def registerUser(req):
    form = userForm()
    if req.method == 'POST':
        form = userForm(req.POST)
        if form.is_valid:
            #first_name = req.POST['first_name']
            #last_name = req.POST['last_name']
            #email = req.POST['email']
            #password = req.POST['password']
            #confirm_password = req.POST['confirm_password']
            #password = make_password(password)
            #confirm_password = make_password(confirm_password)
            #print('first_name=>',first_name,
            #'\nlast_last=>',last_name,
            #'\nemail=>',email,
            #'\npassword=>',password,
            #'\nconfirm_passowrd=>',confirm_password)
           form.save()
           messages.success(req,'Thank you for registred')
        else:
           print(form.errors)
        
    return render(req,'registerUser.html',{'form':form})

def registerVendor(req):
    form = venderForm
    user = userForm
    
    if req.method == 'POST':
        form = venderForm(req.POST)
        user = userForm(req.POST)
        if form.is_valid():
            #first_name = req.POST['first_name']
            #last_name = req.POST['last_name']
            #vender_name = req.POST['vender_name']
            #password = req.POST['password']
            #confirm_password = req.POST['confirm_password']
            #password = make_password(password)
            #confirm_password = make_password(confirm_password)
            #print('first_name=>',first_name,
            #'\nlast_last=>',last_name,
            #'\nVender_name=>',vender_name,
            #'\npassword=>',password,
            #'\nconfirm_passowrd=>',confirm_password)
            #form.save()
            if user.is_valid:
                user.save()
                messages.success(req,'Thank you for registred')
            else:
                print("wrong")
        else:
            print(form.errors)
    context = {
        'form':form,
        'user':user
    }
    return render(req,'registerVender.html',context)


def user_login(req):
    if req.user.is_authenticated:
        messages.error(req,"You are already login...!!")
        #return HttpResponseRedirect(reverse('nava:dashboard/'))
    elif req.method == 'POST':
        email = req.POST['email']
        password = req.POST['password']
        #print(email,password)
        user = auth.authenticate(email=email,password=password) 
        if user:
            if user.is_active:
                auth.login(req,user)
                #return HttpResponseRedirect(reverse('nava:dashboard/'))
                if login and user.role == 1:
                    return HttpResponseRedirect(reverse('nava:dashboardvender/'))
                elif login and user.role == 2:
                    return HttpResponseRedirect(reverse('nava:dashboard/'))
                else:
                    return HttpResponse("User is not activated")
        else:
            return HttpResponse("Please enter correct email and password")
    return render(req,'login.html')

@login_required
def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse('nava:user_login'))


@login_required
def dashboard(request):
    return render(request,"dashboard.html")

@login_required
def dashboardvender(req):
    return render(req,'dashboardvender.html')