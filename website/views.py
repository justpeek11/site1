from django.shortcuts import render

from django.http import HttpResponse

def home_view(request):
    return render(request,'home.html')

def about_view(request):
     return render(request, 'about.html')

def contact_view(request):
     return render(request, 'contact.html')