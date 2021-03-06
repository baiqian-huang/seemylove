# Generated by Django 3.0.3 on 2020-02-26 02:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zhujue', models.CharField(default='美女', max_length=64, verbose_name='主角')),
                ('poster', models.CharField(max_length=256, verbose_name='海报img')),
                ('url', models.CharField(max_length=512, verbose_name='目标链接')),
                ('tags', models.CharField(max_length=32, verbose_name='标签分类')),
                ('addtime', models.DateTimeField(default=datetime.datetime(2020, 2, 26, 10, 37, 37, 514869), verbose_name='添加时间')),
                ('fromuser', models.CharField(default='Manager', max_length=64, verbose_name='上传者')),
                ('title', models.CharField(default='美女', max_length=64, verbose_name='标题')),
                ('jieshao', models.CharField(max_length=512, verbose_name='详情介绍')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
    ]
