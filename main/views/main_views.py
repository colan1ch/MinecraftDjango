from django.shortcuts import render
from main.views.common import get_context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def index_page(request):
    context = get_context(request)
    return render(request, "index.html", context)


def error404_page(request):
    context = get_context(request)
    return render(request, "error404.html", context)


def create_server_page(request):
    return render(request, "create_server.html")
