from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
import json
from django.http import HttpResponse
from .models import Vacation,Account

@login_required(login_url='login')
def addVacation(request):
    pending=Vacation.objects.filter(status='PENDING').count()
    approved=Vacation.objects.filter(status='APPROVED').count()
    denied=Vacation.objects.filter(status='DENIED').count()
    context={}
    if request.method == 'POST':
        vacation = Vacation(
            owner=request.user,
            type_vacation = request.POST['type_vacation'],
            start_date = request.POST['start_date'],
            end_date = request.POST['end_date'],
            comments = request.POST['comments'],

            )
        
        vacation.save()
        return redirect('vacation-user')
    context={'types': list(Vacation.TYPE_OF_VACATION),
        'pending':pending,
        'approved':approved,
        'denied':denied,
    }
    return render(request, 'vacation/add-vacation.html',context)
   
@login_required(login_url='login')
def editVacation(request,id):
    page='edit'
    vacation = Vacation.objects.get(id=id)
    # print(vacation)
    if vacation.owner.id== request.user.id:
        if request.method == 'POST':
            defaults=dict(
            #status = request.POST['status'],
            type_vacation = request.POST['type_vacation'],
            start_date = request.POST['start_date'],
            end_date = request.POST['end_date'],
            comments= request.POST['comments'])
            vacation, created = Vacation.objects.update_or_create(id=id,defaults=defaults)
            return redirect('vacation-user')
    return render(request, 'vacation/add-vacation.html', {'vacation': vacation,'page':True,'types': list(Vacation.TYPE_OF_VACATION)})

@login_required(login_url='login')
def approve(request,id):
    Vacation.objects.filter(id=id).update(status='Approved')
    return redirect('vacation-user')

@login_required(login_url='login')
def deny(request,id):
    Vacation.objects.filter(id=id).update(status='Denied')
    return redirect('vacation-user')
  

@login_required(login_url='login')
def deleteVacation(request, id):
    vacation = Vacation.objects.get(id=id)
    if vacation.owner.id == request.user.id:
        if request.method == 'GET':
            vacation.delete()
            return redirect('vacation-user')
        # return render(request, 'vacation/delete-vacation.html', context)

    else:
        return HttpResponseForbidden()


@login_required(login_url='login')
def showUserVacation(request):
    pending=Vacation.objects.filter(status='PENDING').count()
    approved=Vacation.objects.filter(status='APPROVED').count()
    denied=Vacation.objects.filter(status='DENIED').count()
    owner = request.user.id
    vacations = Vacation.objects.filter(owner=request.user)
    vacations=Vacation.objects.order_by('-date_vacation')
    context={
        'vacations':vacations,
        'pending':pending,
        'approved':approved,
        'denied':denied,
        'types': list(Vacation.TYPE_OF_VACATION),
        'statuses': list(Vacation.STATUS)
    }
    return render(request,'vacation/user-vacation.html',context)