from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def auth(request):
    return render(request, 'main/auth.html')

def registration(request):
    return render(request, 'main/registration.html')