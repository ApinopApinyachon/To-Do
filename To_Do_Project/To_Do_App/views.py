from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Main(request):
    return HttpResponse ("<h1>Rachapro</>")

def base(request):
    return render (request,"base.html")

def Login(request):
    return render (request,"login.html")