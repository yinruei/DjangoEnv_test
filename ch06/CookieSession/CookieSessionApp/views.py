from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def set_cookie(request,key=None,value=None):
    response = HttpResponse('Cookie 儲存完畢!')
    response.set_cookie(key,value,max_age=1000)
    return response

def get_cookie(request,key=None,value=None):
    if key in request.COOKIES:
        return HttpResponse('%s : %s' %(key,request.COOKIES[key]))
    else:
        return HttpResponse('Cookie 不存在!')


def get_allcookies(request):
    if request.COOKIES != None:
        strcookies = ""
        for key1, value1 in request.COOKIES.items():
            strcookies = strcookies + key1 + ':' + value1 +'<br>'
        return HttpResponse(' %s ' %(strcookies))
    else:
        return HttpResponse('Cookie 不存在!')

def set_cookie2(request,key=None,value=None):
    response = HttpResponse('Cookie 有效時間')
    response.set_cookie(key, value, max_age=3600)
    return response

def delete_cookie(request,key=None,value=None):
    if key in request.COOKIES:
        response = HttpResponse('Delete COOKIE: '+key)
        response.delete_cookie(key)
        return response
    else:
        return HttpResponse('No cookies: '+key)

def index(request):
    if "counter" in request.COOKIES:
        counter=int(request.COOKIES["counter"])
        counter+=1
    else:
        counter=1
    response =HttpResponse('今日瀏覽次數: '+ str(counter))
    print(datetime.datetime.now())
    tomorrow = datetime.datetime.now()+ datetime.timedelta(days=1)
    print(tomorrow)
    tomorrow = datetime.datetime.replace(tomorrow,hour=0,minute=0,second=0)
    print(tomorrow)
    expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%y %H:%M:%S GMT")
    print(expires)
    response.set_cookie("counter",counter,expires=expires)
    return response

def set_session(request, key=None, value= None):
    response = HttpResponse('Session儲存完畢!')
    request.session[key] = value
    return response

def get_session(request, key=None):
    if key in request.session:
        return HttpResponse('%s : %s' % (key, request.session[key]))
    else:
        return HttpResponse('Session不存在!')

def get_allsessions(request):
    if request.session != None:
        strsession=""
        for key, value in request.session.items():
            strsession = strsession + key + ":" + str(value) +"<br>"
        return HttpResponse(strsession)
    else:
        return HttpResponse('Session 不存在!')