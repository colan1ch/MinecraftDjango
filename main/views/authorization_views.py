from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from main.views.common import get_context


def login_page(request):
    if request.method == "POST":
        f = request.POST
        u = authenticate(username=f.data['login'], password=f.data['psw'])
        if u is not None:
            user = User.objects.get(username=f.data['email'])
            login(request, user)
            return redirect('/profile')
        else:
            return redirect('/authorization')
    else:
        if auth.get_user(request).is_authenticated:
            return redirect('/profile')
        context = get_context(request)
        return render(request, "authorization.html", context)


def registration_page(request):
    if request.method == "POST":
        f = request.POST
        data = f.data
        user = User(username=data['login'], email=data['email'], first_name=data['first'], last_name=data['last'])
        user.set_password(data['psw'])
        user.save()
        return redirect('/authorization')
    else:
        context = get_context(request)
        return render(request, "registration.html", context)
