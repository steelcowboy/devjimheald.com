# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-26 03:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_auto_20170924_2302'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='affiliation',
            options={'ordering': ['-start_date']},
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-start_date']},
        ),
        migrations.AlterModelOptions(
            name='employment',
            options={'ordering': ['-start_date']},
        ),
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['-start_date']},
        ),
    ]
