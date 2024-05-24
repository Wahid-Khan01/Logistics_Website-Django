from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, 'about.html')

def fcl(request):
    return render(request, 'FCL.html')

def lcl(request):
    return render(request, 'LCL.html')

def airfreight(request):
    return render(request, 'airfreight.html')

def customclearance(request):
    return render(request, 'customclearance.html')

def industries(request):
    return render(request, 'industries.html')
# Create your views here.
