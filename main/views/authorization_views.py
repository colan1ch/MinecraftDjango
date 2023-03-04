from django.shortcuts import render
from main.views.common import get_context


def authorization_page(request):
    context = get_context(request)
    return render(request, "authorization.html", context)