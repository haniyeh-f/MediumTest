# Generated by Django 3.1.6 on 2021-02-06 19:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('medium', '0013_auto_20210206_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body',
            field=models.TextField(default='-'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(default='blockchain', max_length=255),
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
