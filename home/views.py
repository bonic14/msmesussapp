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
            response = "CON Welcome to Rwandan Culture USSD app \n "
            response +="1. English \n"
            response +="2. Kinyarwanda"
        elif text =='1':
            response ="CON Welcome to Rwandan Culture platform "+str(len(level))+"\n"
            response +="1. Register to have account(sigin) \n"
            response +="0. Go Black"
           #===========culture in english
        elif text == '1*1':
            response ="CON Enter your email or phone number "+str(len(level))+"\n"
        elif numb =='1*1' and int(len(level))==3 and str(level[2]) in str(level):
            response ="CON Enter your password "
        elif numb =='1*1' and  int(len(level))==4 and str(level[3]) in str(level):
            response ="CON Enter your pincode"
        elif text == '1*2':
            response ="CON Enter your pincode"
        elif text == '1*3':
            response ="CON Enter your pincode"
            #====================culture in english end==================
        elif text =='2':
            response ="CON Urukaza neza kurubuga rw'umuco nyarwanda "+str(level[0])+"\n"
            response +="1. kwiyandikisha \n"
            response +="0. gusubira inyuma \n"
            
        elif text == '2*1':
            response ="CON  shyiramo nimero ya telefoni "+str(len(level))+"\n"
        elif numb =='2*1' and int(len(level))==3 and str(level[2]) in str(level):
            response ="CON urakoze kwiyandikisha kurubuga rw'umuco nyarwanda \n"  
            response +="1. Ushaka kwiga umuco nyarwanda \n"
            response +="2. Amatorero(atoza umuco nyarwanda) \n"
            response +="0. Gusubira inyuma " 
            
        elif numb =='2*1*1' and  int(len(level))==4 and str(level[3]) in str(level):
            response ="CON igihe cyigana gute?? \n"  
            response +="1. umunsi \n"
            response +="2. icyumweru \n"  
            response +="3. ukwezi \n"
            response +="0. Gusubira inyuma "

        elif numb =='2*1*1*1' and  int(len(level))==5 and str(level[4]) in str(level):   
            response ="CON ibiciro "
            response +="1. isaha imwe: \n"
            response +="2. amasaha abiri: \n"
            response +="3. amasaha atatu: \n"
            response +="4. amsaha ane: \n"
            response +="5. amasaha atantu: \n"
            response +="0. Gusubira inyuma: \n"

    

        else:
            response ="END invalid choice"    


        return HttpResponse(response)

    

    return HttpResponse('welcome')