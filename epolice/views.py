from django.db import reset_queries
from django.db.models.query_utils import RegisterLookupMixin
from django.shortcuts import render,redirect

from mysite.settings import TEMPLATES, USE_I18N
from .models import *
from django.conf import settings
from django.core.mail import send_mail
from random import randrange,choices


# Create your views here.
def index(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'index.html',{'uid':uid})
    except:
        return render(request,'index.html')

def about(request):
    try:
        uid = User.objects.get(email=request.session['email'])
        return render(request,'about.html',{'uid':uid})
    except:
        return render(request,'about.html')

def register(request):
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            msg = "Your Email already Exist"
            return render(request,'register.html',{'msg':msg})
        except:
            if request.POST['password'] == request.POST['confirm_password']:
                global temp
                otp = randrange(1000,9999)

                temp = {
                    'fname' : request.POST['fname'],
                    'lname' : request.POST['lname'],
                    'email' : request.POST['email'],
                    'mobile' : request.POST['mobile'],
                    'address' : request.POST['address'],
                    'role' : request.POST['role'],
                    'password' : request.POST['password'],
                    'otp' : otp
                }

                subject = "OTP Verification"
                message = f'Hello User your OTP is : {otp}'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [request.POST['email'], ]
                send_mail(subject,message,email_from,recipient_list)
                return render(request,'otp.html',{'otp':otp})

            else:
                msg = 'Password and confirm password does not match'
                return render(request,'register.html',{'msg':msg})

    return render(request,'register.html')

def otp(request):
    if request.method == "POST":
        if request.POST['otp'] == request.POST['uotp']:
            global temp
            User.objects.create(
                fname = temp['fname'],
                lname = temp['lname'],
                email = temp['email'],
                mobile = temp['mobile'],
                address = temp['address'],
                role = temp['role'],
                password = temp['password']
            )

            msg1 = 'User Created'
            del temp
            return render(request,'login.html',{'msg1':msg1})

        else:
            msg = "OTP does not match"
            return render(request,'otp.html',{'msg':msg,'otp':request.POST['otp']})

    return render(request,'otp.html')

def login(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST['email'])
            if request.POST['password'] == uid.password:
                request.session['email'] = request.POST['email']
                return render(request,'index.html',{'uid':uid})
            else:
                return render(request,'login.html',{'msg':'Incorrect Password'})
        except:
            msg = 'Incorrect Email'
            return render(request,'login.html',{'msg':msg})

    return render(request,'login.html')

def logout(request):
    del request.session['email']
    return redirect('index')

def forgot_password(request):
    if request.method == 'POST':
        try:
            uid = User.objects.get(email=request.POST['email'])
            s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
            pw = ''.join(choices(s,k=6))

            subject = "E-Police Reset Password"
            message = f"""Hello {uid.fname} {uid.lname}!!!,
            Your New Password is here!!!
            {pw}
            
            Please Login with new Password"""
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [request.POST['email'], ]
            send_mail(subject,message,email_from,recipient_list)

            uid.password = pw
            uid.save()
            return render(request,'login.html',{'msg1':'New Password is sent on your Email'})
        except:
            return render(request,'forgot_password.html',{'msg':'Incorrect Email'})

    return render(request,'forgot_password.html')

def profile(request):
    uid = User.objects.get(email=request.session['email'])

    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm_password']:
            uid.fname = request.POST['fname']
            uid.lname = request.POST['lname']
            uid.mobile = request.POST['mobile']
            uid.address = request.POST['address']
            uid.password = request.POST['password']
            if 'pic' in request.FILES:
                uid.pic = request.FILES['pic']
            uid.save()
            return render(request,'profile.html',{'msg1':'Your Profile Edited Successfully!!!','uid':uid})
        else:
            return render(request,'profile.html',{'msg':'Password and Confirm Password does not match','uid':uid})

    return render(request,'profile.html',{'uid':uid})

def contact(request):
    uid = User.objects.get(email=request.session['email'])

    if request.method == 'POST':
        Contact.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        subject = "Thank You for Contact Us"
        message = f'Hello {request.POST["name"]}! Thank You for Contact Us. Admin will Contact you soon.!!'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email'], ]
        send_mail(subject,message,email_from,recipient_list)


        subject = "Someone is Contact You"
        message = f"""Hello Admin! Someone is trying to contact you. Here are the details :
        Name : {request.POST['name']}
        Email : {request.POST['email']}
        Subject : {request.POST['subject']}
        Message : {request.POST['message']}"""

        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['mahima2006mistry@gmail.com', ]
        send_mail(subject,message,email_from,recipient_list)

        return render(request,'contact.html',{'msg':'We Will Contact you soon.','uid':uid})

    return render(request,'contact.html',{'uid':uid})

def add_fir(request):
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

def view_fir(request):
    uid = User.objects.get(email=request.session['email'])
    vfir = FIR.objects.filter(uid=uid)
    return render(request,'view_fir.html',{'uid':uid,'vfir':vfir})

def view_fir_police(request):
    uid = User.objects.get(email=request.session['email'])
    vfir = FIR.objects.all()
    select = False
    if request.method == 'POST':
        select = request.POST['search']
        if select == 'pending':
            select = False
        else:
            select = True

    return render(request,'view_fir.html',{'uid':uid,'vfir':vfir,'select':select})

def solved_fir(request,id):
    vfir = FIR.objects.get(id=id)
    vfir.status = True
    vfir.save()
    return redirect('view_fir_police')

def add_criminal(request):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        if 'pic' in request.FILES:
            Criminal.objects.create(
            uid = uid,
            criminal_name = request.POST['criminal_name'],
            address = request.POST['address'],
            mobile = request.POST['mobile'],
            crime = request.POST['crime'],
            crime_details = request.POST['crime_details'],
            pic = request.FILES['pic'],
            )
        else:
            Criminal.objects.create(
            uid = uid,
            criminal_name = request.POST['criminal_name'],
            address = request.POST['address'],
            mobile = request.POST['mobile'],
            crime = request.POST['crime'],
            crime_details = request.POST['crime_details'],
        
            )


        return render(request,'add_criminal.html',{'msg':'Added Criminal Details','uid':uid})

    return render(request,'add_criminal.html',{'uid':uid})

def view_criminal(request):
    uid = User.objects.get(email=request.session['email'])
    criminals = Criminal.objects.all()
    return render(request,'view_criminals.html',{'uid':uid,'criminals':criminals})

def edit_criminal(request,id):
    uid = User.objects.get(email=request.session['email'])
    criminals = Criminal.objects.get(id=id)

    if request.method == 'POST':
        criminals.criminal_name = request.POST['criminal_name']
        criminals.address = request.POST['address']
        criminals.mobile = request.POST['mobile']
        criminals.crime = request.POST['crime']
        criminals.crime_details = request.POST['crime_details']
        if 'pic' in request.FILES:
            criminals.pic = request.FILES['pic']
        criminals.save()
        criminals = Criminal.objects.all()
        return render(request,'view_criminals.html',{'msg':'Edited Successfully','uid':uid,'criminals':criminals})

    return render(request,'edit_criminal.html',{'uid':uid,'criminals':criminals})

def delete_criminal(request,id):
    uid = User.objects.get(email = request.session['email'])
    criminals = Criminal.objects.get(id=id)
    criminals.delete()
    criminals = Criminal.objects.all()
    return render(request,'view_criminals.html',{'msg':'Deleted Successfully','uid':uid,'criminals':criminals})
