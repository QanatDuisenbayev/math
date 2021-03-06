# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-10-11 08:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mathapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Elementary_math',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=mathapp.models.generic_filename)),
                ('content', models.TextField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('price', models.PositiveIntegerField(default=0)),
                ('video', models.FileField(null=True, upload_to='user_videos/')),
                ('question1', models.TextField(blank=True, null=True)),
                ('answer1', models.IntegerField(blank=True, null=True)),
                ('block1', models.TextField(blank=True, null=True)),
                ('question2', models.TextField(blank=True, null=True)),
                ('answer2', models.IntegerField(blank=True, null=True)),
                ('block2', models.TextField(blank=True, null=True)),
                ('question3', models.TextField(blank=True, null=True)),
                ('answer3', models.IntegerField(blank=True, null=True)),
                ('block3', models.TextField(blank=True, null=True)),
                ('question4', models.TextField(blank=True, null=True)),
                ('answer4', models.IntegerField(blank=True, null=True)),
                ('block4', models.TextField(blank=True, null=True)),
                ('question5', models.TextField(blank=True, null=True)),
                ('answer5', models.IntegerField(blank=True, null=True)),
                ('block5', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('active', models.BooleanField(default=False)),
                ('session_key', models.CharField(blank=True, max_length=32, null=True)),
                ('exam1', models.IntegerField(default=0)),
                ('exam2', models.IntegerField(default=0)),
                ('exam3', models.IntegerField(default=0)),
                ('exam4', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='logged_in_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
