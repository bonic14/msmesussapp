from django.shortcuts import render
import africastalking
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import*
from django.http import HttpResponse
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
        # newtext = request.POST.get("text")
        
        # select=SessionsModel.objects.filter(sessionID=session_id)
        
        # if select.exists():
            
        #     update = SessionsModel.objects.filter(sessionID=session_id).update(newsession=newtext)
        # else:
        #     insert = SessionsModel(sessionID=session_id,newsession=newtext)
        #     insert.save()
        # for nicole in select:              
        #     text=nicole.newsession


        level = text.split('*')
        response =""
        numb = text[:3]
        if text =='':
            response = "CON Welcome to IHUZO Rwanda  \n "
            response +="1. English \n"
            response +="2. Kinyarwanda"
        elif text == '1':
            # update = SessionsModel.objects.filter(sessionID=session_id).update(newsession='')
            response ="CON Register Here To The Digital Commerce Partners For Your Business \n"
            response +="1. Become an Iworkers\n"
            response +="2. Service Provider\n"
            response +="3. MSMEs\n"
            response +="0. Go Black"
           #===========become iworkers registration
        elif text == '1*1':
            response =" CON Register  to Become an iWorker  on Digital Platforms "+str(len(level))+"\n"
            response +="1. CAN\n"
            response +="2. RTN\n"
            response +="3. ABADASOBWA\n"
            response +="4. Digital Ambsasador\n"
            response +="5. Freelancers\n"
            response +="0. Go Black"
             #=========================CAN==========

        elif text == '1*1*1':
            response ="CON Enter your name \n"
        elif numb =='1*1*1' and int(len(level))==3 and str(level[2]) in str(level):
            response ="CON Enter your Age "
        elif numb =='1*1*1' and  int(len(level))==4 and str(level[3]) in str(level):
            response ="CON Enter your phone number"
        elif numb =='1*1*1' and  int(len(level))==5 and str(level[4]) in str(level):
            response ="CON Enter your District"

          #=========================RTN==========
        elif text == '1*1*2':
            response ="CON Enter your name \n"
        elif numb =='1*1*2' and int(len(level))==3 and str(level[2]) in str(level):
            response ="CON Enter your Age "
        elif numb =='1*1*2' and  int(len(level))==4 and str(level[3]) in str(level):
            response ="CON Enter your phone number"
        elif numb =='1*1*2' and  int(len(level))==5 and str(level[4]) in str(level):
            response ="CON Enter your District"   
        #=========================ABADASOBWA==========
        elif text == '1*1*3':
            response ="CON Enter your name "+str(len(level))+"\n"
        elif numb =='1*1*3' and int(len(level))==3 and str(level[2]) in str(level):
            response ="CON Enter your Age "
        elif numb =='1*1*3' and  int(len(level))==4 and str(level[3]) in str(level):
            response ="CON Enter your phone number"
        elif numb =='1*1*3' and  int(len(level))==5 and str(level[4]) in str(level):
            response ="CON Enter your District"  


         #=========================DIGITAL AMBASSADOR==========
        elif text == '1*1*4':
            response ="CON Enter your name "+str(len(level))+"\n"
        elif numb =='1*2' and int(len(level))==3 and str(level[2]) in str(level):
            response ="CON Enter your Age "
        elif numb =='1*2' and  int(len(level))==4 and str(level[3]) in str(level):
            response ="CON Enter your phone number"
        elif numb =='1*2' and  int(len(level))==5 and str(level[4]) in str(level):
            response ="CON Enter your District"   



        
         #===========DSP registration 
        elif text == '1*2':
            response ="CON Iworker Digital Platforms "+str(len(level))+"\n"
            response +="1. CAN\n"
            response +="2. RTN\n"
            response +="3. ABADASOBWA\n"
            response +="4. Digital Ambsasador\n"
            response +="0. Go Black"   




       

        #===========MSMEs registration
        elif text == '1*3':
            response ="CON Join Hundreds of  E-commerce & Digital Platforms  Register Your business Here "+str(len(level))+"\n"
            response +="1. AgriTech\n"
            response +="2. EdTech\n"
            response +="3. HeathTech\n"
            response +="4. IT & Hard Solutions\n"
            response +="5. E-Commerce\n"
            response +="6. Digital Infrastructure\n"
            response +="7. Others\n"
            response +="0. Go Black"   

        #===========agritech
        elif text == '1*3*1':
            response ="CON Enter your name \n"
        elif numb =='1*3*2' and int(len(level))==3 and str(level[2]) in str(level):
            response ="CON Enter your Age "
        elif numb =='1*3*3' and  int(len(level))==4 and str(level[3]) in str(level):
            response ="CON Enter your phone number"
        elif numb =='1*3*4' and  int(len(level))==5 and str(level[4]) in str(level):
            response ="CON Enter your District"    

        #===========edtech
        elif text == '1*3*2':
            response ="CON Enter your name \n"
        elif numb =='1*3*2' and int(len(level))==3 and str(level[2]) in str(level):
            response ="CON Enter your Age "
        elif numb =='1*3*3' and  int(len(level))==4 and str(level[3]) in str(level):
            response ="CON Enter your phone number"
        elif numb =='1*3*4' and  int(len(level))==5 and str(level[4]) in str(level):
            response ="CON Enter your District"























            #====================Registration in english end==================

             #====================iyandikishe mukinyarwanda biratangiye==================
        elif text =='2':
            response ="CON Urukaza neza kurubuga rw'IHUZO Rwanda Iyandikishe"+str(len(level))+"\n"
            response +="1. Become an Iworkers\n"
            response +="2. DSP Registration\n"
            response +="3. MSMEs\n"
            response +="4. Freelancers\n"
            response +="0. Gusubira inyuma " 
        elif text =='2*1':
            response ="CON Iworker Digital Platforms "+str(len(level))+"\n"
            response +="1. CAN\n"
            response +="2. RTN\n"
            response +="3. ABADASOBWA\n"
            response +="4. Digital Ambsasador\n"
            response +="5. Others \n"
            response +="0. Gusubira inyuma "
           
        elif text =='2*1*1':
            response ="CON ibiciro "+str(len(level))+"\n"
            response +="1. isaha imwe: \n"
            response +="2. amasaha abiri: \n"
            response +="3. amasaha atatu: \n"
            response +="4. amsaha ane: \n"
            response +="5. amasaha atantu: \n"
            response +="0. Gusubira inyuma: \n"
        elif text =='2*1*1*1' :   
            response ="CON umwirondoro wawe (amazina)"+str(len(level))+"\n"
            response +="0. Gusubira inyuma \n"
        elif text == '2*1*1*1*1':
            response ="CON shyiramo ahutuye "+str(len(level))+"\n"
            response +="0. Gusubira inyuma"
        elif text == '2*1*1*1*1*1':
            response ="CON shyiramo nimero ya telefone "+str(len(level))+""   



            #==========umunsi ntago urangiye haraburamo ibindi
          #hano icyumweru nihano gutangiriye  
        # elif text =='2*1*2':
        #     response ="CON ibiciro "+str(len(level))+"\n"
        #     response +="1. iminsi ibiri : \n"
        #     response +="2. iminsi itatu: \n"
        #     response +="3. iminsi ine: \n"
        #     response +="4. iminsi itantu: \n"
        #     response +="5. icyumweru cyose: \n"
        #     response +="0. Gusubira inyuma: \n"
        # elif text =='2*1*2*1' :   
        #     response ="CON umwirondoro wawe "+str(len(level))+"\n"
        #     response +=" shyiramo amazina yawe \n"    
        # elif text =='':
        #     response =""

        #   #icyumweru cyigombo kurangirira hano  
        # #========ukwezi kuratangiye======
        # elif text =='2*1*3':
        #     response ="CON ibiciro "+str(len(level))+"\n"
        #     response +="1. kabiri mukwezi: \n"
        #     response +="2. gatatu mukwezi: \n"
        #     response +="3. ukwezi kose: \n"
        #     response +="0. Gusubira inyuma: \n"
        # elif text =='2*1*3*1' :   
        #     response ="CON umwirondoro wawe "+str(len(level))+"\n"
        #     response +=" shyiramo amazina yawe \n"  
            

        else:
            response ="END Thank you For Registering  "    


        return HttpResponse(response)

    

    return HttpResponse('welcome')


def registration(request):
    
    #select =Registration.objects.all().filter(phone='0788978517').order_by('id')
    select =Registration.objects.all().order_by('id')
    if request.method =='POST':
        phone=request.POST['phone']
        firstname =request.POST['FirstName']
        lastname =request.POST['LastName']
        insert = Registration(phone=phone,firstname=firstname,lastname=lastname)
        try:
            insert.save()
            return render(request,'register.html',{'message': 'data has been inserted successful','data':select})
        except:
            return render(request,'register.html',{'message': 'fail to insert','data':select})
    return render(request,'register.html',{'data':select})

def delreg(request,id):
    select =Registration.objects.all().order_by('-id')
    deleteInfos=Registration.objects.get(id=id).delete()
    return render(request,'register.html',{'delmsg':'data has been deleted','data':select})

def updatereg(request,id):
    select =Registration.objects.all().order_by('-id')
    update =Registration.objects.get(id=id)
    if request.method=='POST':
        update.phone = request.POST['phone']
        update.firstname = request.POST['firstname']
        update.lastname = request.POST['lastname']
        try:
            update.save()
            return render(request,'updateregister.html',{'message':'data has been updated','data':select,'update':update})    
        except:
            return render(request,'updateregister.html',{'message':'data hasn failed','data':select,'update':update})

    return render(request,'updateregister.html',{'delmsg':'successful deleted','data':select,'update':update})

#===============buiding your endpoint
@csrf_exempt
def registerEndpoint(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        reg =Registration.objects.all()
        serializer = RegisterSerializers(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request) #request .data
        serializer = RegisterSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful','data':serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)

# delete/put/get single data
@csrf_exempt
def deleteEndpoint(request,id):
     
    if request.method == 'GET':
        reg =Registration.objects.get(id=id)
        serializer = RegisterSerializers(reg, many=False)
        return JsonResponse(serializer.data, safe=False)
    elif request.method =='DELETE':
        delete=Registration.objects.get(id=id).delete()
        return JsonResponse({'message':'data has been deleted'},status=490)

    elif request.method == 'PUT':
        reg =Registration.objects.get(id=id)
        data = JSONParser().parse(request) #request .data
        serializer = RegisterSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message':'successful','data':serializer.data}, status=201)
        return JsonResponse(serializer.errors, status=400)        