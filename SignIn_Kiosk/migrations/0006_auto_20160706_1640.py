# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-06 22:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SignIn_Kiosk', '0005_auto_20160706_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='creation_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 22, 40, 23, 371781, tzinfo=utc)),
        ),
    ]
