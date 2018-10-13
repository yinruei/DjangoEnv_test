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

def post1(request):
    if request.method =="POST":
        cName = request.POST['cName']
        cSex  = request.POST['cSex']
        cBirthday = request.POST['cBirthday']
        cEmail = request.POST['cEmail']
        cPhone = request.POST['cPhone']
        cAddr = request.POST['cAddr']
        #新增一筆紀錄
        unit = student.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail, 
        cPhone=cPhone, cAddr=cAddr)
        unit.save()
        return redirect('/index/')
    else:
        message = '請輸入資料 (資料不做驗證)'
    return render(request, "post1.html", locals())