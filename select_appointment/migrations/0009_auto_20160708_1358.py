# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-08 20:58
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('select_appointment', '0008_auto_20160708_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 8, 20, 58, 21, 502727, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ethnicity',
            field=models.CharField(choices=[('blank', 'Blank'), ('hispanic', 'Hispanic'), ('not_hispanic', 'Not Hispanic'), ('declined', 'Decline')], default='blank', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='race',
            field=models.CharField(choices=[('blank', 'blank'), ('indian', 'Indian'), ('asian', 'Asian'), ('black', 'Black'), ('hawaiian', 'Hawaiian'), ('white', 'White'), ('declined', 'Decline')], default='blank', max_length=15, null=True),
        ),
    ]