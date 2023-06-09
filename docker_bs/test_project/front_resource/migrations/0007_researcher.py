# Generated by Django 2.2.12 on 2022-06-26 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_resource', '0006_auto_20220625_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='Researcher',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='专家名字')),
                ('content', models.TextField(default='专家介绍')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '研究人员',
            },
        ),
    ]
