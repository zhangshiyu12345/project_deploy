# Generated by Django 2.2.12 on 2022-06-12 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='repassword',
        ),
    ]
