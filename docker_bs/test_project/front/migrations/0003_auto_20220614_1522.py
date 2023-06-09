# Generated by Django 2.2.12 on 2022-06-14 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_remove_user_repassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to='avatar'),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='空空如也', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='info',
            field=models.CharField(default='空空如也', max_length=150, verbose_name='个人签名'),
        ),
        migrations.AddField(
            model_name='user',
            name='nickname',
            field=models.CharField(default='空空如也', max_length=50, verbose_name='昵称'),
        ),
    ]
