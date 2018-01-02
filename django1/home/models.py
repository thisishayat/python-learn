# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    open = models.CharField(max_length=10)
    close = models.CharField(max_length=10)
    volume = models.CharField(max_length=10)

    def __long__(self):
        return self