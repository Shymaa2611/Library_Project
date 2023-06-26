from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import client_data,company,services,Locations

def index(request):
  data=ContactForm()
  if request.method=='POST':
   data=ContactForm(request.POST)
   if data.is_valid():
      data.save()
  redirect('/')
      
  context={
      'data':company.objects.all(),
      'service':services.objects.all(),
      'location':Locations.objects.all(),
      'form':ContactForm()
   }

  return render(request,'pages/index.html',context)

def about(request):
  
   return render(request,'pages/about.html')


def blog(request):
  
   return render(request,'pages/blog.html')


def contact(request):
  data=ContactForm()
  if request.method=='POST':
   data=ContactForm(request.POST)
   if data.is_valid():
      data.save()
  context={
      'data':client_data.objects.all(),
      'form':data
   }

  return render(request,'pages/contact.html',context)

def service(request):
  context={
    'service':services.objects.all()
  }
  return render(request,'pages/service.html',context)

def locations(request):
  context={
    'location':Locations.objects.all()
  }
  return render(request,'pages/locations.html',context)




