# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
    ]
