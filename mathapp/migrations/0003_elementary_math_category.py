# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-10-15 17:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mathapp', '0002_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementary_math',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mathapp.Category'),
        ),
    ]