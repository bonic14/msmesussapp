from django.db import models

# Create your models here.
# class Employees(models.Model):
#     firstname = models.CharField(max_length=255)
#     lastname = models.CharField(max_length=255)
#     telephone =models.CharField(max_length=255)
#     description = models.TextField()
#     def __str__(self):
#         return self.firstname
class Registration(models.Model):
    phone =models.CharField(max_length=255) 
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255) 

    def __str__(self):
        return self.firstname 

class SessionsModel(models.Model):    
    sessionID = models.CharField(max_length=255)   
    newsession = models.CharField(max_length=255)
    def __str__(self):
        return self.sessionID

class Iworkers(models.Model):
    Fullname = models.CharField(max_length=255)   
    phoneNumber = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    District = models.CharField(max_length=255)
    def __str__(self):
        return self.phoneNumber 

class MSMEs(models.Model):
    Fullname = models.CharField(max_length=255)   
    phoneNumber = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    District = models.CharField(max_length=255)
    def __str__(self):
        return self.phoneNumber         

        



    

