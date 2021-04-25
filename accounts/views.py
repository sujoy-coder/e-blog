from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    if not request.user.is_anonymous:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        username = email.split('@')[0]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfull !!! You can create new Post')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials !!! Provide correct Information')
            return render(request, 'accounts/login.html', {'title':'Login', 'email_value': email})
    return render(request, 'accounts/login.html', {'title':'Login'})


def register(request):
    if not request.user.is_anonymous:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        username = email.split('@')[0]
        if User.objects.filter(username=username).first():
            messages.error(request, 'Email is already registered')
        elif password1 != password2:
            messages.error(request, 'Both passwords are not matched')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()
            messages.success(request, 'Registration Successfull !!! Now you can Login')
            return redirect('login')
        return render(request, 'accounts/register.html', {'title':'Register', 'email_value': email})
    return render(request, 'accounts/register.html', {'title':'Register'})


def user_logout(request):
    logout(request)
    messages.info(request, 'You are Logout !!!')
    return redirect('login')

