from django.shortcuts import render


def profile_page(request):
    context = {}
    return render(request, "profile.html", context)


def editing_profile_page(request):
    context = {}
    return render(request, "editing_profile.html", context)
