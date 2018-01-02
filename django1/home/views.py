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
    # return HttpResponse('<h1>Welcome man. kire man</h1>')
    return render(request,'index.html')

def homeTwo(request):
    renderer_classes = (JSONRenderer,)
    # return HttpResponse('<h1>Welcome man. kire man</h1>')
    posts = Stock.objects.get()
    postsData = serializers.serialize('json',[posts])
    print postsData
    args = {'post':posts}
    return HttpResponse(postsData,content_type="application/json")

