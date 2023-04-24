from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def mahi(request):
    res=HttpResponse("<html><body bgcolor=purple><h1><center>DESIGN QR-CODE PROJECT</center></h1></body></html>")
    return res