# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-30 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='评论者')),
                ('title', models.CharField(max_length=200, verbose_name='评论标题')),
                ('text', models.TextField(verbose_name='评论内容')),
                ('created_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='创建时间')),
                ('flag', models.IntegerField(choices=[(0, '未删除'), (1, '已删除')], default=0, verbose_name='控制字段')),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Art', verbose_name='关联的小说')),
            ],
            options={
                'verbose_name': '用户评论',
                'verbose_name_plural': '用户评论',
                'db_table': 'comments',
                'ordering': ['-created_time'],
            },
        ),
    ]
