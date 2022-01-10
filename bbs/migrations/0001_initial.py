# Generated by Django 4.0 on 2022-01-10 00:03

import bbs.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='カテゴリ')),
                ('path_name', models.CharField(max_length=128, verbose_name='パス名')),
                ('rank', models.IntegerField(default=0, verbose_name='表示順')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('restrict', models.BooleanField(default=False, verbose_name='制限')),
                ('alive', models.BooleanField(default=True, verbose_name='有効')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='タイトル')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='概要')),
                ('src', models.FileField(upload_to=bbs.models.get_upload_to, verbose_name='FilePath')),
                ('rank', models.IntegerField(default=0, verbose_name='表示順')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日')),
                ('alive', models.BooleanField(default=True, verbose_name='有効')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bbs.category', verbose_name='カテゴリ')),
            ],
        ),
    ]