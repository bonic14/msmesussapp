import csv
from django.shortcuts import render
import africastalking
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import*
from django.http import HttpResponse
from .models import Msmes
username = "ihuzo-rwanda"
api_key = "b93b4aa62515beb627442898bf8c6415baba7dd8bded3aefb93d53389f7f2150"
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

        nicole = text[:5]
        if text =='':
            response = "CON Welcome to MSMEs GO DIGITAL  \n "
            response +="1. English \n"
            response +="2. Kinyarwanda"
        elif text == '1':
            # update = SessionsModel.objects.filter(sessionID=session_id).update(newsession='')
            response ="CON MSMEs GO DIGITAL Expand your business on Digatal Platforms\n"
            response +="1. Register to MSMEs GO DIGITAL\n"
            
           #===========become msmes registration
        elif text == '1*1':
            response =" CON Choose Different Sector \n"
            response +="1. Retail shops&wholesalers \n"
            response +="2. Food & Beverages\n"
            response +="3. Hotel&Restaurant\n"
            response +="4. Agribusiness\n"
            response +="5. Constrution Material\n"
            response +="6. Arts&crafts\n"
            response +="7. Other"
            
 
        elif text == '1*1*1':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*1*1' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "
        elif nicole =='1*1*1' and int(len(level))== 5 and str(level[4]) in str(level):
            sector ='Retail shops&wholesalers'
            fullname= str(level[3])
            district=str(level[4])
            # namect=len(fullname)
            # dis=district.count() 
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response = "END Thank you for registering "
            # else:
            # response = "END Please Fill this space "+namect

        elif text == '1*1*2':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*1*2' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District " 
        elif nicole =='1*1*2' and int(len(level))== 5 and str(level[4]) in str(level):
            
            sector ='Food & Beverages'
            fullname= str(level[3])
            district=str(level[4])
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "    

        
        elif text == '1*1*3':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*1*3' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Enter Your District " 
        elif nicole =='1*1*3' and int(len(level))== 5 and str(level[4]) in str(level):
            sector ='Hotel&Restaurant'
            fullname= str(level[3])
            district=str(level[4])
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "    


         #=========================DIGITAL AMBASSADOR==========
        elif text == '1*1*4':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*1*4' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District " 
        elif nicole =='1*1*4' and int(len(level))== 5 and str(level[4]) in str(level):
            sector ='Agribusiness'
            fullname= str(level[3])
            district=str(level[4])
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "    

        elif text == '1*1*5':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*1*5' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District " 
        elif nicole =='1*1*5' and int(len(level))== 5 and str(level[4]) in str(level):
            sector ='Constrution Material'
            fullname= str(level[3])
            district=str(level[4])
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "    

       
        elif text == '1*1*6':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*1*6' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District " 
        elif nicole =='1*1*6' and int(len(level))== 5 and str(level[4]) in str(level):
            
            sector ='Arts&crafts'
            fullname= str(level[3])
            district=str(level[4])
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "      

        elif text == '1*1*7':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*1*7' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District " 
        elif nicole =='1*1*7' and int(len(level))== 5 and str(level[4]) in str(level):
            
            sector ='Other'
            fullname= str(level[3])
            district=str(level[4])
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "      





        



            #====================Registration in english end==================

             #====================iyandikishe mukinyarwanda biratangiye==================
        elif text =='2':
            response ="CON AGURA UBUCURUZI BWAWE WIFASHIJIJE IKORANABUHANGA\n"
            response +="1. Kwiyandikisha mu guhuzwa n’umufasha mu bucuruzi\n"
            
          
        elif text =='2*1':
            response ="CON Ingeriz'ubucuruzi \n"
            response +="1. Amaduka\n"
            response +="2. Amafunguro n'ibinyobwa\n"
            response +="3. Hoteli na Resitora\n"
            response +="4. Ibikomoka kubuhinzi\n"
            response +="5. Ibikoresho byubwubatsi \n"
            response +="6. Ubugeni n'ubukorikori \n"
            response +="7. Ubundi Bucuruzi"
            

        
        elif text == '2*1*1':
            response ="CON Andika amazina yawe \n"
        elif nicole =='2*1*1' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Andika akarere utuyemo"
        elif nicole == '2*1*1'and int(len(level))== 5 and str(level[4]) in str(level):
            sector ='Retail shops&wholesalers'
            fullname= str(level[3])
            district=str(level[4])
            # namect=len(fullname)
            # dis=district.count() 
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()  
            response ="END Murakoze kwiyandikisha ku rubuga rwa MSMEs  "   


        elif text == '2*1*2':
            response ="CON Andika amazina yawe \n"
        elif nicole =='2*1*2' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Andika akarere utuyemo"
        elif nicole == '2*1*2'and int(len(level))== 5 and str(level[4]) in str(level):
            sector ='Food & Beverages'
            fullname= str(level[3])
            district=str(level[4])
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()  
            response ="END Murakoze kwiyandikisha ku rubuga rwa MSMEs "    

        elif text == '2*1*3':
            response ="CON Andika amazina yawe \n"
        elif nicole =='2*1*3' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Andika akarere utuyemo"
        elif nicole == '2*1*3'and int(len(level))== 5 and str(level[4]) in str(level):
            sector ='Hotel&Restaurant'
            fullname= str(level[3])
            district=str(level[4])
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save() 
            response ="END Murakoze kwiyandikisha ku rubuga rwa MSMEs "    


         
        elif text == '2*1*4':
            response ="CON Andika amazina yawe \n"
        elif nicole =='2*1*4' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Andika akarere utuyemo"
        elif nicole == '2*1*4'and int(len(level))== 5 and str(level[4]) in str(level):
            sector ='Agribusiness'
            fullname= str(level[3])
            district=str(level[4])
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()  
            response ="END Murakoze kwiyandikisha ku rubuga rwa MSMEs "    

       
        elif text == '2*1*5':
            response ="CON Andika amazina yawe \n"
        elif nicole =='2*1*5' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Andika akarere utuyemo"
        elif nicole == '2*1*5'and int(len(level))== 5 and str(level[4]) in str(level): 
            sector ='Constrution Material'
            fullname= str(level[3])
            district=str(level[4])
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Murakoze kwiyandikisha ku rubuga rwa MSMEs " 
       
        elif text == '2*1*6':
            response ="CON Andika amazina yawe \n"
        elif nicole =='2*1*6' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Andika akarere utuyemo"
        elif nicole == '2*1*6'and int(len(level))== 5 and str(level[4]) in str(level): 
            sector ='Arts&crafts'
            fullname= str(level[3])
            district=str(level[4])
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Murakoze kwiyandikisha ku rubuga rwa MSMEs  "  

        elif text == '2*1*7':
            response ="CON Andika amazina yawe \n"
        elif nicole =='2*1*7' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Andika akarere utuyemo"
        elif nicole == '2*1*7'and int(len(level))== 5 and str(level[4]) in str(level): 
            sector ='Other'
            fullname= str(level[3])
            district=str(level[4])
            reg = Msmes(sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save() 
            response ="END Murakoze kwiyandikisha ku rubuga rwa MSMEs "       
            




        
               


          
           



         
            

        else:
            response ="END Invalid choice "   



        return HttpResponse(response)


    ######csv file ####################
    

    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['category','sector','Fullname','District','phoneNumber'])

    for member in Ihuzo.objects.all().values_list('category','sector','Fullname','District','phoneNumber'):
        writer.writerow(ihuzo)
    response ['Content-Disposition'] = 'attachment; filename="ihuzos.csv"'    
    return response


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