# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-08 20:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('select_appointment', '0007_auto_20160708_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='scheduled_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 8, 20, 28, 10, 755509, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='cell_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='home_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='race',
            field=models.CharField(choices=[('blank', 'blank'), ('indian', 'indian'), ('asian', 'asian'), ('black', 'black'), ('hawaiian', 'hawaiian'), ('white', 'white'), ('declined', 'declined')], default='blank', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='responsible_party_phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='social_security_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]