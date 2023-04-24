from django.shortcuts import render
from main.views.common import get_context


def login_page(request):
    context = get_context(request)
    return render(request, "login.html", context)

def registration_page(request):
    context = get_context(request)
    return render(request, "registration.html", context)
