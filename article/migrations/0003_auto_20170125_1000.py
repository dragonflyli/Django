# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-25 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_article_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.CharField(max_length=10000, verbose_name='文章描述'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.IntegerField(choices=[(0, '正常'), (-1, '删除')], default=0, verbose_name='文章状态'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='文章名称'),
        ),
    ]
