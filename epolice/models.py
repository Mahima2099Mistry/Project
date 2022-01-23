from django.db import models
from django.db.models.base import Model

from mysite.settings import AUTH_PASSWORD_VALIDATORS

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=10)
    address = models.TextField(max_length=300)
    role = models.CharField(max_length=20,null=True,blank=True)
    password = models.CharField(max_length=50)
    pic = models.FileField(upload_to='Profile',default='profile.jpg')

    def __str__(self):
        return self.fname + ' ' + self.lname

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.name

class FIR(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    fir_title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    place = models.TextField(max_length=300)
    status = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return self.name

class Criminal(models.Model):
    uid = models.ForeignKey(User,on_delete=models.CASCADE)
    criminal_name = models.CharField(max_length=50)
    address = models.TextField(max_length=300)
    mobile = models.CharField(max_length=20)
    crime = models.CharField(max_length=50)
    crime_details = models.TextField(max_length=300)
    pic = models.FileField(upload_to='criminals',null=True,blank=True)

    def __str__(self):
        return self.criminal_name
