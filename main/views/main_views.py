from django.shortcuts import render
from main.views.common import get_context


def index_page(request):
    context = get_context(request)
    return render(request, "index.html", context)