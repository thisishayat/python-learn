# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse('<h1>Welcome man. kire man</h1>')
    return render(request,'index.html')
