from django.shortcuts import render
from main.views.common import get_context


def editing_profile_page(request):
    context = get_context(request)
    return render(request, "editing_profile.html", context)