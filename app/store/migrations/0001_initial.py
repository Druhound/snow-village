# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.BooleanField(default=False, verbose_name='Опубликовано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('is_active', models.DateTimeField(verbose_name='Дата публикации')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
            },
        ),
    ]