# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core import serializers

from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from home.models import Stock
from rest_framework.views import APIView

# Create your views here.

def home(request):
    #hell = Stock.objects.create(open='Apple', ticker='asasdasd', close='wwwwww',volume='444444')
    #hell.save()
    # return HttpResponse('<h1>Welcome man. kire man</h1>')

    #a = Stock.objects.get(id=1)
    #a.open = 'edittttttt'
    #a.save()

    #a = Stock.objects.get(id=4)
    #a.delete()



    return render(request,'index.html')

def homeTwo(request):
    renderer_classes = (JSONRenderer,)
    # return HttpResponse('<h1>Welcome man. kire man</h1>')
    posts = Stock.objects.get()
    print(posts.id)
    args = {'post':posts}


    return render(request,'home-two.html',args)

