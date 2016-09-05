# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-05 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import pinax.news.models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_news', '0002_news_press_release'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='secondary_image',
            field=models.ImageField(blank=True, upload_to=pinax.news.models.image_upload_to),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, upload_to=pinax.news.models.image_upload_to),
        ),
    ]