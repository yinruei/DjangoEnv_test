from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
# Create your views here.

def sayhello(request):
    return HttpResponse("Hello Django !")
def hello2(request,username):
    return HttpResponse("Hello "+ username)
def hello3(request,username):
    now = datetime.now()
    return render(request,"hello3.html",locals())
def hello4(request,username):
    now = datetime.now()
    return render(request,"hello4.html",locals())

