# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-27 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180827_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Kurier_InPost',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='Paczkomaty_InPost',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='Poczta_Polska',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='model_wysylki',
            field=models.BooleanField(default=False),
        ),
    ]
