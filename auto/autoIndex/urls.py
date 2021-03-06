"""auto URL Configuration

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
from . import views
urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^api/task/(\d+)',views.index,name='task'),
    url(r'^api/interface/(\d+)', views.interface, name='interface'),
    url(r'^api/addProject', views.addProject,name='addProject'),
    url(r'^api/addTask/(\d+)', views.addTask, name='addTask'),
    url(r'^api/addInterface/(\d+)', views.addInterface,name='addInterface'),
    url(r'^api/content/(\d+)', views.apiContent,name='content'),

]
