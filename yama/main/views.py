from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.conf import settings


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def registration(request):
    if request.method == 'GET':
        return render(request, 'registration/registration.html')
    elif request.method == 'POST':
        user = User.objects.create_user(
            request.POST.get('username'),
            request.POST.get('email'),
            request.POST.get('password'),
            # request.POST,
        )
        user.save()
        return HttpResponseRedirect(settings.LOGIN_URL)
    else:
        return HttpResponse(f'Method {request.method} not allowed', status=405)
