import os
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from ..models import Server
from ..forms import SetServerSettingsForm

SERVER_IP = os.environ.get('SERVER_IP', 'localhost')
SERVER_PORT = os.environ.get('SERVER_PORT', 5000)

SERVER_ADDR = str(SERVER_IP) + ':' + str(SERVER_PORT)


def console_page(request, server_id):
    server = get_object_or_404(Server, id=server_id)
    if server.user != request.user:
        raise PermissionDenied()
    context = {'server': server,
               'SERVER_ADDR': SERVER_ADDR
               }
    return render(request, 'server_console.html', context)


def settings_page(request, server_id):
    server = get_object_or_404(Server, id=server_id)
    if server.user != request.user:
        raise PermissionDenied()
    context = {'form': SetServerSettingsForm(server.settings), 'server': server}
    return render(request, "server_settings.html", context)


def world_page(request, server_id):
    server = get_object_or_404(Server, id=server_id)
    if server.user != request.user:
        raise PermissionDenied()
    context = {'server': server,
               'SERVER_ADDR': SERVER_ADDR}
    return render(request, "server_world.html", context)
