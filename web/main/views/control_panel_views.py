from django.shortcuts import render


def console_page(request, server_id):
    return render(request, 'server_console.html')


def settings_page(request, server_id):
    return render(request, "server_settings.html")


def world_page(request, server_id):
    return render(request, "server_world.html")
