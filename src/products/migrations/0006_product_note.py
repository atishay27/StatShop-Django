# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190402_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='note',
            field=models.TextField(default='ReadMe'),
        ),
    ]
