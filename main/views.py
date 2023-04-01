
from django.contrib.auth.views import LoginView
from .forms import *
from django.urls import reverse_lazy
from django.shortcuts import render

def  login_page(request):
    form_class = LoginPage
    context = {
        'form': LoginView.get_form(),
    }

    #return reverse_lazy('index')
    return render(request, 'registration/login.html', context)


