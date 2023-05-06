from django.shortcuts import render
from ..forms import SetServerSettingsForm


def console_page(request, server_id):
    context = {'server_id': server_id}
    return render(request, 'server_console.html', context)


def settings_page(request, server_id):
    context = {'form': SetServerSettingsForm(), 'server_id': server_id}
    return render(request, "server_settings.html", context)


def world_page(request, server_id):
    context = {'server_id': server_id}
    return render(request, "server_world.html", context)
