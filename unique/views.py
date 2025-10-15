from django.shortcuts import render
from django.http import HttpResponse


def landingp(request):
    return render(request,'unique/lp.html')

def register(request):
    return render(request,'unique/regestratio.html')

def login(request):
    return render(request,'unique/login.html')
