# Generated by Django 4.2.3 on 2023-08-03 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_alter_comment_date_alter_post_date_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=280),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]
