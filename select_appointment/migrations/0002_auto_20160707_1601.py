# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-07 22:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('select_appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 7, 22, 1, 35, 227310, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='middle_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]