from django.shortcuts import render
from django.conf import settings

from django.http import HttpRequest,HttpResponse
from core.functions.functions import send_smtp_email
from .models import Contactus,Newsletter,Gallery,Testimonial
import os
import datetime

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
def index(request):
    # return HttpResponse('This is index page')
    category_types = Gallery.objects.values('type').distinct()
    testimonial_data = Testimonial.objects.filter(status='1').order_by('id')    
    context = {'page':'Home','category_types':category_types,'testimonial_data':testimonial_data}
    return render(request,'index.html',context=context)

def about(request):
    testimonial_data = Testimonial.objects.filter(status='1').order_by('id')
    category_types = Gallery.objects.values('type').distinct()
    return render(request,'about.html',context={'page':'About Us','testimonial_data':testimonial_data,'category_types':category_types})

def contact(request):
    category_types = Gallery.objects.values('type').distinct()
    context = {'page':'Contact Us','category_types':category_types}
    return render(request,'contact.html',context=context)

def insert_inquiry(request):
    # if request.POST:
    #     return HttpResponse(True)
    # else:
    #     return HttpResponse(request) 
    today = datetime.datetime.now() # Returns 2018-01-15 09:00    
    contact_us_obj = Contactus(name=request.POST['name'],email=request.POST['email'],subject=request.POST['subject'],message=request.POST['message'],created_at=today,updated_at=today)
    check_db = contact_us_obj.save()
    LastInsertId = (Contactus.objects.last()).id    
    if LastInsertId>0:
        #Send email
        subject = 'New inquiry received'
        message = f"Hello Admin,\n\n\n Name : {request.POST['name']}\n\n Email : {request.POST['email']}\n\n Subject : {request.POST['subject']}\n\n Message : {request.POST['message']}\n\n\nRegards,\nTeam Blog"
        send_smtp_email(['sheetalvishwakarma69106@gmail.com'],subject,message)
        return HttpResponse('success')
    else:
        return HttpResponse('error')
    
def insert_newsletter(request):
        today = datetime.datetime.now() # Returns 2018-01-15 09:00  
        if Newsletter.objects.filter(email=request.POST['email']).exists():  
             return HttpResponse('duplicate')
        else:
            newsletter_obj = Newsletter(email=request.POST['email'],is_subscribed='1',created_at=today,updated_at=today)
            newsletter_obj.save()
            LastInsertId = (Newsletter.objects.last()).id    
            if LastInsertId>0:
                return HttpResponse('success')
            else:
                return HttpResponse('error')
            
def courses(request):
    return render(request,'courses.html',context= {'page':'Courses'})   

def gallery(request):
    type = request.POST['category_type']
    # print('-------gallery_type-----')
    # print(type)
    # print('-------gallery_type-----')
    if(type=='all'):
        gallery = Gallery.objects.all().order_by('type')
    else:        
        gallery = Gallery.objects.filter(type=type).order_by('type')
    # print('gallery')
    # print(gallery)
    # print('gallery')
    page_name = f"Gallery - {type}"
    category_types = Gallery.objects.values('type').distinct()
    return render(request,'gallery.html',context={'page': page_name,'gallery':gallery,'category':type,'category_types':category_types})      

def terms_of_services(request):
    category_types = Gallery.objects.values('type').distinct()
    return render(request,'terms_of_services.html',context={'page': 'Terms of Service','category_types':category_types}) 

def privacy_policy(request):
    category_types = Gallery.objects.values('type').distinct()
    return render(request,'privacy_policy.html',context={'page': 'Privacy Policy','category_types':category_types})     

