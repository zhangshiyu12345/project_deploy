# Generated by Django 2.2.12 on 2022-06-23 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0011_comments_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='parent_comment_ID',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
