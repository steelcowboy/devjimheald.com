# Generated by Django 2.0.4 on 2018-04-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20180420_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='listen_date',
            field=models.DateField(blank=True, null=True, verbose_name='Listen Date'),
        ),
    ]
