from django.conf.urls import url
from django.contrib import admin
from studentsapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^listone/$', views.listone),
	url(r'^listall/$', views.listall),
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    
    url(r'^post/$', views.post),#POST傳送表單
    # url(r'^post1/$', views.post1),#資料新增，資料不驗證
    # url(r'^post2/$', views.post2),#資料新增，資料不驗證
 
    # url(r'^delete/(\d+)/$', views.delete),

    # url(r'^edit/(\d+)/$', views.edit),#由瀏覽器瀏覽
    # url(r'^edit/(\d+)/(\w+)$', views.edit),#由edit.html按送出鈕

    # url(r'^edit2/(\d+)/(\w+)$', views.edit2),
    # url(r'^postform/$', views.postform),#表單驗證
]
