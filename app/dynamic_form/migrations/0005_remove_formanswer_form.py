# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 04:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_form', '0004_auto_20170730_0453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formanswer',
            name='form',
        ),
    ]