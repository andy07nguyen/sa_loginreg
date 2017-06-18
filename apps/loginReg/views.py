from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
# Create your views here.

def landing(request):

    return render(request, 'loginReg/landing.html')

def index(request):

    return render(request, 'loginReg/index.html')

def process(request):
    print "FROM VIEWS: ", request.POST
    user = User.objects.register(request.POST)
    return redirect('/')
