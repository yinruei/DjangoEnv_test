from django.shortcuts import render,redirect
from studentsapp.models import student
from studentsapp.form import PostForm ##這邊是將form.py引入PostForm的類別

def listone(request): 
    try: 
        unit = student.objects.get(cName="李采茜") #讀取一筆資料
        # unit = student.objects.get(cPhone= "0914530768")
    except:
        errormessage = "(讀取錯誤!)"
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

def postform(request):  #新增資料，資料必須驗證
    postform = PostForm()  #建立PostForm物件
    return render(request, "postform.html", locals())

def post2(request):  #新增資料，資料必須驗證
	if request.method == "POST":  #如果是以POST方式才處理
		postform = PostForm(request.POST)  #建立forms物件
		if postform.is_valid():			#通過forms驗證
			cName = postform.cleaned_data['cName'] #取得表單輸入資料
			cSex =  postform.cleaned_data['cSex']
			cBirthday =  postform.cleaned_data['cBirthday']
			cEmail = postform.cleaned_data['cEmail']
			cPhone =  postform.cleaned_data['cPhone']
			cAddr =  postform.cleaned_data['cAddr']
			#新增一筆記錄
			unit = student.objects.create(cName=cName, cSex=cSex, cBirthday=cBirthday, cEmail=cEmail,cPhone=cPhone, cAddr=cAddr) 
			unit.save()  #寫入資料庫
			message = '已儲存...'
			return redirect('/index/')	
		else:
			message = '驗證碼錯誤！'	
	else:
		message = '姓名、性別、生日必須輸入！'
		postform = PostForm()
	return render(request, "post2.html", locals())