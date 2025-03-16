#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("hey")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("hey2")
    return render(request, 'about.html')