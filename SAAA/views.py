from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,'home.html')
def newuser(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
