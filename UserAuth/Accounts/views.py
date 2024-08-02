from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login_attempt(request):
    return render(request, 'login.html')

def register_attempt(request):
    return render(request, 'register.html')