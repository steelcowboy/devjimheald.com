# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-26 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0010_educationpoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationpoint',
            name='keyword',
            field=models.CharField(max_length=50, null=True, verbose_name='Keyword'),
        ),
    ]
