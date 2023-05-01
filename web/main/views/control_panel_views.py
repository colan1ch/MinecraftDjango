from django.shortcuts import render
from ..forms import SetServerSettingsForm


def console_page(request, server_id):
    return render(request, 'server_console.html')


def settings_page(request, server_id):
    context = {'form': SetServerSettingsForm()}
    return render(request, "server_settings.html", context)


def world_page(request, server_id):
    return render(request, "server_world.html")
