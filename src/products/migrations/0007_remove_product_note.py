# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 19:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='note',
        ),
    ]
