from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import Debt


def index(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'index.html', {'debts': request.user.debts.all()})
        else:
            return render(request, 'index.html')
    else:
        return HttpResponse(f'Method {request.method} not allowed', status=405)


def about(request):
    if request.method == 'GET':
        return render(request, 'about.html')
    else:
        return HttpResponse(f'Method {request.method} not allowed', status=405)


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


def debt_create(request):
    if request.method == 'GET':
        return render(request, 'debt_create.html')
    elif request.method == 'POST':
        debt = Debt.objects.create(
            creditor=request.user,
            debtor=request.POST.get('debtor'),
            amount=request.POST.get('amount'),
            description=request.POST.get('description'),
            date_due=request.POST.get('date'),
        )
        debt.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse(f'Method {request.method} not allowed', status=405)


def debt_delete(request, debt_id):
    if request.method == 'POST':
        debt = Debt.objects.get(id=debt_id)
        debt.delete()
        return HttpResponseRedirect('/')
    else:
        return HttpResponse(f'Method {request.method} not allowed', status=405)
