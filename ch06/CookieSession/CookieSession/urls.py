"""CookieSession URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from CookieSessionApp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^set_cookie/(\w+)/(\w+)/$', views.set_cookie),
    url(r'^set_cookie2/(\w+)/(\w+)/$', views.set_cookie2),
    url(r'^get_cookie/(\w+)/$', views.get_cookie),
    url(r'^get_allcookies/$', views.get_allcookies),
    url(r'^delete_cookie/(\w+)/$', views.delete_cookie),

    url(r'^$', views.index),
    url(r'^index/$', views.index),

    url(r'^set_session/(\w+)/(\w+)$', views.set_session),
    url(r'^get_session/(\w+)/$', views.get_session),
    url(r'^get_allsessions/$', views.get_allsessions),

    # url(r'^vote/$', views.vote),
    # url(r'^set_session2/(\w+)/(\w+)/', views.set_session2),
    # url(r'^delete_session/(\w+)/$', views.delete_session),

    # url(r'^login/$', views.login),
    # url(r'^logout/$', views.logout),
]
