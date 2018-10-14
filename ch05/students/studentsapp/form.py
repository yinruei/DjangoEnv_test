from django import forms

class PostForm(forms.Form):
    cName = forms.CharField(max_length=20,initial='')
    cSex  = forms.CharField(max_length=2,initial='M')
    cBirthday = forms.DateField()
    cEmail  = forms.EmailField(max_length=100,initial='',required=False)#initial表示設定初始值,required表示設定資料是否可選填(預設值True表示資料不可空白)
    cPhone  = forms.CharField(max_length=50,initial='',required=False)
    cAddr   = forms.CharField(max_length=255,initial='',required=False)