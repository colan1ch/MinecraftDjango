from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from ..forms import SetServerSettingsForm
from django.shortcuts import redirect, get_object_or_404
from ..models import Server


def console_page(request, server_id):
    server = get_object_or_404(Server, id=server_id)
    if server.user != request.user:
        raise PermissionDenied()
    context = {'server': server,
               'IP_ADDR': 'localhost',
               'PORT': '5000',
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
    context = {'server': server}
    return render(request, "server_world.html", context)
