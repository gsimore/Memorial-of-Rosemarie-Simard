# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-16 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mewall', '0005_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b'/uploads/'),
        ),
    ]