from django.shortcuts import render
from main.views.common import get_context


def index_page(request):
    context = get_context(request)
    return render(request, "index.html", context)


def error404_page(request):
    context = get_context(request)
    return render(request, "error404.html", context)
