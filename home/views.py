import csv
from django.shortcuts import render
import africastalking
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import*
from django.http import HttpResponse
from .models import Ihuzo
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
            response = "CON Welcome to IHUZO Rwanda  \n "
            response +="1. English \n"
            response +="2. Kinyarwanda"
        elif text == '1':
            # update = SessionsModel.objects.filter(sessionID=session_id).update(newsession='')
            response ="CON Register Here To The Digital Commerce Partners For Your Business \n"
            response +="1. Become an Iworkers\n"
            response +="2. Service Provider\n"
            response +="3. Business\n"
           #===========become iworkers registration
        elif text == '1*1':
            response =" CON Register  to Become an iWorker  on Digital Platforms \n"
            response +="1. CAN Agents \n"
            response +="2. RTN Agents\n"
            response +="3. ABADASOBWA\n"
            response +="4. Digital Ambsasador\n"
            response +="5. Klab Freelancers \n"
            response +="6. Other\n"
            # response +="0. Go Black"
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
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response = "END Thank you for registering "
      
      
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



        
         #===========DSP registration 
        elif text == '1*2':
            response ="CON What Digital Service do you Provider \n"
            response +="1. Egovernment Services\n"
            response +="2. Film&other multimedia\n"
            response +="3. Application Web Development\n"
            response +="4. Others\n"
              

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

        #=========================Film&other multimedia==========
        elif text == '1*2*2':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*2*2' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District " 
        elif nicole =='1*2*2' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Service Provider'
            sector ='Film&other multimedia'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "    


         #=========================Application Web Development==========
        elif text == '1*2*3':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*2*3' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter  Your District " 
        elif nicole =='1*2*3' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Service Provider'
            sector ='Application Web Development'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "     




       

        #===========MSMEs registration
        elif text == '1*3':
            response ="CON What kind of Business are you,Register Your business Here \n"
            response +="1. Agriculture\n"
            response +="2. Education\n"
            response +="3. Heath\n"
            response +="4. IT & Hardware Solutions\n"
            response +="5. E-Commerce\n"
            response +="6. Digital Infrastructure\n"
            response +="7. Finacial \n"
            response +="8. Others\n"
              

        #===========agritech
        elif text == '1*3*1':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*3*1' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "     
        elif nicole =='1*3*1' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector ='AgriTech'
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
            sector ='EdTech'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "

        #===========HeathTech
        elif text == '1*3*3':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*3*3' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "  
        elif nicole =='1*3*3' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector ='HeathTech'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "  

        #===========IT & Hard Solutions
        elif text == '1*3*4':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*3*4' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "
        elif nicole =='1*3*4' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector ='IT & Hard Solutions'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "

        #===========E-Commerce
        elif text == '1*3*5':
            response ="CON Enter Your Fullname \n"
        elif nicole =='1*3*5' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "
        elif nicole =='1*3*5' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector ='E-Commerce'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "     

        #===========Digital Infrastructure
        elif text == '1*3*6':
            response ="CON Enter Your Fullname "+str(len(level))+"\n"
        elif nicole =='1*3*6' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "   
        elif nicole =='1*3*6' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector = 'Digital Infrastructure'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "          

        #===========FINTECH
        elif text == '1*3*7':
            response ="CON Enter Your Fullname "+str(len(level))+"\n"
        elif nicole =='1*3*7' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Enter Your District "
        elif nicole =='1*3*7' and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'MSMEs'
            sector = 'FinTech'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()
            response ="END Thank you for registering "  





















            #====================Registration in english end==================

             #====================iyandikishe mukinyarwanda biratangiye==================
        elif text =='2':
            response ="CON Kwiyandikisha mu guhuzwa n’umufasha mu bucuruzi\n"
            response +="1. Kuba umuhuza\n"
            response +="2. Utanga serivisi\n"
            response +="3. Ubucuruzi buto, ubuciriritse n’uburinganiye\n"
          
        elif text =='2*1':
            response ="CON Kwiyandikisha nk’umuhuza \n"
            response +="1. CAN\n"
            response +="2. RTN\n"
            response +="3. ABADASOBWA\n"
            response +="4. Umuhuza mu ikoranabuhanga\n"
            response +="5. klab freelancers \n"
            response +="6. ibindi \n"
            

         #=========================CAN==========
        elif text == '2*1*1':
            response ="CON Shyiramo amazina yawe \n"
        elif nicole =='2*1*1' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Shiramo Akarere utuyemo"
        elif nicole == '2*1*1'and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Iworkers'
            sector ='CAN'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()   
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "   

         #=========================RTN==========
        elif text == '2*1*2':
            response ="CON Shyiramo amazina yawe \n"
        elif nicole =='2*1*2' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Shiramo Akarere utuyemo"
        elif nicole == '2*1*2'and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Iworkers'
            sector ='RTN'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()  
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "    

        #=========================ABADASOBWA==========
        elif text == '2*1*3':
            response ="CON Shyiramo amazina yawe \n"
        elif nicole =='2*1*3' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Shiramo Akarere utuyemo"
        elif nicole == '2*1*3'and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Iworkers'
            sector ='ABADASOBWA'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()  
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "    


         #=========================UMUHUZA MU IKORANABUHANGA==========
        elif text == '2*1*4':
            response ="CON Shyiramo amazina yawe \n"
        elif nicole =='2*1*4' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Shiramo Akarere utuyemo"
        elif nicole == '2*1*4'and int(len(level))== 5 and str(level[4]) in str(level):
            category = 'Iworkers'
            sector ='Digital Ambsasador'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save()  
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "    

         #=========================freelancers==========
        elif text == '2*1*5':
            response ="CON Shyiramo amazina yawe \n"
        elif nicole =='2*1*5' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Shiramo Akarere utuyemo"
        elif nicole == '2*1*5'and int(len(level))== 5 and str(level[4]) in str(level): 
            category = 'Iworker'
            sector ='Freelancers'
            fullname= str(level[3])
            district=str(level[4])
            reg = Ihuzo(category=category,sector=sector,Fullname=fullname,District=district,phoneNumber=phone_number,email='')
            reg.save() 
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "         



        
         #==========UTANGA SERIVICE 
        elif text == '1*2':
            response ="CON Utanga Serivice \n"
            response +="1. Ikoranabuhanga muri guverinoma\n"
            response +="2. Film&other multimedia\n"
            response +="3. Application Web Development\n"
            response +="4. Ibindi\n"
               

         #=========================EGORVERNMENT==========
        elif text == '2*2*1':
            response ="CON Shyiramo amazina yawe \n"
        elif nicole =='2*2*1' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Shiramo Akarere utuyemo"
        elif nicole == '2*2*1'and int(len(level))== 5 and str(level[4]) in str(level):  
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "    

        #=========================Film&other multimedia==========
        elif text == '2*2*2':
            response ="CON Shyiramo amazina yawe \n"
        elif nicole =='2*2*2' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Shiramo Akarere utuyemo" 
        elif nicole == '2*2*2'and int(len(level))== 5 and str(level[4]) in str(level):  
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "  


         #=========================Application Web Development==========
        elif text == '2*2*3':
            response ="CON Shyiramo amazina yawe \n"
        elif nicole =='2*2*3' and int(len(level))== 4 and str(level[3]) in str(level):
            response = "CON Shiramo Akarere utuyemo"
        elif nicole == '2*2*3'and int(len(level))== 5 and str(level[4]) in str(level):  
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "    




       

        #===========ubucuruzi buto nubucuriritse
        elif text == '2*3':
            response ="CON Kwandikisha ubucuruzi ku mbuga zicururizwaho kuri interineti \n"
            response +="1. Ikoranabuhanga mu buhinzi\n"
            response +="2. Ikoranabuhanga mu burezi\n"
            response +="3. Ikoranabuhanga mu buvuzi\n"
            response +="4. Ikoranabuhanga mu gukemura ibibazo\n"
            response +="5. Ubucuruzi bwo kuri interineti\n"
            response +="6. Ikoranabuhanga mu ibikorwa remezo\n"
            response +="7. Ikoranabuhanga mu guhererekanya amafaranga\n"
            response +="8. Ibindi\n"
             

        #===========agritech
        elif text == '2*3*1':
            response ="CON Shyiramo amazina yawe \n"
        elif nicole =='2*3*1' and int(len(level))== 4 and str(level[3]) in str(level):
             response = "CON Shiramo Akarere utuyemo"
        elif nicole == '2*3*1'and int(len(level))== 5 and str(level[4]) in str(level):  
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "   

        #===========edtech
        elif text == '2*3*2':
            response ="CON Shyiramo amazina yawe \n"
        elif nicole =='2*3*2' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Shyiramo nimero ya telefone yawe "
        elif nicole == '2*3*2'and int(len(level))== 5 and str(level[4]) in str(level):  
            response = "CON Shiramo Akarere utuyemo"     
        elif nicole =='2*3*2' and int(len(level))== 6 and str(level[5]) in str(level):
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "   

        #===========HeathTech
        elif text == '2*3*3':
            response ="CON Shyiramo amazina yawe "+str(len(level))+"\n"
        elif nicole =='2*3*3' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Shyiramo nimero ya telefone yawe "
        elif nicole == '2*3*3'and int(len(level))== 5 and str(level[4]) in str(level):  
            response = "CON Shiramo Akarere utuyemo"     
        elif nicole =='2*3*3' and int(len(level))== 6 and str(level[5]) in str(level):
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "    

        #===========IT & Hard Solutions
        elif text == '2*3*4':
            response ="CON Shyiramo amazina yawe "+str(len(level))+"\n"
        elif nicole =='2*3*4' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Shyiramo nimero ya telefone yawe "
        elif nicole == '2*3*4'and int(len(level))== 5 and str(level[4]) in str(level):  
            response = "CON Shiramo Akarere utuyemo"     
        elif nicole =='2*3*4' and int(len(level))== 6 and str(level[5]) in str(level):
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "   

        #===========E-Commerce
        elif text == '2*3*5':
            response ="CON Shyiramo amazina yawe "+str(len(level))+"\n"
        elif nicole =='2*3*5' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Shyiramo nimero ya telefone yawe "
        elif nicole == '2*3*5'and int(len(level))== 5 and str(level[4]) in str(level):  
            response = "CON Shiramo Akarere utuyemo"     
        elif nicole =='2*3*5' and int(len(level))== 6 and str(level[5]) in str(level):
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "        

        #===========E-Digital Infrastructure
        elif text == '2*3*6':
            response ="CON Shyiramo amazina yawe \n"
        elif nicole =='2*3*6' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Shyiramo nimero ya telefone yawe "
        elif nicole == '2*3*6'and int(len(level))== 5 and str(level[4]) in str(level):  
            response = "CON Shiramo Akarere utuyemo"     
        elif nicole =='2*3*6' and int(len(level))== 6 and str(level[5]) in str(level):
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo " 
        #=======================fintech
        elif text == '2*3*7':
            response ="CON Shyiramo amazina yawe \n"
        elif nicole =='2*3*7' and int(len(level))== 4 and str(level[3]) in str(level):
            response ="CON Shyiramo nimero ya telefone yawe "
        elif nicole == '2*3*7'and int(len(level))== 5 and str(level[4]) in str(level):  
            response = "CON Shiramo Akarere utuyemo"     
        elif nicole =='2*3*7' and int(len(level))== 6 and str(level[5]) in str(level):
            response ="END Murakoze kwiyandikisha kurubuga rw'ihuzo "              
          
           



         
            

        else:
            response ="END Invalid choice "   



        return HttpResponse(response)


    ######csv file ####################
    

    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['category','sector','Fullname','District','phoneNumber'])

    for member in Member.objects.all().values_list('category','sector','Fullname','District','phoneNumber'):
        writer.writerow(member)
    response ['Content-Disposition'] = 'attachment; filename="members.csv"'    
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