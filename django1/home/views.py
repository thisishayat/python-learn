# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from home.models import Stock
# Create your views here.

def home(request):
    # return HttpResponse('<h1>Welcome man. kire man</h1>')
    return render(request,'index.html')

def homeTwo(request):
    # return HttpResponse('<h1>Welcome man. kire man</h1>')
    posts = Stock.objects.get()
    print posts
    args = {'post':posts}
    return render(request,'home-two.html',args)

