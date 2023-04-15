from django.shortcuts import render
from main.views.common import get_context
from django.contrib.auth.models import User


def profile_page(request):
    context = get_context(request)
    return render(request, "profile.html", context)

def profile_edit_password(request):
    context = get_context(request)
    if (context['old_pass'] == User['pass']) and (context['new_pass'] == context['repeat']):
        User['pass'] = context['new_pass']
    return render(request, "editing_profile.html", context)

def profile_edit_logo(request):
    context = get_context(request)
    User['logo'] = context['logo']
    return render(request, "editing_profile.html", context)

def profile_edit_email(request):
    context = get_context(request)
    User['email'] = context['new_email']
    return render(request, "editing_profile.html", context)

def profile_edit_username(request):
    context = get_context(request)
    User['name'] = context['new_name']
    return render(request, "editing_profile.html", context)

def editing_profile_page(request):
    context = get_context(request)
    return render(request, "editing_profile.html", context)
