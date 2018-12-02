from django.shortcuts import render
from django.http import HttpResponse

def file(request):
    return render(request,'file.html')

 


 
