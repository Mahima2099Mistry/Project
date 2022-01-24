from django.shortcuts import render
from epolice.models import *
from police_station.models import Police_station

# Create your views here.
def view_fir_commissioner(request):
    uid = User.objects.get(email=request.session['email'])
    vfir = FIR.objects.all()
    return render(request,'view_fir.html',{'uid':uid,'vfir':vfir})

def add_police_station(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        Police_station.objects.create(
            police_station_name = request.POST['police_station_name'],
            area = request.POST['area']
        )
        return render(request,'add_police_station.html',{'msg':'Added Successfully','uid':uid})
    return render(request,'add_police_station.html',{'uid':uid})

def view_police_station(request):
    uid = User.objects.get(email=request.session['email'])
    police_station = Police_station.objects.all()
    return render(request,'view_police_station.html',{'uid':uid,'police_station':police_station})

def edit_police_station(request,id):
    uid = User.objects.get(email=request.session['email'])
    police_station = Police_station.objects.get(id=id)

    if request.method == 'POST':
        police_station.police_station_name = request.POST['police_station_name']
        police_station.area = request.POST['area']
        police_station.save()
        police_station = Police_station.objects.all()
        return render(request,'view_police_station.html',{'msg':'Edited Successfully','uid':uid,'police_station':police_station})
    return render(request,'edit_police_station.html',{'uid':uid,'police_station':police_station})

def delete_police_station(request,id):
    uid = User.objects.get(email=request.session['email'])
    police_station = Police_station.objects.get(id=id)
    police_station.delete()
    police_station = Police_station.objects.all()
    return render(request,'view_police_station.html',{'msg':'Deleted Successfully','uid':uid,'police_station':police_station})

def view_police(request):
    uid = User.objects.get(email=request.session['email'])

    police = User.objects.filter(role='police')
    return render(request,'view_police.html',{'uid':uid,'police':police})

def add_fir_commissioner(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        FIR.objects.create(
            uid = uid,
            name = request.POST['name'],
            fir_title = request.POST['fir_title'],
            description = request.POST['description'],
            place = request.POST['place'],
        )
        return render(request,'add_fir.html',{'msg':'Added Successfully','uid':uid})
    return render(request,'add_fir.html',{'uid':uid})

def add_police(request):
    uid = User.objects.get(email = request.session['email'])
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            if 'pic' in request.FILES:
                User.objects.create(
                    fname = request.POST['fname'],
                    lname = request.POST['lname'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    address = request.POST['address'],
                    role = request.POST['role'],
                    password = request.POST['password'],
                    pic = request.FILES['pic'],
                )
            else:
                User.objects.create(
                    fname = request.POST['fname'],
                    lname = request.POST['lname'],
                    email = request.POST['email'],
                    mobile = request.POST['mobile'],
                    address = request.POST['address'],
                    role = request.POST['role'],
                    password = request.POST['password'],
                )
        else:
            return render(request,'add_police.html',{'uid':uid,'msg1':'Password and Confirm Password Does not match'})

        return render(request,'add_police.html',{'msg':'Added Successfully','uid':uid})
    return render(request,'add_police.html',{'uid':uid})

def edit_police(request,id):
    uid = User.objects.get(email=request.session['email'])
    police = User.objects.get(id=id)

    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            police.fname = request.POST['fname']
            police.lname = request.POST['lname']
            police.mobile = request.POST['mobile']
            police.address = request.POST['address']
            police.password = request.POST['password']
            if 'pic' in request.FILES:
                police.pic = request.FILES['pic']
            police.save()
            police = User.objects.filter(role='police')
            return render(request,'view_police.html',{'msg':'Edited Successfully','uid':uid,'police':police})
        else:
            return render(request,'edit_police.html',{'msg1':'Password and Confirm Does not match','uid':uid,'police':police})
    
    return render(request,'edit_police.html',{'uid':uid,'police':police})

def delete_police(request,id):
    uid = User.objects.get(email=request.session['email'])
    police = User.objects.get(id=id)
    police.delete()
    police = User.objects.all()
    return render(request,'view_police.html',{'msg':'Deleted Successfully','uid':uid,'police':police})