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

        nicole = text[:5]
        if text =='':
            response = "CON MURAKAZA NEZA KURI MSMES GO DIGITAL\n "
            response +=" AGURA UBUCURUZI BWAWE WIFASHIJE IKORANABUHANGA\n"
            response +="1.Kwiyandikisha"
            
        elif text == '1':
            # update = SessionsModel.objects.filter(sessionID=session_id).update(newsession='')
            response ="CON Iyandikishe muguhuzwa n'umufasha mubucuruzi,Ingeri z'ubucuruzi \n"
            response +="1. Amaduka\n"
            response +="2. Amafunguro n'ibinyobwa\n"
            response +="3. Hoteli na Resitora\n"
            response +="4. Ibikomoka Kubuhinzi\n"
            response +="5. Ibikoresho byubwubatsi\n"
            response +="6. Ubugeni n'ubukorikori\n"
            response +="7. Ubundi bucuruzi\n"
           #===========become iworkers registration
        elif text == '1*1':
            response ="CON Andika amazina yawe \n"
        elif nicole =='2*1*1' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Andika akarere utuyemo"
        elif nicole == '2*1*1'and int(len(level))== 5 and str(level[4]) in str(level):
            response +="0. Go Black"
             #=========================CAN==========
 
        elif text == '1*1*1':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*1*1' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "
        elif nicole =='1*1*1' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Iworkers'
            sector ='CAN'
            fullname= str(level[3])
            district=str(level[4])
            # namect=len(fullname)
            # dis=district.count()
            # if name >=2: 
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response = "END Thank you for registering "
            # else:
            # response = "END Please Fill this space "+namect

      
      
          #=========================RTN==========
        elif text == '1*1*2':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*1*2' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District " 
        elif nicole =='1*1*2' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Iworkers'
            sector ='RTN'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "    

        #=========================ABADASOBWA==========
        elif text == '1*1*3':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*1*3' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Enter Your District " 
        elif nicole =='1*1*3' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Iworkers'
            sector ='ABADASOBWA'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "    


         #=========================DIGITAL AMBASSADOR==========
        elif text == '1*1*4':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*1*4' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District " 
        elif nicole =='1*1*4' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Iworkers'
            sector ='Digital Ambsasador'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "    

         #=========================freelancers==========
        elif text == '1*1*5':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*1*5' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District " 
        elif nicole =='1*1*5' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Iworker'
            sector ='Freelancers'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "    

        #=========================other iworker==========
        elif text == '1*1*6':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*1*6' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District " 
        elif nicole =='1*1*6' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Iworker'
            sector ='Others'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "      





        
         #===========DSP registration 
        elif text == '1*2':
            response ="CON What  services do you offer \n"
            response +="1. Egovernment Services\n"
            response +="2. Financial Services\n"
            response +="3. Real estate Services\n"
            response +="4. Internet Services\n"
            response +="5. Insurance Services\n"
            response +="6. Translation Services\n"
            response +="7. App developer\n"
            response +="8. Others\n"
              

         #=========================EGORVERNMENT==========
        elif text == '1*2*1':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*2*1' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District " 
        elif nicole =='1*2*1' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Service Provider'
            sector ='Egovernment Services'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "    

        #=========================finacial==========
        elif text == '1*2*2':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*2*2' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District " 
        elif nicole =='1*2*2' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Service Provider'
            sector ='Financial Services'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "  



         #=========================Real estate services==========
        elif text == '1*2*3':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*2*3' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter  Your District " 
        elif nicole =='1*2*3' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Service Provider'
            sector ='Real estate services'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "   

        #=========================internet services==========
        elif text == '1*2*4':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*2*4' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter  Your District " 
        elif nicole =='1*2*4' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Service Provider'
            sector ='Internet services'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering " 

        #=========================insurance==========
        elif text == '1*2*5':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*2*5' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter  Your District " 
        elif nicole =='1*2*5' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Service Provider'
            sector ='Insurance services'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering " 

        #=========================translation services==========
        elif text == '1*2*6':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*2*6' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter  Your District " 
        elif nicole =='1*2*6' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Service Provider'
            sector ='Translation services'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering " 

        #=========================app developer==========
        elif text == '1*2*7':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*2*7' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter  Your District " 
        elif nicole =='1*2*7' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Service Provider'
            sector ='App developer services'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering " 

        #=========================others==========
        elif text == '1*2*8':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*2*8' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter  Your District " 
        elif nicole =='1*2*8' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Service Provider'
            sector ='other services'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "                       




       

        #===========MSMEs registration
        elif text == '1*3':
            response ="CON Which business to register for Ihuzo \n"
            response +="1. AgriBusiness\n"
            response +="2. Schools&training providers\n"
            response +="3. Multimedia&Photography\n"
            response +="4. ICT products&Services\n"
            response +="5. Retail shops&wholesalersn"
            response +="6. Travel tours,hotels&restaurants\n"
            response +="7. Arts,crafts&fashion\n"
            response +="8. Others\n"
              

        #===========agritech
        elif text == '1*3*1':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*3*1' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "     
        elif nicole =='1*3*1' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector ='AgriBusiness'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "   

        #===========edtech
        elif text == '1*3*2':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*3*2' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "
        elif nicole =='1*3*2' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector ='Education'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "

        #===========Multimedia
        elif text == '1*3*3':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*3*3' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "  
        elif nicole =='1*3*3' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector ='Multimedia'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "  

        #===========ICT 
        elif text == '1*3*4':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*3*4' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "
        elif nicole =='1*3*4' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector ='ICT products&services'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "

        #===========trading
        elif text == '1*3*5':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*3*5' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "
        elif nicole =='1*3*5' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector ='Trading'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "     

        #===========tourism
        elif text == '1*3*6':
            response ="CON Enter Your Fullname "+str(len(level))+"\n"
        elif nicole =='1*3*6' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "   
        elif nicole =='1*3*6' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector = 'Tourism'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "          

        #===========arts&crafts
        elif text == '1*3*7':
            response ="CON Enter Your Fullname "+str(len(level))+"\n"
        elif nicole =='1*3*7' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "
        elif nicole =='1*3*7' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector = 'Arts&Crafts'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "  

        #===========other business
        elif text == '1*3*8':
            response ="CON Enter Your Fullname "+str(len(level))+"\n"
        elif nicole =='1*3*8' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "
        elif nicole =='1*3*8' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector = 'Others'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "      





















        #     #====================Registration in english end==================

        #      #====================iyandikishe mukinyarwanda biratangiye==================
        # elif text =='2':
        #     response ="CON Kwiyandikisha mu guhuzwa n’umufasha mu bucuruzi\n"
        #     response +="1. Kuba umuhuza\n"
        #     response +="2. Utanga serivisi\n"
        #     response +="3. Ubucuruzi buto, ubuciriritse n’uburinganiye\n"
          
        # elif text =='2*1':
        #     response ="CON Kwiyandikisha nk’umuhuza \n"
        #     response +="1. Umukozi wa CAN\n"
        #     response +="2. Umukozi wa RTN\n"
        #     response +="3. ABADASOBWA\n"
        #     response +="4. Umuhuza mu ikoranabuhanga\n"
        #     response +="5. Klab freelancers \n"
        #     response +="6. Undi muhuza \n"
            

        #  #=========================CAN==========
        # elif text == '2*1*1':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*1*1' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*1*1'and int(len(level))== 5 and str(level[4]) in str(level):
        #     category = 'Iworkers'
        #     sector ='CAN'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()   
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "   

        #  #=========================RTN==========
        # elif text == '2*1*2':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*1*2' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*1*2'and int(len(level))== 5 and str(level[4]) in str(level):
        #     category = 'Iworkers'
        #     sector ='RTN'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()  
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "    

        # #=========================ABADASOBWA==========
        # elif text == '2*1*3':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*1*3' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*1*3'and int(len(level))== 5 and str(level[4]) in str(level):
        #     category = 'Iworkers'
        #     sector ='ABADASOBWA'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()  
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "    


        #  #=========================UMUHUZA MU IKORANABUHANGA==========
        # elif text == '2*1*4':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*1*4' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*1*4'and int(len(level))== 5 and str(level[4]) in str(level):
        #     category = 'Iworkers'
        #     sector ='Digital Ambsasador'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()  
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "    

        #  #=========================freelancers==========
        # elif text == '2*1*5':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*1*5' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*1*5'and int(len(level))== 5 and str(level[4]) in str(level): 
        #     category = 'Iworker'
        #     sector ='Freelancers'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save() 
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  " 
        #  #=========================izindi serivisi==========
        # elif text == '2*1*6':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*1*6' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*1*6'and int(len(level))== 5 and str(level[4]) in str(level): 
        #     category = 'Iworker'
        #     sector ='Others'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save() 
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "    
            




        
        #  #==========UTANGA SERIVICE 
        # elif text == '1*2':
        #     response ="CON Ni izihe serivisi utanga \n"
        #     response +="1. Serivisi za leta\n"
        #     response +="2. Servisi za amafaranga (banki, irembo, Forex bureau, etc.)\n"
        #     response +="3. Serivisi z’ubutaka\n"
        #     response +="4. Serivisi za interineti\n"
        #     response +="5. Serivisi z’ubwishingizi\n"
        #     response +="6. Ivunjisha\n"
        #     response +="7. Gukora porogaramu za terefoni\n"
        #     response +="8. Izindi Serivisi\n"
               

        #  #=========================EGORVERNMENT==========
        # elif text == '2*2*1':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*2*1' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*2*1'and int(len(level))== 5 and str(level[4]) in str(level): 
        #     category = 'Service Provider'
        #     sector ='Egovernment Services'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "    

        # #=======================financial servie==========
        # elif text == '2*2*2':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*2*2' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo" 
        # elif nicole == '2*2*2'and int(len(level))== 5 and str(level[4]) in str(level): 
        #     category = 'Service Provider'
        #     sector ='Financial Services'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save() 
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "  


        #  #=========================real estate==========
        # elif text == '2*2*3':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*2*3' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*2*3'and int(len(level))== 5 and str(level[4]) in str(level):
        #     category = 'Service Provider'
        #     sector ='Real estate services'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()  
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "    

        # #=========================internnet ==========
        # elif text == '2*2*4':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*2*4' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*2*4'and int(len(level))== 5 and str(level[4]) in str(level):
        #     category = 'Service Provider'
        #     sector ='Internet services'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()  
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "        


        # #=========================insurance==========
        # elif text == '2*2*5':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*2*5' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*2*5'and int(len(level))== 5 and str(level[4]) in str(level): 
        #     category = 'Service Provider'
        #     sector ='Insurance services'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save() 
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "    

        # #=========================forin exchange==========
        # elif text == '2*2*6':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*2*6' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*2*6'and int(len(level))== 5 and str(level[4]) in str(level):
        #     category = 'Service Provider'
        #     sector ='Translation services'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()  
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "    
        # #=========================app developer==========
        # elif text == '2*2*7':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*2*7' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*2*7'and int(len(level))== 5 and str(level[4]) in str(level):
        #     category = 'Service Provider'
        #     sector ='App developer services'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()  
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "    

        # #=========================ibindi==========
        # elif text == '2*2*8':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*2*8' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*2*8'and int(len(level))== 5 and str(level[4]) in str(level):
        #     category = 'Service Provider'
        #     sector ='Others'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "                




       

        # #===========ubucuruzi buto nubucuriritse
        # elif text == '2*3':
        #     response ="CON Ni ubuhe bucuruzi wandikisha?  \n"
        #     response +="1. Ubuhinzi bugamije ubucuruzi\n"
        #     response +="2. Ibigo by’amashuri n’abatanga amahugurwa\n"
        #     response +="3. Itangazamakuru no gufata amafoto\n"
        #     response +="4. Abatekinisiye mu ikoranabuhanga\n"
        #     response +="5. Amaduka n’abaranguza\n"
        #     response +="6. Ubukerarugendo, amahoteri n’amaresitora\n"
        #     response +="7. Ubugeni n’imideri\n"
        #     response +="8. Ubundi bucuruzi\n"
             

        # #===========agritech
        # elif text == '2*3*1':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*3*1' and int(len(level))== 4 and str(level[3]) in str(level):
        #      response = "CON Andika akarere utuyemo"
        # elif nicole == '2*3*1'and int(len(level))== 5 and str(level[4]) in str(level): 
        #     category = 'MSMEs'
        #     sector ='AgriBusiness'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save() 
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "   

        # #===========education
        # elif text == '2*3*2':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*3*2' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*3*2'and int(len(level))== 5 and str(level[4]) in str(level):  
        #     category = 'MSMEs'
        #     sector ='Education'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "   

        # #===========HeathTech
        # elif text == '2*3*3':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*3*3' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"     
        # elif nicole == '2*3*3'and int(len(level))== 5 and str(level[4]) in str(level):  
        #     category = 'MSMEs'
        #     sector ='Multimedia'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "    

        # #===========IT & Hard Solutions
        # elif text == '2*3*4':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*3*4' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"     
        # elif nicole == '2*3*4'and int(len(level))== 5 and str(level[4]) in str(level):  
        #     category = 'MSMEs'
        #     sector ='ICT products&services'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "   

        # #===========trading
        # elif text == '2*3*5':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*3*5' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*3*5'and int(len(level))== 5 and str(level[4]) in str(level):  
        #     category = 'MSMEs'
        #     sector ='Trading'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo  "        

        # #===========tourism
        # elif text == '2*3*6':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*3*6' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response = "CON Andika akarere utuyemo"
        # elif nicole == '2*3*6'and int(len(level))== 5 and str(level[4]) in str(level):  
        #     category = 'MSMEs'
        #     sector = 'Tourism'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo " 
        # #=======================arts and craft
        # elif text == '2*3*7':
        #     response ="CON Andika amazina yawe \n"
        # elif nicole =='2*3*7' and int(len(level))== 4 and str(level[3]) in str(level):
        #    response = "CON Andika akarere utuyemo" 
        # elif nicole == '2*3*7'and int(len(level))== 5 and str(level[4]) in str(level):  
        #     category = 'MSMEs'
        #     sector = 'Arts&Crafts'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo "  

        # #===========other business
        # elif text == '2*3*8':
        #     response ="CON  Andika amazina yawe \n"
        # elif nicole =='2*3*8' and int(len(level))== 4 and str(level[3]) in str(level):
        #     response ="CON  Andika akarere utuyemo "
        # elif nicole =='2*3*8' and int(len(level))== 5 and str(level[4]) in str(level):
        #     category = 'MSMEs'
        #     sector = 'Others'
        #     fullname= str(level[3])
        #     district=str(level[4])
        #     reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
        #     reg.save()
        #     response ="END Murakoze kwiyandikisha ku rubuga rw'iHuzo "             


          
           



         
            

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