from django.db import models
from csvexport.actions import csvexport
from django.contrib import admin
# Create your models here.
# class Employees(models.Model):
#     firstname = models.CharField(max_length=255)
#     lastname = models.CharField(max_length=255)
#     telephone =models.CharField(max_length=255)
#     description = models.TextField()
#     def __str__(self):
#         return self.firstname


class SessionsModel(models.Model):    
    sessionID = models.CharField(max_length=255)   
    newsession = models.CharField(max_length=255)
    def __str__(self):
        return self.sessionID

class Msmes(models.Model):
    category =models.CharField(max_length=255)
    # sector =models.CharField(max_length=255)
    Fullname = models.CharField(max_length=255)   
    phoneNumber = models.CharField(max_length=255)
    email = models.CharField(max_length=255,default='')
    District = models.CharField(max_length=255)
    def __str__(self):
        return self.phoneNumber 


        



    

