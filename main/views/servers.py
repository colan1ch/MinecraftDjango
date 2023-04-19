from django.shortcuts import render
from main.models import Servers


def servers_page(request):
    context = {
        'servers': Servers.objects.all()
    }
    return render(request, "servers.html", context)
