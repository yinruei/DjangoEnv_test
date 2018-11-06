from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def set_cookie(request,key=None,value=None):
    response = HttpResponse('Cookie 儲存完畢!')
    response.set_cookie(key,value)
    return response

def get_cookie(request,key=None,value=None):
    if key in request.COOKIES:
        return HttpResponse('%s : %s' %(key,request.COOKIES[key]))
    else:
        return HttpResponse('Cookie 不存在!')

def get_allcookies(request):
    if request.COOKIES !=None:
        strcookies=""
        for key1,value1 in request.COOKIES.items():
            strcookies=strcookies + key1 + ":" + value1 +"<br>"
        return HttpResponse('%s' %(strcookies))
    else:
        return HttpResponse('Cookie 不存在!')