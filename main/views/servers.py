from django.shortcuts import render
from main.models import Server


def servers_page(request):
    context = {
        'servers': Server.objects.all()
    }
    return render(request, "servers.html", context)
