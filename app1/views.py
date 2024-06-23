from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')


def SignUpPage(request):
    if request.method == 'POST':
        uname = request.POST['username']
        # Проверка что имя пользователя не такое как имя админа (НЕ ОБЯЗАТЕЛЬНО ДЕЛАТЬ)
        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already exists")

        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 != pass2:
            return HttpResponse("Passwords don't match")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass']
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid login details")
    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')
