from django.shortcuts import render
import africastalking
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
username = "nsabihamiss@gmail.com"
api_key = "7a6e5b772d94fc4af67cb8e9ac0b656af8ab659b27e422c2a1105d374bcb4662"
africastalking.initialize(username,api_key)
# Create your views here.
def welcome(request):
    return render(request,'index.html')
def Product(request): 
    return render(request,'Product.html') 

@csrf_exempt
def ussdapp(request):
    if request.method == 'POST':
        ## mandatory
        session_id = request.POST.get("sessionid")
        service_code = request.POST.get("servicecode")
        phone_number =request.POST.get("phonenumber")
        text = request.POST.get("text")
        level = text.split('*')
        response =""

        if text =='':
            response ="CON Welcome to ida technology USSD app \n"
            response +="1. Girls in code \n"
            response +="2. sdf program"
        elif text =="1" :
            response ="CON you selected Girls in code program \n" 
            response +="1. Join the program \n"
            response +="2. Get activity \n"
            response +="3. leave"
        elif text =="2" :
            response ="CON you selected Girls in code program \n" 
            response +="1. Join the program \n"
            response +="2. Get activity \n"
            response +="3. leave"

        else:
            response ="END invalid choice"    


        return HttpResponse(response)

    

    return HttpResponse('welcome')