from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render

from .backends import generate_report
from .models import Debt, Report


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


def reports_list(request):
    if request.method == 'GET':
        return render(
            request,
            'reports_list.html',
            {'reports': request.user.reports.all().order_by('-date_created')}
        )
    else:
        return HttpResponse(f'Method {request.method} not allowed', status=405)


def report_generate(request):
    if request.method == 'GET':
        new_report = generate_report(request.user)
        new_report.save()
        return HttpResponseRedirect('/report_download/' + str(new_report.id))
    else:
        return HttpResponse(f'Method {request.method} not allowed', status=405)


def report_download(request, report_id):
    if request.method == 'GET':
        report = Report.objects.get(id=report_id)
        response = FileResponse(open(settings.REPORTS_DIR / report.file_name, 'rb'))
        response['Content-Disposition'] = f'attachment; filename="{report.file_name}"'
        return response
    else:
        return HttpResponse(f'Method {request.method} not allowed', status=405)
