# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 20:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max 200 characters', max_length=200, verbose_name='Question')),
                ('author', models.CharField(max_length=50, verbose_name='Your name')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='date published')),
            ],
        ),
    ]
