from django.shortcuts import render,redirect
import socket
from .forms import USerForm,UpdateForm,UserSearchForm
from . models import UserRegistration,Admin_panel
from django.core.mail import send_mail
from django.conf import settings
from django.views import View
from django.contrib.auth.hashers import check_password

class Login(View):
    def get(self,request):
        return render(request,"User_management/login.html")
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = Admin_panel.get_Login_byusername(username)
        context = {
            "username":username,
            "message":"Welcome to Admin Panel"
        }
        if user:
            flag = check_password(password,user.password)
            if flag:
                return render(request,"User_management/home.html",context)
            else:
                error_message = "Invalid credentials"
        else:
            error_message="Invalid credentials"
        return render(request,"User_management/login.html",{"error":error_message})


    
def logout(request):
    request.session.clear()
    return redirect('/')

def add_user(request):
    socket.getaddrinfo('localhost',8000)
    reciepient_list =list(Admin_panel.objects.all().values_list("email",flat=True))
    form = USerForm(request.POST or None)
    total_users = UserRegistration.objects.count()
    queryset = UserRegistration.objects.order_by('-qualification')[:10]
    if form.is_valid():
        name = form.cleaned_data['name']
        email_id = form.cleaned_data['email_id']
        qualification = form.cleaned_data['qualification']
        address = form.cleaned_data['address']
        user = UserRegistration(name=name,
                                email_id=email_id,
                                qualification=qualification,
                                address=address)
        user.save()
        subject = f' NEW USER NAMED {user.name} ADDED'
        body = {
            "NAME":name,
            "EMAIL_ID":email_id,
            "QUALIFICATION":qualification,
            "ADDRESS":address
        }
        message = "\n".join(f'{k}:{v}' for k,v in body.items())
        send_mail(subject,message,
                  settings.EMAIL_HOST_USER,
                  reciepient_list,fail_silently=False)
        return redirect('/existing_user')
    context = {
        "form":form,
        "total_users":total_users,
        "queryset":queryset
    }
    return render(request,"User_management/user_form.html",context)

def existing_user(request):
    title = "All Registered User"
    queryset = UserRegistration.objects.all()
    form = UserSearchForm(request.POST or None)
    context = {
        'title':title,
        "form":form,
        'queryset':queryset
    }
    if request.method == "POST":
        queryset=UserRegistration.objects.filter(
            name__icontains=form['name'].value(),
            email_id__icontains=form['email_id'].value())
        
    context = {
        'title':title,
        "form":form,
        'queryset':queryset
    }
    return render(request,'User_management/existing_users.html',context)

def update_user(request,pk):
    reciepient_list =list(Admin_panel.objects.all().values_list("email",flat=True))
    queryset = UserRegistration.objects.get(id=pk)
    form = UpdateForm(instance=queryset)
    if request.method == "POST":
        form = UpdateForm(request.POST,instance=queryset)
        if form.is_valid():
            name = form.cleaned_data['name']
            email_id = form.cleaned_data['email_id']
            qualification = form.cleaned_data['qualification']
            address = form.cleaned_data['address']
            user = UserRegistration(name=name,
                                email_id=email_id,
                                qualification=qualification,
                                address=address)
            form.save()
            subject = f'DETAILS UPDATED FOR {user.name}'
        body = {
            "NAME":name,
            "EMAIL_ID":email_id,
            "QUALIFICATION":qualification,
            "ADDRESS":address
        }
        message = "\n".join(f'{k}:{v}' for k,v in body.items())
        send_mail(subject,message,
                  settings.EMAIL_HOST_USER,
                  reciepient_list,fail_silently=False)
        return redirect('/existing_user')
        
    context = {
        'form':form
    }
    return render(request,'User_management/user_form.html',context)

def delete_user(request,pk):
    queryset = UserRegistration.objects.get(id=pk)
    if request.method == "POST":
        queryset.delete()
        return redirect('/existing_user')
    return render(request,'User_management/delete.html')