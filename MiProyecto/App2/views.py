from django.shortcuts import render


def home(request):
    return render(request, 'App2/index.html')
