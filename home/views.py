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
        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST.get("text")
        level = text.split('*')
        response =""
        numb = text[:3]
        if text =='':
            response = "CON Welcome to ida technology USSD app \n "
            response +="1. Girls in code \n"
            response +="2. Sdf program "
        elif text =='1':
            response ="CON Welcome to Girls in code program "+str(len(level))+"\n"
            response +="1. Join the program \n"
            response +="2. Get activity \n"
            response +="3. Leave"
           #===========Girls in
        elif text == '1*1':
            response ="CON Enter your name "+str(len(level))+"\n"
        elif numb =='1*1' and int(len(level))==3 and str(level[2]) in str(level):
            response ="CON Enter your ID number"
        elif numb =='1*1' and  int(len(level))==4 and str(level[3]) in str(level):
            response ="CON Enter your pincode"
        elif text == '1*2':
            response ="CON Enter your pincode"
        elif text == '1*3':
            response ="CON Enter your pincode"
            #====================Girls end==================
        elif text =='2':
            response ="CON Welcome to Girls in code program "+str(level[0])+"\n"
            response +="1. Join the program \n"
            response +="2. Get activity \n"
            response +="3. Leave"
    

        else:
            response ="END invalid choice"    


        return HttpResponse(response)

    

    return HttpResponse('welcome')