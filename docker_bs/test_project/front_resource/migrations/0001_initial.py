# Generated by Django 2.2.12 on 2022-06-25 03:27

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Resoure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='空空如也', verbose_name='文献标题')),
                ('content', tinymce.models.HTMLField(default='空空如也', verbose_name='文献内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '文献资源',
            },
        ),
    ]
