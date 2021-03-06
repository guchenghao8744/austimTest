# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import testProject,testTask,testInterface,apiBody,apiParams,apiHeader
from .forms import formProject,formTask,formInterface
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
# Create your views here.
from django.http import HttpResponseRedirect,JsonResponse
def home(request):
    list=testProject.objects.all()
    return render(request,'home.html',{'data':list})
def index(request,project_id):
    project=testProject.objects.get(pk=project_id)
    list=testTask.objects.filter(pProject=project)
    print(list)

    return render(request,'index.html',{'data':list,
                                        'project':project_id
                                        })
def interface(request,task_id):
    task = testTask.objects.get(pk=task_id)
    list = testInterface.objects.filter(iTask=task)
    print(list)

    return render(request, 'interface.html', {'data': list,
                                          'task': task_id

                                        })
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def addProject(request):
    if request.method=='POST':
        form = formProject(request.POST)
        if form.is_valid():
            formInfo=form.cleaned_data

            print (formInfo)
            testProject.objects.get_or_create(tName=formInfo['name'])
        return HttpResponseRedirect('/')
def addTask(request,project_id):
    project = testProject.objects.get(pk=project_id)
    if request.method=='POST':
        form = formTask(request.POST)
        if form.is_valid():
            formInfo=form.cleaned_data
            t=testTask()

            print (formInfo)
            t.pPort=formInfo['port']
            t.pHost=formInfo['host']
            t.pName=formInfo['name']
            t.pProject= project
            # testTask.objects.get_or_create(pName=formInfo['name'],pHost=formInfo['po']+formInfo['host'],pPort=formInfo['port'],pPoject=project)
            t.save()
        return HttpResponseRedirect(reverse('autoIndex:task',args=(project_id,)))


def addInterface(request,task_id):
    task=testTask.objects.get(pk=task_id)
    if request.method=='POST':
        form=formInterface(request.POST)
        # print(form)
        if form.is_valid():

            formInfo=form.cleaned_data
            print formInfo
            t = testInterface()
            t.iHttp=formInfo['iHttp']
            t.iName=formInfo['iName']
            t.iType=formInfo['iType']
            t.iurl=formInfo['iurl']
            t.iTask=task
            t.save()
    return HttpResponseRedirect(reverse('autoIndex:interface',args=(task_id,)))

def apiContent(request,api_id):
    api=testInterface.objects.get(pk=api_id)
    # params=apiParams.objects.filter(apiId=api)
    # header=apiParams.objects.filter(apiId=api)
    # body= apiBoby.objects.filter(apiId=api)
    return render(request,'content.html',{
        'apiData':api
    })