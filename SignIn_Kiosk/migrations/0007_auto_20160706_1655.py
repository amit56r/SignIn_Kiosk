# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-06 22:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SignIn_Kiosk', '0006_auto_20160706_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='expires_in',
            new_name='expire_timestamp',
        ),
        migrations.RemoveField(
            model_name='token',
            name='creation_timestamp',
        ),
    ]