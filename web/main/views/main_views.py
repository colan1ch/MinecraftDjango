from django.shortcuts import render


def index_page(request):
    context = {}
    return render(request, "index.html", context)


def error404_page(request):
    context = {}
    return render(request, "error404.html", context)
