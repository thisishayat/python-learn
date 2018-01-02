# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-02 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('open', models.CharField(max_length=10)),
                ('close', models.CharField(max_length=10)),
                ('volume', models.CharField(max_length=10)),
            ],
        ),
    ]
