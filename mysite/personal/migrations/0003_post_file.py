# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-19 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_remove_post_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]