# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161031_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='draw',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='event',
            name='win1',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='event',
            name='win2',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]