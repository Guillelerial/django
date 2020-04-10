from django.shortcuts import render


def welcome_page(request):
    return render(request, "excel2web/welcome.html")
