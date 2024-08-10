# Generated by Django 5.0.8 on 2024-08-10 22:35

import bbs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_alter_file_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='img',
            field=models.ImageField(null=True, upload_to=bbs.models.get_upload_to, validators=[bbs.models.image_size], verbose_name='写真ファイル'),
        ),
    ]
