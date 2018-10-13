from django.shortcuts import render,redirect
from studentsapp.models import student

def listone(request): 
	try: 
		unit = student.objects.get(cName="李采茜") #讀取一筆資料
        # unit = student.objects.get(cPhone= "0914530768")
	except:
  		errormessage = " (讀取錯誤!)"
	return render(request, "listone.html", locals())

def listall(request):  
    students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "listall.html", locals())
	
def index(request):  
    students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "index.html", locals())	

def post(request):
    if request.method == "POST": #如果是以POST方式才處理
        mess = request.POST['username']#取得表單輸入資料
    else:
        mess = "表單資料尚未送出!"
    return render(request, "post.html", locals())
